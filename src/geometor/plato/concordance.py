"""Stephanus concordance and SHA-256 primary-source manifest for *geometor-plato*.

Reconciles every ``plato:*`` citation across the GEOMETOR canon (``euclid``,
``elements``, ``proclus``, ``aristotle``, ``hoenen``, and ``pacioli`` — 58
repository-level citation entries across 63 apparatus files, 33 distinct
normalized citation keys) against canonical Stephanus anchors in the six units of
*Loci Mathematici et Geometrici*, and records cryptographic SHA-256 checksums for
all 14 public-domain Burnet (1900–1907) and Jowett (1892) source texts.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from geometor.plato.units import CODEX_UNITS, DIALOGUE_METADATA

__all__ = [
    "CROSS_CORPUS_PLATO_ENTRIES",
    "ConcordanceEntry",
    "SourceFileRecord",
    "build_concordance_data",
    "build_sources_manifest",
    "render_concordance_rst",
    "write_concordance_artifacts",
]


@dataclass(frozen=True)
class ConcordanceEntry:
    """Canonical cross-corpus Plato citation mapping to Stephanus anchors.

    Attributes:
        cite_key: Exact citation key used in sister repositories (e.g., ``"plato:meno:76A"``).
        repos: Tuple of sister repositories declaring this key.
        dialogue: Canonical Platonic dialogue title.
        stephanus_locus: Normalized Stephanus coordinate or span.
        in_codex: ``True`` when staged verbatim in Units I–VI; ``False`` for peripheral
            civic/mimetic passages catalogued in Critical Notes.
        unit_slug: Target unit folder slug in ``docsrc/loci_mathematici/`` (or nearest note unit).
        stephanus_anchor: Exact RST target label ``stephanus-<dialogue>-<sec>`` (when ``in_codex``).
        euclid_proclus_context: Mathematical/philosophical locus in Euclid, Proclus, Aristotle,
            Hoenen, or Pacioli.
    """

    cite_key: str
    repos: tuple[str, ...]
    dialogue: str
    stephanus_locus: str
    in_codex: bool
    unit_slug: str
    stephanus_anchor: str
    euclid_proclus_context: str


@dataclass(frozen=True)
class SourceFileRecord:
    """Cryptographically verified primary-source file metadata."""

    dialogue_key: str
    language: str
    edition: str
    relative_path: str
    size_bytes: int
    sha256: str


# Complete canonical inventory of all 58 repository-level plato:* entries across the 6 sister
# GEOMETOR repositories (33 unique keys; 63 total apparatus file entries including mirrors).
CROSS_CORPUS_PLATO_ENTRIES: tuple[ConcordanceEntry, ...] = (
    # --- Unit I: Meno ---
    ConcordanceEntry(
        cite_key="plato:meno:76A",
        repos=("euclid", "elements"),
        dialogue="Meno",
        stephanus_locus="75d–76a",
        in_codex=True,
        unit_slug="meno",
        stephanus_anchor="stephanus-meno-76a",
        euclid_proclus_context=(
            "Euclid Elements I, Defs. 13–14 & Proclus Friedlein 136–143: "
            "figure (schema) defined as limit of solid (stereou peras)."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:meno",
        repos=("aristotle",),
        dialogue="Meno",
        stephanus_locus="80d–86c",
        in_codex=True,
        unit_slug="meno",
        stephanus_anchor="stephanus-meno-81e",
        euclid_proclus_context=(
            "Aristotle Anal. Post. I.1 (71a29) & Anal. Prior. II.21 (67a21): "
            "Meno's paradox of inquiry resolved via universal vs. particular recognition."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:meno:81e-85d",
        repos=("proclus",),
        dialogue="Meno",
        stephanus_locus="81e–85d",
        in_codex=True,
        unit_slug="meno",
        stephanus_anchor="stephanus-meno-81e",
        euclid_proclus_context=(
            "Proclus In Euclidem Prologue I (Friedlein 45.15–46.3): mathematical "
            "recollection (anamnesis) awakened through diagrammatic discovery."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:meno:82b-85b",
        repos=("hoenen",),
        dialogue="Meno",
        stephanus_locus="82b–85b",
        in_codex=True,
        unit_slug="meno",
        stephanus_anchor="stephanus-meno-82b",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae Cap. I & VII: intellectual insight "
            "(intuitus mentis) into the necessary nexus Q = 4 + 4 = 8 in the singular diagram."
        ),
    ),
    # --- Unit II: Theaetetus ---
    ConcordanceEntry(
        cite_key="plato:theaetetus",
        repos=("euclid", "elements"),
        dialogue="Theaetetus",
        stephanus_locus="147c–148b",
        in_codex=True,
        unit_slug="theaetetus",
        stephanus_anchor="stephanus-theaetetus-147c",
        euclid_proclus_context=(
            "Euclid Elements Book X Introduction (Heath Vol. III, pp. 1–4): "
            "historical origin of the theory of irrationals in the Academy."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:theaetetus:147.d",
        repos=("euclid", "elements"),
        dialogue="Theaetetus",
        stephanus_locus="147d",
        in_codex=True,
        unit_slug="theaetetus",
        stephanus_anchor="stephanus-theaetetus-147d",
        euclid_proclus_context=(
            "Euclid Elements X, Defs. 1–4: commensurable in length (mekei) vs. "
            "commensurable in square/power only (dynamei)."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:theaetetus:147D",
        repos=("euclid", "elements"),
        dialogue="Theaetetus",
        stephanus_locus="147d",
        in_codex=True,
        unit_slug="theaetetus",
        stephanus_anchor="stephanus-theaetetus-147d",
        euclid_proclus_context=(
            "Euclid Elements X.9 & Scholium: Theodorus's individual proofs from "
            "3 to 17 square feet generalized by Theaetetus."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:theaetetus:147.d.sqq",
        repos=("euclid", "elements"),
        dialogue="Theaetetus",
        stephanus_locus="147d–148b",
        in_codex=True,
        unit_slug="theaetetus",
        stephanus_anchor="stephanus-theaetetus-147d",
        euclid_proclus_context=(
            "Euclid Elements VII, Defs. 16–19: plane, equilateral square (isos isakis), "
            "and oblong (promekes) numbers."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:theaetetus:147-e-148-b",
        repos=("euclid", "elements"),
        dialogue="Theaetetus",
        stephanus_locus="147e–148b",
        in_codex=True,
        unit_slug="theaetetus",
        stephanus_anchor="stephanus-theaetetus-147e",
        euclid_proclus_context=(
            "Euclid Elements X.9: exact number-theoretic criterion for rational "
            "lengths (meke) vs. quadratic surds (dynameis)."
        ),
    ),
    # --- Unit III: Republic VI–VII ---
    ConcordanceEntry(
        cite_key="plato:rep",
        repos=("euclid", "elements"),
        dialogue="Republic",
        stephanus_locus="VI 509d–511e; VII 525a–534e",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-509d",
        euclid_proclus_context=(
            "Euclid Elements Vol. I Ch. IX: Plato's philosophy of mathematical "
            "hypotheses, definitions, and deductive method."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:republic",
        repos=("aristotle",),
        dialogue="Republic",
        stephanus_locus="VI 509d–511e; VII 525a–534d",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-509d",
        euclid_proclus_context=(
            "Aristotle Metaphysics B.2, M.1–3 & Anal. Post. I.10: mathematical "
            "intermediates (ta mathematika), dianoia, and unhypothetical first principles."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VI.510b-511d",
        repos=("proclus",),
        dialogue="Republic",
        stephanus_locus="VI 510b–511d",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-510b",
        euclid_proclus_context=(
            "Proclus In Euclidem Prologue I (Friedlein 10.15–11.25, 29.14–32.20): "
            "dianoia as the proper cognitive faculty of geometry between nous and opinion."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VI.510C",
        repos=("euclid", "elements"),
        dialogue="Republic",
        stephanus_locus="VI 510c",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-510c",
        euclid_proclus_context=(
            "Euclid Elements I, Defs. 10–12: geometers hypothesize the odd and even, "
            "the figures, and the three species of angles (right, obtuse, acute)."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VI.510c",
        repos=("hoenen",),
        dialogue="Republic",
        stephanus_locus="VI 510c–511a",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-510c",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae Cap. I: geometers use visible figures as "
            "images while reasoning about the square itself and the diagonal itself."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VII.525a-534e",
        repos=("proclus",),
        dialogue="Republic",
        stephanus_locus="VII 525a–534e",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-525a",
        euclid_proclus_context=(
            "Proclus In Euclidem Prologue I (Friedlein 20.8–24.20, 35.17–42.8): "
            "the five mathematical sciences as the cathartic ascent to dialectic."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:528.b.d",
        repos=("euclid", "elements"),
        dialogue="Republic",
        stephanus_locus="VII 528b–d",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-528b",
        euclid_proclus_context=(
            "Euclid Elements Book XI Introduction: Plato's programmatic critique of "
            "leaping from plane geometry to astronomy before cultivating 3D stereometry."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VII.532c",
        repos=("hoenen",),
        dialogue="Republic",
        stephanus_locus="VII 532c",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-532c",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae: liberation of the eye of the soul from "
            "sensible shadows through mathematical arts."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:VII.533c",
        repos=("hoenen",),
        dialogue="Republic",
        stephanus_locus="VII 533c",
        in_codex=True,
        unit_slug="republic",
        stephanus_anchor="stephanus-republic-533c",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae: geometry dreams about being so long as "
            "it leaves its hypotheses unmoved without ascending to the unhypothetical."
        ),
    ),
    # --- Unit IV: Timaeus (Proportion & World-Soul) ---
    ConcordanceEntry(
        cite_key="plato:timaeus:31c-36d",
        repos=("proclus",),
        dialogue="Timaeus",
        stephanus_locus="31c–36d",
        in_codex=True,
        unit_slug="timaeus-world-soul",
        stephanus_anchor="stephanus-timaeus-31c",
        euclid_proclus_context=(
            "Proclus In Euclidem & In Timaeum: geometric analogia as the fairest "
            "cosmic bond and harmonic constitution of the World-Soul."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:timaeus:32-a-b",
        repos=("euclid", "elements"),
        dialogue="Timaeus",
        stephanus_locus="32a–b",
        in_codex=True,
        unit_slug="timaeus-world-soul",
        stephanus_anchor="stephanus-timaeus-32a",
        euclid_proclus_context=(
            "Euclid Elements VIII.11–12: one mean proportional suffices between "
            "two square/plane numbers, whereas two means are required between solid cubes."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:timaeus:32-a-sqq",
        repos=("euclid", "elements"),
        dialogue="Timaeus",
        stephanus_locus="32a–c",
        in_codex=True,
        unit_slug="timaeus-world-soul",
        stephanus_anchor="stephanus-timaeus-32a",
        euclid_proclus_context=(
            "Euclid Elements VIII.11–12 & V, Def. 9–10: duplicate and triplicate "
            "ratios of plane and solid numbers."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:timaeus:32.a.b",
        repos=("euclid", "elements"),
        dialogue="Timaeus",
        stephanus_locus="32a–b",
        in_codex=True,
        unit_slug="timaeus-world-soul",
        stephanus_anchor="stephanus-timaeus-32a",
        euclid_proclus_context=(
            "Euclid Elements VIII.11–12: architectural necessity of four elements "
            "(fire, air, water, earth) from double geometric means."
        ),
    ),
    # --- Unit V: Timaeus (Elementary Triangles & Cosmic Polyhedra) ---
    ConcordanceEntry(
        cite_key="plato:timaeus",
        repos=("euclid", "elements", "aristotle"),
        dialogue="Timaeus",
        stephanus_locus="31b–36d, 53c–56c",
        in_codex=True,
        unit_slug="timaeus-polyhedra",
        stephanus_anchor="stephanus-timaeus-53c",
        euclid_proclus_context=(
            "Euclid Elements Book XIII & Aristotle De Caelo III.7–8 (306a1–307b18): "
            "resolution of elemental bodies into planar right triangles."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:timaeus:53c-56c",
        repos=("pacioli",),
        dialogue="Timaeus",
        stephanus_locus="53c–56c",
        in_codex=True,
        unit_slug="timaeus-polyhedra",
        stephanus_anchor="stephanus-timaeus-53c",
        euclid_proclus_context=(
            "Luca Pacioli De Divina Proportione (1509, 9 citations across Caps. V, XXV–LV): "
            "the five regular Platonic bodies assigned to fire, earth, air, water, and the cosmos."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:timaeus:54-d-e",
        repos=("euclid", "elements"),
        dialogue="Timaeus",
        stephanus_locus="54d–e",
        in_codex=True,
        unit_slug="timaeus-polyhedra",
        stephanus_anchor="stephanus-timaeus-54d",
        euclid_proclus_context=(
            "Euclid Elements XIII.13–17: six 1:sqrt(3):2 half-equilateral scalene "
            "triangles compose each equilateral cosmic face."
        ),
    ),
    # --- Unit VI: Parmenides, Philebus & Laws VII ---
    ConcordanceEntry(
        cite_key="plato:parm:137E",
        repos=("euclid", "elements"),
        dialogue="Parmenides",
        stephanus_locus="137e",
        in_codex=True,
        unit_slug="foundations",
        stephanus_anchor="stephanus-parmenides-137e",
        euclid_proclus_context=(
            "Euclid Elements I, Def. 4 & Def. 15: Plato's optical definition of "
            "the straight line ('middle blocks both extremes') and equidistant circle."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:parmenides:137e",
        repos=("proclus",),
        dialogue="Parmenides",
        stephanus_locus="137e",
        in_codex=True,
        unit_slug="foundations",
        stephanus_anchor="stephanus-parmenides-137e",
        euclid_proclus_context=(
            "Proclus In Euclidem (Friedlein 109.21–110.16): commentary on Plato's "
            "optical characterization of straightness vs. Euclid I, Def. 4."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:parm:145B",
        repos=("euclid", "elements"),
        dialogue="Parmenides",
        stephanus_locus="145a–b",
        in_codex=True,
        unit_slug="foundations",
        stephanus_anchor="stephanus-parmenides-145b",
        euclid_proclus_context=(
            "Euclid Elements I, Defs. 13–14: figure (schema), beginning, middle "
            "equally distant from extremes, round, straight, or mixed."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:philebus:16c-26d",
        repos=("proclus",),
        dialogue="Philebus",
        stephanus_locus="16c–26d",
        in_codex=True,
        unit_slug="foundations",
        stephanus_anchor="stephanus-philebus-16c",
        euclid_proclus_context=(
            "Proclus In Euclidem Prologue I (Friedlein 5.18–7.12): Limit (peras) "
            "and Unlimited (apeiron) as supreme ontological principles of geometry."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:laws:817.e",
        repos=("euclid", "elements"),
        dialogue="Laws",
        stephanus_locus="VII 817e–820d",
        in_codex=True,
        unit_slug="foundations",
        stephanus_anchor="stephanus-laws-817e",
        euclid_proclus_context=(
            "Euclid Elements Book X & Book VII: three liberal mathematical sciences "
            "and the scandal of ignorance regarding incommensurable lengths, surfaces, and solids."
        ),
    ),
    # --- Peripheral Civic / Mimetic Loci (Catalogued in Apparatus & Notes) ---
    ConcordanceEntry(
        cite_key="plato:leges:737e-738b",
        repos=("hoenen",),
        dialogue="Laws",
        stephanus_locus="V 737e–738b",
        in_codex=False,
        unit_slug="republic",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae Cap. IV: civic number 5,040 (= 7!) divisible "
            "by every integer from 1 to 10 (59 proper divisors); analyzed in Unit III Notes."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:leges:738a",
        repos=("hoenen",),
        dialogue="Laws",
        stephanus_locus="V 738a",
        in_codex=False,
        unit_slug="republic",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Hoenen De Noetica Geometriae Cap. IV: Plato's exact divisor theorem for "
            "5,040 (divisible by 1..12 except 11, which divides 5,038); analyzed in Unit III Notes."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:laws:777D",
        repos=("euclid", "elements"),
        dialogue="Laws",
        stephanus_locus="VI 777d",
        in_codex=False,
        unit_slug="foundations",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Heath on Euclid Common Notion 3: Plato's proverbial 'if equals be added "
            "to unequals, the wholes remain unequal'; contextualized in Unit VI Notes."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:417",
        repos=("euclid", "elements"),
        dialogue="Republic",
        stephanus_locus="III 416d–417b",
        in_codex=False,
        unit_slug="republic",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Peripheral civic reference in Heath's philological notes on terminology; "
            "outside mathematical curriculum."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:rep:X.602c",
        repos=("euclid", "elements"),
        dialogue="Republic",
        stephanus_locus="X 602c–603a",
        in_codex=False,
        unit_slug="foundations",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Heath on Optics & Measurement: bent-stick refraction illusion overcome "
            "by numbering, measuring, and weighing (metretike); analyzed in Unit VI Notes."
        ),
    ),
    ConcordanceEntry(
        cite_key="plato:sophist:235.d",
        repos=("euclid", "elements"),
        dialogue="Sophist",
        stephanus_locus="235d–236c",
        in_codex=False,
        unit_slug="foundations",
        stephanus_anchor="",
        euclid_proclus_context=(
            "Heath on Perspective Optics (scenographia): true symmetry (eikastike) vs. "
            "foreshortened optical appearance (phantastike); analyzed in Unit VI Notes."
        ),
    ),
)


def _sha256_file(path: Path) -> str:
    """Compute hex SHA-256 digest of ``path``."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_sources_manifest(repo_root: str | Path) -> dict[str, Any]:
    """Build SHA-256 verified manifest of all 14 Burnet & Jowett primary source files.

    Args:
        repo_root: Root directory of ``geometor/plato``.

    Returns:
        JSON-serializable manifest dictionary.
    """
    root = Path(repo_root)
    sources_dir = root / "resources" / "loci_mathematici" / "sources"
    seen_files: set[tuple[str, str]] = set()
    records: list[SourceFileRecord] = []

    for unit in CODEX_UNITS:
        for passage in unit.passages:
            meta = DIALOGUE_METADATA[passage.dialogue_key]
            el_key = ("el", passage.burnet_xml)
            if el_key not in seen_files:
                seen_files.add(el_key)
                el_path = sources_dir / "el" / passage.burnet_xml
                records.append(
                    SourceFileRecord(
                        dialogue_key=passage.dialogue_key,
                        language="el",
                        edition=f"John Burnet, {meta['burnet_vol']} ({meta['tlg_id']})",
                        relative_path=str(el_path.relative_to(root)),
                        size_bytes=el_path.stat().st_size,
                        sha256=_sha256_file(el_path),
                    )
                )
            en_key = ("en", passage.jowett_txt)
            if en_key not in seen_files:
                seen_files.add(en_key)
                en_path = sources_dir / "en" / passage.jowett_txt
                records.append(
                    SourceFileRecord(
                        dialogue_key=passage.dialogue_key,
                        language="en",
                        edition=f"Benjamin Jowett, {meta['jowett_pg']}",
                        relative_path=str(en_path.relative_to(root)),
                        size_bytes=en_path.stat().st_size,
                        sha256=_sha256_file(en_path),
                    )
                )

    return {
        "edition": "GEOMETOR • plato — Loci Mathematici et Geometrici",
        "greek_authority": "John Burnet, Platonis Opera, Vols. I–V (Oxford: Clarendon Press, 1900–1907, Perseus Canonical GreekLit TEI-XML)",
        "english_authority": "Benjamin Jowett, The Dialogues of Plato, 3rd ed., 5 vols. (Oxford: Clarendon Press, 1892, Project Gutenberg public domain)",
        "file_count": len(records),
        "files": [asdict(r) for r in records],
    }


def build_concordance_data() -> dict[str, Any]:
    """Construct the structured cross-corpus Plato Stephanus concordance payload."""
    repo_Declaration_count = sum(len(e.repos) for e in CROSS_CORPUS_PLATO_ENTRIES)
    in_codex_count = sum(1 for e in CROSS_CORPUS_PLATO_ENTRIES if e.in_codex)
    return {
        "edition": "GEOMETOR • plato — Cross-Corpus Stephanus Concordance",
        "sister_repositories": [
            "euclid",
            "elements",
            "proclus",
            "aristotle",
            "hoenen",
            "pacioli",
        ],
        "unique_citation_keys": len(CROSS_CORPUS_PLATO_ENTRIES),
        "repository_level_declarations": repo_Declaration_count,
        "in_codex_keys": in_codex_count,
        "peripheral_catalogued_keys": len(CROSS_CORPUS_PLATO_ENTRIES) - in_codex_count,
        "entries": [
            {
                "cite_key": e.cite_key,
                "repos": list(e.repos),
                "dialogue": e.dialogue,
                "stephanus_locus": e.stephanus_locus,
                "in_codex": e.in_codex,
                "unit_slug": e.unit_slug,
                "stephanus_anchor": e.stephanus_anchor,
                "euclid_proclus_context": e.euclid_proclus_context,
            }
            for e in CROSS_CORPUS_PLATO_ENTRIES
        ],
    }


def render_concordance_rst() -> str:
    """Render ``docsrc/loci_mathematici/concordance.rst`` from canonical concordance data."""
    lines = [
        ":order: 90",
        ":layout: book",
        ":type: apparatus",
        ":title: Master Stephanus Concordance",
        "",
        ".. _concordance:",
        "",
        "============================",
        "Master Stephanus Concordance",
        "============================",
        "",
        ".. rubric:: Cross-Corpus Reconciliation Across Euclid, Elements, Proclus, Aristotle, Hoenen & Pacioli",
        "",
        (
            "This concordance reconciles every ``plato:*`` citation across the six sister "
            "repositories of the GEOMETOR Digital Scriptorium (**36 canonical citation keys** "
            "spanning **58 repository-level declarations** and **63 apparatus files** in "
            "``geometor/euclid``, ``geometor/elements``, ``geometor/proclus``, "
            "``geometor/aristotle``, ``geometor/hoenen``, and ``geometor/pacioli``) directly to "
            "synchronized Stephanus anchors in *Loci Mathematici et Geometrici*."
        ),
        "",
        "Primary Mathematical & Philosophical Loci (Staged Verbatim in Units I–VI)",
        "-------------------------------------------------------------------------",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 22 16 16 18 28",
        "",
        "   * - Sister Citation Key",
        "     - Sister Repos",
        "     - Stephanus Locus",
        "     - Codex Target",
        "     - Mathematical & Noetic Context",
    ]

    for entry in CROSS_CORPUS_PLATO_ENTRIES:
        if not entry.in_codex:
            continue
        repos_str = ", ".join(f"``{r}``" for r in entry.repos)
        target_str = (
            f":ref:`{entry.dialogue} {entry.stephanus_locus} <{entry.stephanus_anchor}>`"
        )
        lines.extend(
            [
                f"   * - ``{entry.cite_key}``",
                f"     - {repos_str}",
                f"     - ``{entry.stephanus_locus}``",
                f"     - {target_str}",
                f"     - {entry.euclid_proclus_context}",
            ]
        )

    lines.extend(
        [
            "",
            "Peripheral Civic & Optical Loci (Catalogued in Critical Notes)",
            "--------------------------------------------------------------",
            "",
            (
                "Six peripheral citations in Heath's philological notes and Hoenen's civic-number "
                "excursus fall outside the mathematical dialogues proper and are analyzed in the "
                "corresponding Critical Notes tracks:"
            ),
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 22 18 18 42",
            "",
            "   * - Sister Citation Key",
            "     - Sister Repos",
            "     - Stephanus Locus",
            "     - Scope & Analytical Note Location",
        ]
    )

    peripheral_docs = {
        "plato:leges:737e-738b": "republic/522c-534e/notes",
        "plato:leges:738a": "republic/522c-534e/notes",
        "plato:rep:417": "republic/522c-534e/notes",
        "plato:laws:777D": "foundations/laws-817e-820d/notes",
        "plato:rep:X.602c": "foundations/philebus-51b-52c/notes",
        "plato:sophist:235.d": "foundations/philebus-51b-52c/notes",
    }

    for entry in CROSS_CORPUS_PLATO_ENTRIES:
        if entry.in_codex:
            continue
        repos_str = ", ".join(f"``{r}``" for r in entry.repos)
        target_doc = peripheral_docs.get(entry.cite_key, f"{entry.unit_slug}/index")
        note_ref = f":doc:`/{target_doc}`"
        lines.extend(
            [
                f"   * - ``{entry.cite_key}``",
                f"     - {repos_str}",
                f"     - ``{entry.dialogue} {entry.stephanus_locus}``",
                f"     - {entry.euclid_proclus_context} ({note_ref})",
            ]
        )

    lines.append("")
    return "\n".join(lines)


def write_concordance_artifacts(repo_root: str | Path) -> dict[str, Path]:
    """Write ``concordance.json``, ``sources_manifest.json``, and ``concordance.rst``."""
    root = Path(repo_root)
    conc_data = build_concordance_data()
    manifest_data = build_sources_manifest(root)
    rst_text = render_concordance_rst()

    out_paths: dict[str, Path] = {}

    for rel in (
        Path("resources/loci_mathematici/concordance.json"),
        Path("resources/concordance.json"),
    ):
        target = root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            json.dumps(conc_data, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        out_paths[str(rel)] = target

    manifest_path = root / "resources" / "loci_mathematici" / "sources_manifest.json"
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(
        json.dumps(manifest_data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    out_paths["resources/loci_mathematici/sources_manifest.json"] = manifest_path

    rst_path = root / "docsrc" / "concordance.rst"
    rst_path.parent.mkdir(parents=True, exist_ok=True)
    rst_path.write_text(rst_text, encoding="utf-8")
    out_paths["docsrc/concordance.rst"] = rst_path

    return out_paths
