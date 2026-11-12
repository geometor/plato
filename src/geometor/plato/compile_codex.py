"""Deterministic 4-track Book Codex compiler for *Loci Mathematici et Geometrici*.

Parses John Burnet's Oxford Classical Text TEI-XML (`tlg0059.*.burnet_oct.xml`) and
Benjamin Jowett's 3rd-edition English texts (`*_jowett_pg*.txt`), aligns Stephanus
marginal pagination (`.. folio::`) and cross-reference anchors (`.. _stephanus-...:`)
across both primary language tracks, wires standalone interactive `.euclid-graphic`
SVG figures (`.. picture:: /_static/figures/...`), and compiles all companion tracks
(`-en.rst`, `-el.rst`, `-summary.rst`, `-notes.rst`), apparatus pages, and the Book
index (`docsrc/loci_mathematici/index.rst`).
"""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from geometor.plato.apparatus import write_apparatus_artifacts
from geometor.plato.commentary import UNIT_EPIGRAPHS, UNIT_NOTES, UNIT_SUMMARIES
from geometor.plato.concordance import write_concordance_artifacts
from geometor.plato.render import export_all_codex_figures
from geometor.plato.units import (
    CODEX_UNITS,
    DIALOGUE_METADATA,
    CodexUnitSpec,
    PassageSpec,
)

__all__ = [
    "DIALOGUE_FOLIO_ABBR",
    "GreekParagraph",
    "compile_all_codex",
    "extract_burnet_passage",
    "extract_jowett_passage",
]

DIALOGUE_FOLIO_ABBR: dict[str, str] = {
    "meno": "Meno",
    "theaetetus": "Theaet.",
    "republic": "Rep.",
    "timaeus": "Tim.",
    "parmenides": "Parm.",
    "philebus": "Phil.",
    "laws": "Laws",
}

BETA_GREEK_MAP: dict[str, str] = {
    "ou)rano/s, o(rato/s": "οὐρανός, ὁρατός",
    "thei=a": "θεῖα",
    "no/mos": "νόμος",
    "di' a)pisto/n": "δι’ ἄπιστον",
}


@dataclass(frozen=True)
class GreekParagraph:
    """Extracted polytonic Greek speech/paragraph with attached Stephanus milestones."""

    milestones: tuple[str, ...]
    text: str


def _stephanus_sort_key(sec: str) -> tuple[int, str]:
    """Parse ``'509d'`` into sortable ``(509, 'd')``."""
    m = re.match(r"^(\d+)([a-e]?)$", sec.strip().lower())
    if not m:
        return (0, sec.strip().lower())
    return (int(m.group(1)), m.group(2))


def _stephanus_in_range(sec: str, start_sec: str, end_sec: str) -> bool:
    """Return ``True`` when ``start_sec <= sec <= end_sec`` in Stephanus order."""
    if not sec:
        return False
    k = _stephanus_sort_key(sec)
    return _stephanus_sort_key(start_sec) <= k <= _stephanus_sort_key(end_sec)


def _local_tag(elem: ET.Element) -> str:
    """Strip XML namespace URI from an ElementTree tag."""
    return elem.tag.split("}")[-1]


def extract_burnet_passage(
    xml_path: str | Path,
    start_stephanus: str,
    end_stephanus: str,
) -> tuple[list[GreekParagraph], list[tuple[str, float]]]:
    """Extract exact Stephanus slice from a Burnet TEI-XML file.

    Args:
        xml_path: Path to ``tlg0059.*.burnet_oct.xml``.
        start_stephanus: Inclusive start Stephanus section (e.g., ``"75d"``).
        end_stephanus: Inclusive end Stephanus section (e.g., ``"76a"``).

    Returns:
        Tuple ``(paragraphs, milestone_progress)`` where ``milestone_progress`` lists
        each encountered Stephanus section alongside its normalized ``[0.0, 1.0]``
        offset within the extracted passage.
    """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    body = next((el for el in root.iter() if _local_tag(el) == "body"), root)

    start_key = _stephanus_sort_key(start_stephanus)
    end_key = _stephanus_sort_key(end_stephanus)

    active = False
    finished = False
    paragraphs: list[GreekParagraph] = []
    seen_milestones: list[tuple[str, int]] = []
    total_chars = 0

    for p_elem in body.iter():
        if _local_tag(p_elem) != "p":
            continue
        if finished:
            break

        para_chunks: list[str] = []
        para_milestones: list[str] = []

        def _walk(node: ET.Element) -> None:
            nonlocal active, finished
            if finished:
                return
            tag = _local_tag(node)

            if tag == "milestone" and node.attrib.get("unit") == "section":
                sec_val = node.attrib.get("n", "").strip().lower()
                if sec_val:
                    sk = _stephanus_sort_key(sec_val)
                    if sk > end_key:
                        if active:
                            finished = True
                            return
                    elif sk >= start_key:
                        active = True
                        if sec_val not in para_milestones and not any(
                            m_id == sec_val for m_id, _ in seen_milestones
                        ):
                            para_milestones.append(sec_val)

            if tag in {"note", "bibl"}:
                return

            if tag == "label":
                lbl = (node.text or "").strip()
                if active and lbl:
                    para_chunks.append(f"**{lbl}** ")
                return

            if tag == "q":
                if active:
                    para_chunks.append("«")
                if node.text and active:
                    para_chunks.append(node.text)
                for child in node:
                    _walk(child)
                    if finished:
                        return
                    if child.tail and active:
                        para_chunks.append(child.tail)
                if active:
                    para_chunks.append("»")
                return

            if node.text and active:
                para_chunks.append(node.text)

            for child in node:
                _walk(child)
                if finished:
                    return
                if child.tail and active:
                    para_chunks.append(child.tail)

        _walk(p_elem)

        cleaned = re.sub(r"\s+", " ", "".join(para_chunks)).strip()
        cleaned = re.sub(r"«\s+", "«", cleaned)
        cleaned = re.sub(r"\s+»", "»", cleaned)
        if cleaned or para_milestones:
            for ms in para_milestones:
                seen_milestones.append((ms, total_chars))
            if cleaned:
                paragraphs.append(
                    GreekParagraph(milestones=tuple(para_milestones), text=cleaned)
                )
                total_chars += len(cleaned)
            elif para_milestones and paragraphs:
                prev = paragraphs[-1]
                paragraphs[-1] = GreekParagraph(
                    milestones=prev.milestones + tuple(para_milestones),
                    text=prev.text,
                )

    denom = max(total_chars, 1)
    milestone_progress = [(ms, min(1.0, offset / denom)) for ms, offset in seen_milestones]
    return paragraphs, milestone_progress


def _strip_nested_footnotes(text: str) -> str:
    """Remove Gutenberg ``[Footnote N: ...]`` blocks even when containing nested ``[...]``."""
    out: list[str] = []
    idx = 0
    n = len(text)
    while idx < n:
        if text.startswith("[Footnote", idx):
            depth = 0
            while idx < n:
                if text[idx] == "[":
                    depth += 1
                elif text[idx] == "]":
                    depth -= 1
                    if depth <= 0:
                        idx += 1
                        break
                idx += 1
        else:
            out.append(text[idx])
            idx += 1
    return "".join(out)


def _clean_jowett_block(raw_text: str) -> str:
    """Clean Project Gutenberg sidenotes, footnotes, page braces, and Beta Code tokens."""
    cleaned = re.sub(r"\[Sidenote:.*?\]", "", raw_text, flags=re.S)
    cleaned = _strip_nested_footnotes(cleaned)
    cleaned = re.sub(r"\{\d+\}", "", cleaned)
    cleaned = re.sub(r"\{[ivxlcdmIVXLCDM]+\}", "", cleaned)
    cleaned = re.sub(r"\[\d+\]", "", cleaned)

    def _replace_greek(match: re.Match[str]) -> str:
        inner = match.group(1).strip()
        return BETA_GREEK_MAP.get(inner, inner)

    cleaned = re.sub(r"\[Greek:\s*([^\]]+)\]", _replace_greek, cleaned)
    return cleaned


def _format_speaker_prefix(para: str) -> str:
    """Format uppercase speaker prefixes (e.g., ``SOCRATES:``) as bold RST lead-ins."""
    m = re.match(r"^(\(?[A-Z][A-Z\s]{1,22}):\s+(.*)$", para)
    if m:
        speaker = m.group(1).strip()
        rest = m.group(2).strip()
        if speaker.startswith("("):
            return f"*(**{speaker[1:]}:** {rest}"
        return f"**{speaker}:** {rest}"
    return para


def extract_jowett_passage(
    txt_path: str | Path,
    passage: PassageSpec,
    milestone_progress: list[tuple[str, float]],
) -> list[tuple[list[str], str]]:
    """Extract and Stephanus-align a Jowett English passage into paragraphs.

    Args:
        txt_path: Path to ``*_jowett_pg*.txt``.
        passage: :class:`~geometor.plato.units.PassageSpec` definition.
        milestone_progress: Ordered ``(sec, fraction)`` list from Burnet TEI-XML.

    Returns:
        List of ``(stephanus_milestones, paragraph_text)`` pairs.
    """
    lines = Path(txt_path).read_text(encoding="utf-8").splitlines()
    raw_slice = "\n".join(lines[passage.jowett_start_line - 1 : passage.jowett_end_line])
    cleaned_slice = _clean_jowett_block(raw_slice)

    raw_paras = [
        re.sub(r"\s+", " ", blk).strip()
        for blk in re.split(r"\n\s*\n", cleaned_slice)
        if blk.strip()
    ]

    para_milestones: list[list[str]] = [[] for _ in raw_paras]
    emitted_secs: set[str] = set()
    clean_paras: list[str] = []

    for p_idx, para in enumerate(raw_paras):
        found_inline = re.findall(r"\*(\d+[A-Ea-e])\*", para)
        for tok in found_inline:
            sec_low = tok.lower()
            if (
                _stephanus_in_range(sec_low, passage.start_stephanus, passage.end_stephanus)
                and sec_low not in emitted_secs
            ):
                para_milestones[p_idx].append(sec_low)
                emitted_secs.add(sec_low)

        para_no_stars = re.sub(r"\*\d+[A-Ea-e]\*\s*", "", para)
        para_no_stars = re.sub(r"\s+", " ", para_no_stars).strip()
        clean_paras.append(_format_speaker_prefix(para_no_stars))

    # Align any remaining Burnet Stephanus milestones proportionally across paragraphs
    if clean_paras and milestone_progress:
        n_paras = len(clean_paras)
        min_idx = 0
        for sec, frac in milestone_progress:
            if sec in emitted_secs:
                # Advance monotonic floor if already placed via inline marker
                for idx_existing, mlist in enumerate(para_milestones):
                    if sec in mlist:
                        min_idx = max(min_idx, idx_existing)
                        break
                continue
            target_idx = max(min_idx, min(n_paras - 1, int(round(frac * (n_paras - 1)))))
            para_milestones[target_idx].append(sec)
            emitted_secs.add(sec)
            min_idx = target_idx

    # Ensure start_stephanus is always anchored on the opening paragraph if absent
    if clean_paras and passage.start_stephanus not in emitted_secs:
        para_milestones[0].insert(0, passage.start_stephanus)

    return [(para_milestones[i], clean_paras[i]) for i in range(len(clean_paras)) if clean_paras[i]]


def _render_picture_block(unit: CodexUnitSpec) -> list[str]:
    """Render standalone interactive ``.. picture::`` block for a Codex unit."""
    return [
        f".. picture:: /_static/figures/{unit.figure_svg}",
        f"   :alt: {unit.title}",
        f"   :caption: {unit.figure_caption}",
        "",
    ]


def _render_unit_en_rst(
    unit: CodexUnitSpec,
    order_num: int,
    sources_dir: Path,
    en_passages_cache: dict[str, list[tuple[list[str], str]]],
) -> str:
    """Render ``<slug>/<slug>-en.rst``."""
    ep_el, ep_en, ep_loc = UNIT_EPIGRAPHS[unit.slug]
    lines = [
        f":order: {order_num}",
        ":layout: book",
        f":title: {unit.unit_number} — {unit.title}",
        f":canonical_id: {unit.stephanus_summary}",
        f":original_id: Stephanus {unit.stephanus_summary}",
        f":folio: {unit.stephanus_summary}",
        "",
        f".. _{unit.slug}:",
        f".. _{unit.slug}-en:",
        "",
        "=" * len(f"{unit.unit_number} — {unit.title}"),
        f"{unit.unit_number} — {unit.title}",
        "=" * len(f"{unit.unit_number} — {unit.title}"),
        "",
        f".. rubric:: {unit.subtitle}",
        "",
        ".. epigraph::",
        "",
        f"   *{ep_el}*",
        "",
        f"   {ep_en} — **{ep_loc}**",
        "",
        *_render_picture_block(unit),
    ]

    emitted_global_anchors: set[str] = set()
    for passage in unit.passages:
        meta = DIALOGUE_METADATA[passage.dialogue_key]
        abbr = DIALOGUE_FOLIO_ABBR[passage.dialogue_key]
        lines.extend(
            [
                f".. _{passage.passage_id}-en:",
                "",
                passage.heading,
                "-" * len(passage.heading),
                "",
                f"*English Translation by Benjamin Jowett (3rd ed., 1892) · {meta['jowett_pg']}*",
                "",
            ]
        )

        for mlist, para_text in en_passages_cache[passage.passage_id]:
            for sec in mlist:
                anchor = f"stephanus-{passage.dialogue_key}-{sec}"
                if anchor not in emitted_global_anchors:
                    lines.append(f".. _{anchor}:")
                    emitted_global_anchors.add(anchor)
            if mlist:
                lines.append("")
                lines.append(f".. folio:: {abbr} {mlist[-1]}")
                lines.append("")
            lines.append(para_text)
            lines.append("")

    return "\n".join(lines)


def _render_unit_el_rst(
    unit: CodexUnitSpec,
    el_passages_cache: dict[str, list[GreekParagraph]],
) -> str:
    """Render ``<slug>/<slug>-el.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Greek (Burnet OCT)"
    lines = [
        ":layout: book",
        ":type: el",
        f":title: {heading_main}",
        f":canonical_id: {unit.stephanus_summary}",
        f":original_id: Stephanus {unit.stephanus_summary}",
        f":folio: {unit.stephanus_summary}",
        "",
        f".. _{unit.slug}-el:",
        "",
        "=" * len(heading_main),
        heading_main,
        "=" * len(heading_main),
        "",
        f".. rubric:: Editio Graeca Oxoniensis (Ioannes Burnet, 1900–1907) · {unit.stephanus_summary}",
        "",
        *_render_picture_block(unit),
    ]

    emitted_el_anchors: set[str] = set()
    for passage in unit.passages:
        meta = DIALOGUE_METADATA[passage.dialogue_key]
        abbr = DIALOGUE_FOLIO_ABBR[passage.dialogue_key]
        sec_head = f"{passage.dialogue_title_el} ({passage.stephanus_range}) — {passage.heading}"
        lines.extend(
            [
                f".. _{passage.passage_id}-el:",
                "",
                sec_head,
                "-" * len(sec_head),
                "",
                f"*{meta['burnet_vol']} · {meta['tlg_id']}*",
                "",
            ]
        )

        for gp in el_passages_cache[passage.passage_id]:
            for sec in gp.milestones:
                anchor = f"stephanus-el-{passage.dialogue_key}-{sec}"
                if anchor not in emitted_el_anchors:
                    lines.append(f".. _{anchor}:")
                    emitted_el_anchors.add(anchor)
            if gp.milestones:
                lines.append("")
                lines.append(f".. folio:: {abbr} {gp.milestones[-1]}")
                lines.append("")
            lines.append(gp.text)
            lines.append("")

    return "\n".join(lines)


def _render_unit_summary_rst(unit: CodexUnitSpec) -> str:
    """Render ``<slug>/<slug>-summary.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Structural Synopsis"
    lines = [
        ":layout: book",
        ":type: summary",
        f":title: {unit.unit_number} — {unit.title} — Summary",
        f":canonical_id: {unit.stephanus_summary}",
        f":original_id: Stephanus {unit.stephanus_summary}",
        f":folio: {unit.stephanus_summary}",
        "",
        f".. _{unit.slug}-summary:",
        "",
        "=" * len(heading_main),
        heading_main,
        "=" * len(heading_main),
        "",
        f".. rubric:: Argumentative Architecture & Interactive Diagram Guide · {unit.stephanus_summary}",
        "",
        *_render_picture_block(unit),
        UNIT_SUMMARIES[unit.slug],
        "",
    ]
    return "\n".join(lines)


def _render_unit_notes_rst(unit: CodexUnitSpec) -> str:
    """Render ``<slug>/<slug>-notes.rst``."""
    heading_main = f"{unit.unit_number} — {unit.title} — Critical Commentary & Notes"
    lines = [
        ":layout: book",
        ":type: notes",
        f":title: {unit.unit_number} — {unit.title} — Notes",
        f":canonical_id: {unit.stephanus_summary}",
        f":original_id: Stephanus {unit.stephanus_summary}",
        f":folio: {unit.stephanus_summary}",
        "",
        f".. _{unit.slug}-notes:",
        "",
        "=" * len(heading_main),
        heading_main,
        "=" * len(heading_main),
        "",
        f".. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · {unit.stephanus_summary}",
        "",
        *_render_picture_block(unit),
        UNIT_NOTES[unit.slug],
        "",
        "IV. Executable Symbolic Verification",
        "------------------------------------",
        "",
        (
            "In accordance with GEOMETOR's strict content/code separation for historical editions, "
            "executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification "
            f"routines for **{unit.unit_number}** live in ``src/geometor/plato/`` and the companion "
            f"walkthrough :doc:`{unit.demo_doc}`."
        ),
        "",
    ]
    return "\n".join(lines)


def render_book_index_rst() -> str:
    """Render ``docsrc/loci_mathematici/index.rst``."""
    lines = [
        ":order: 1",
        ":layout: book",
        ":book_title: Loci Mathematici et Geometrici",
        ":book_subtitle: Plato (c. 428–347 BC) · Burnet Greek OCT (1900–1907) & Jowett English Codex",
        ":author: Plato of Athens",
        ":book_theme: classical-serif",
        "",
        ".. _loci-mathematici:",
        "",
        "==============================================================================",
        "Loci Mathematici et Geometrici — Plato on Geometry, Proportion & Noetic Ascent",
        "==============================================================================",
        "",
        ".. rubric:: Synchronized 4-Track Book Codex (English · Greek Burnet OCT · Summary · Critical Notes)",
        "",
        (
            "**Loci Mathematici et Geometrici** unites into a single critical Digital Scriptorium "
            "edition the eleven foundational mathematical and geometric passages across seven dialogues "
            "of :person:`Plato of Athens <plato>` (*Meno*, *Theaetetus*, *Republic* VI–VII, *Timaeus*, "
            "*Parmenides*, *Philebus*, and *Laws* VII) that established deductive hypothesis, quadratic "
            ":term:`powers <dynamis>`, the :term:`Divided Line <dianoia>` and Quadrivium, harmonic "
            ":term:`proportion <analogia>`, the five cosmic polyhedra, and :term:`Limit <peras>`."
        ),
        "",
        (
            "Every unit is presented across **four synchronized tracks**—**English** (:person:`Benjamin "
            "Jowett's <jowett>` public-domain 3rd edition, 1892), **Greek (Burnet OCT)** (:person:`John "
            "Burnet's <burnet>` *Platonis Opera*, 1900–1907), **Summary**, and **Critical Notes** "
            "(pairing interactive ``.euclid-graphic`` SVG diagrams and literal Greek mathematical "
            "philology with reception across :person:`Euclid <euclid>`, :person:`Proclus <proclus>`, "
            ":person:`Aristotle <aristotle>`, :person:`Pacioli <pacioli>`, and :person:`Hoenen <hoenen>`)."
        ),
        "",
        "Units I–VI — Mathematical & Geometric Dialogues",
        "-----------------------------------------------",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "   :caption: Loci Mathematici",
        "",
    ]

    for unit in CODEX_UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-en")

    lines.extend(
        [
            "",
            "Critical Apparatus & Stephanus Concordance",
            "------------------------------------------",
            "",
            ".. toctree::",
            "   :maxdepth: 1",
            "   :caption: Critical Apparatus",
            "",
            "   concordance",
            "   bibliography",
            "   persons",
            "   glossary",
            "",
            ".. toctree::",
            "   :hidden:",
            "",
        ]
    )

    for unit in CODEX_UNITS:
        lines.append(f"   {unit.slug}/{unit.slug}-el")
        lines.append(f"   {unit.slug}/{unit.slug}-summary")
        lines.append(f"   {unit.slug}/{unit.slug}-notes")

    lines.append("")
    return "\n".join(lines)


def compile_all_codex(repo_root: str | Path, *, regen_figures: bool = True) -> dict[str, Path]:
    """Compile all 4-track Codex units, apparatus JSON/RST files, concordance, and SVG figures.

    Args:
        repo_root: Root directory of ``geometor/plato``.
        regen_figures: When ``True`` (default), regenerate all 6 ``.euclid-graphic`` SVGs.

    Returns:
        Mapping of relative output paths to resolved :class:`~pathlib.Path` objects.
    """
    root = Path(repo_root)
    sources_dir = root / "resources" / "loci_mathematici" / "sources"
    codex_dir = root / "docsrc" / "loci_mathematici"
    codex_dir.mkdir(parents=True, exist_ok=True)

    written: dict[str, Path] = {}

    if regen_figures:
        fig_map = export_all_codex_figures(root / "docsrc" / "_static" / "figures")
        for _, fpath in fig_map.items():
            written[str(fpath.relative_to(root))] = fpath

    written.update(write_apparatus_artifacts(root))
    written.update(write_concordance_artifacts(root))

    index_path = codex_dir / "index.rst"
    index_path.write_text(render_book_index_rst(), encoding="utf-8")
    written[str(index_path.relative_to(root))] = index_path

    for idx, unit in enumerate(CODEX_UNITS, start=1):
        unit_dir = codex_dir / unit.slug
        unit_dir.mkdir(parents=True, exist_ok=True)

        el_cache: dict[str, list[GreekParagraph]] = {}
        en_cache: dict[str, list[tuple[list[str], str]]] = {}

        for passage in unit.passages:
            el_paras, progress = extract_burnet_passage(
                sources_dir / "el" / passage.burnet_xml,
                passage.start_stephanus,
                passage.end_stephanus,
            )
            en_paras = extract_jowett_passage(
                sources_dir / "en" / passage.jowett_txt,
                passage,
                progress,
            )
            el_cache[passage.passage_id] = el_paras
            en_cache[passage.passage_id] = en_paras

        track_files = {
            f"{unit.slug}-en.rst": _render_unit_en_rst(unit, idx * 10, sources_dir, en_cache),
            f"{unit.slug}-el.rst": _render_unit_el_rst(unit, el_cache),
            f"{unit.slug}-summary.rst": _render_unit_summary_rst(unit),
            f"{unit.slug}-notes.rst": _render_unit_notes_rst(unit),
        }

        for fname, content in track_files.items():
            target = unit_dir / fname
            target.write_text(content, encoding="utf-8")
            written[str(target.relative_to(root))] = target

    return written
