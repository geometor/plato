"""Comprehensive test suite for GEOMETOR • plato (`geometor.plato`).

Verifies:
1. 100% exact symbolic SymPy precision (`auto_intersect=False`, zero `sp.Float`) across all
   7 geometric `Model` builders and Rational Trigonometry invariants (quadrances & spreads).
2. Exact rational diatonic arithmetic of the 34-pitch *Timaeus* World-Soul scale
   (24 `9/8` tones, 9 `256/243` *leimmata*, Crantor integer base `384..10368`).
3. Interactive `.euclid-graphic` SVG contract (`<defs>` tick markers, `#elements`,
   `#graphics`, `#highlights`, `#points`, `#labels`, 3-vertex midpoint `<path>` segments,
   and `class="bg"` inline stripping compatibility).
4. SHA-256 verification of all 14 Burnet OCT Greek & Jowett 1892 English primary witnesses.
5. Cross-corpus Stephanus concordance reconciling all 58 `plato:*` repository citations
   across `euclid`, `elements`, `proclus`, `aristotle`, `pacioli`, and `hoenen`, and
   resolving every `in_codex` Stephanus anchor in compiled `docsrc/loci_mathematici/`.
6. Strict Content / Code Separation: zero embedded `code-block:: python` or `py_file`
   directives inside `docsrc/loci_mathematici/`.
7. Sphinx `el` track registration (`geometor.plato.sphinx_ext`) and CLI subcommands.
"""

from __future__ import annotations

import hashlib
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from types import SimpleNamespace

import pytest
import sympy as sp
import sympy.geometry as spg
from geometor.model import Model, quadrance, vertex_spread

from geometor.plato import (
    APOTOME,
    CITATIONS_DATA,
    CODEX_UNITS,
    COMMA_PYTHAGOREAN,
    CRANTOR_INTEGER_MULTIPLIER,
    CROSS_CORPUS_PLATO_ENTRIES,
    EPITRITOS,
    EPOGDOOS,
    GLOSSARY_DATA,
    HEMIOLIOS,
    LEIMMA,
    PERSONS_DATA,
    __version__,
    arithmetic_mean,
    build_concordance_data,
    build_timaeus_scale,
    build_timaeus_skeleton,
    classify_theaetetus_powers,
    construct_compass_and_peras,
    construct_divided_line,
    construct_meno_diagonal_doubling,
    construct_theodorus_spiral,
    construct_timaeus_cube_face,
    construct_timaeus_proportion_circles,
    construct_timaeus_triangles,
    geometric_mean_squared,
    harmonic_mean,
    render_svg_string,
    verify_divided_line_identity,
    verify_timaeus_gamut,
)
from geometor.plato.cli import main as cli_main
from geometor.plato.sphinx_ext import register_greek_track
from geometor.plato.sphinx_ext import setup as sphinx_setup

REPO_ROOT = Path(__file__).resolve().parents[1]


def _assert_exact_model(model: Model) -> None:
    """Assert `auto_intersect is False` and zero `sp.Float` atoms anywhere in `model`."""
    assert model.auto_intersect is False
    assert len(model) > 0
    for elem in model:
        if isinstance(elem, spg.Point2D):
            assert not elem.x.atoms(sp.Float), f"Float found in point {elem}: {elem.x}"
            assert not elem.y.atoms(sp.Float), f"Float found in point {elem}: {elem.y}"
        elif isinstance(elem, spg.Line2D):
            for pt in (elem.p1, elem.p2):
                assert not pt.x.atoms(sp.Float)
                assert not pt.y.atoms(sp.Float)
        elif isinstance(elem, spg.Circle):
            assert not elem.center.x.atoms(sp.Float)
            assert not elem.center.y.atoms(sp.Float)
            assert not elem.radius.atoms(sp.Float)


def test_package_version() -> None:
    """Verify semantic version string."""
    assert __version__ == "0.1.1"


def test_meno_diagonal_doubling_exact() -> None:
    """Verify Meno 82b–85b square quadrances (4, 16, 9, 8) and zero floats."""
    model = construct_meno_diagonal_doubling()
    _assert_exact_model(model)

    pt_a = model.get_element_by_ID("A")
    pt_b = model.get_element_by_ID("B")
    pt_d = model.get_element_by_ID("D")
    pt_e = model.get_element_by_ID("E")
    pt_h = model.get_element_by_ID("H")
    pt_k = model.get_element_by_ID("K")
    pt_m = model.get_element_by_ID("M")

    assert quadrance(pt_a, pt_b) == 4
    assert quadrance(pt_a, pt_e) == 16
    assert quadrance(pt_a, pt_m) == 9
    assert quadrance(pt_b, pt_d) == 8
    assert quadrance(pt_b, pt_h) == 8
    assert quadrance(pt_h, pt_k) == 8
    assert quadrance(pt_k, pt_d) == 8


def test_theaetetus_powers_and_theodorus_spiral() -> None:
    """Verify Theaetetus 147c–148b classification and Theodorus spiral Q(O, Pn) = n for 1..17."""
    entries = classify_theaetetus_powers(17)
    assert len(entries) == 17
    meke = [e.area_n for e in entries if "mekos" in e.line_kind]
    dynameis = [e.area_n for e in entries if "dynamis" in e.line_kind]
    assert meke == [1, 4, 9, 16]
    assert dynameis == [2, 3, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 17]

    with pytest.raises(ValueError, match="max_n must be >= 1"):
        classify_theaetetus_powers(0)

    spiral = construct_theodorus_spiral(max_n=17)
    _assert_exact_model(spiral)

    origin = spiral.get_element_by_ID("O")
    prev_pt = spiral.get_element_by_ID("P1")
    assert sp.expand(origin.x**2 + origin.y**2) == 0
    assert sp.expand(prev_pt.x**2 + prev_pt.y**2) == 1

    for n in range(2, 18):
        curr_pt = spiral.get_element_by_ID(f"P{n}")
        q_spoke = sp.expand(curr_pt.x**2 + curr_pt.y**2)
        q_step = sp.expand((curr_pt.x - prev_pt.x) ** 2 + (curr_pt.y - prev_pt.y) ** 2)
        dot_orth = sp.expand(prev_pt.x * (curr_pt.x - prev_pt.x) + prev_pt.y * (curr_pt.y - prev_pt.y))
        assert q_spoke == n
        assert q_step == 1
        assert dot_orth == 0
        prev_pt = curr_pt


def test_republic_divided_line_exact() -> None:
    """Verify Republic VI 509d–511e symbolic identity and golden-ratio semicircle construction."""
    ident = verify_divided_line_identity()
    assert ident["middle_segments_equal"] is True
    assert ident["middle_is_geometric_mean"] is True

    with pytest.raises(ValueError, match="prohibited"):
        construct_divided_line(ratio=sp.Float(1.618))

    model = construct_divided_line()
    _assert_exact_model(model)

    pt_a = model.get_element_by_ID("A")
    pt_b = model.get_element_by_ID("B")
    pt_c = model.get_element_by_ID("C")
    pt_d = model.get_element_by_ID("D")
    pt_e = model.get_element_by_ID("E")
    pt_g = model.get_element_by_ID("G")

    assert quadrance(pt_a, pt_b) == 1
    assert sp.simplify(quadrance(pt_b, pt_c) - quadrance(pt_c, pt_d)) == 0
    assert sp.simplify(quadrance(pt_b, pt_g) - quadrance(pt_b, pt_c)) == 0
    # Under phi, DE == AC
    assert sp.simplify(quadrance(pt_a, pt_c) - quadrance(pt_d, pt_e)) == 0


def test_timaeus_harmonics_and_semicircle() -> None:
    """Verify Timaeus 31b–36d means, 34-pitch World-Soul gamut, and semicircle construction."""
    assert arithmetic_mean(2, 4) == 3
    assert harmonic_mean(2, 4) == sp.Rational(8, 3)
    assert geometric_mean_squared(2, 4) == 8
    assert arithmetic_mean(2, 4) / harmonic_mean(2, 4) == EPOGDOOS
    assert EPITRITOS / (EPOGDOOS**2) == LEIMMA
    assert EPOGDOOS / LEIMMA == APOTOME
    assert APOTOME / LEIMMA == COMMA_PYTHAGOREAN
    assert HEMIOLIOS / EPITRITOS == EPOGDOOS

    skeleton = build_timaeus_skeleton()
    assert skeleton[0] == 1
    assert skeleton[-1] == 27

    scale = build_timaeus_scale()
    assert len(scale) == 34
    assert scale[0].ratio == 1
    assert scale[-1].ratio == 27
    assert scale[0].crantor_integer == CRANTOR_INTEGER_MULTIPLIER == 384
    assert scale[-1].crantor_integer == 10368

    summary = verify_timaeus_gamut()
    assert summary["pitch_count"] == 34
    assert summary["tone_count"] == 24
    assert summary["leimma_count"] == 9
    assert summary["total_span"] == 27
    assert summary["all_steps_diatonic"] is True
    assert sp.simplify(EPOGDOOS**24 * LEIMMA**9 - 27) == 0

    model = construct_timaeus_proportion_circles()
    _assert_exact_model(model)
    pt_o = model.get_element_by_ID("O")
    pt_j = model.get_element_by_ID("J")
    pt_g = model.get_element_by_ID("G")
    pt_h = model.get_element_by_ID("H")
    assert quadrance(pt_o, pt_g) == 9
    assert quadrance(pt_j, pt_g) == 8
    assert quadrance(pt_g, pt_h) == sp.Rational(64, 9)
    assert quadrance(pt_o, pt_g) / quadrance(pt_g, pt_h) == EPOGDOOS**2


def test_timaeus_elementary_triangles_and_cube_face() -> None:
    """Verify Timaeus 53c–56c scalene (1,3,4; spreads 1/4,3/4,1) and isosceles (1,1,2) models."""
    tri = construct_timaeus_triangles()
    _assert_exact_model(tri)
    pt_g = tri.get_element_by_ID("G")
    pt_m1 = tri.get_element_by_ID("M1")
    pt_a = tri.get_element_by_ID("A")
    pt_b = tri.get_element_by_ID("B")
    pt_c = tri.get_element_by_ID("C")

    assert (quadrance(pt_g, pt_m1), quadrance(pt_m1, pt_c), quadrance(pt_g, pt_c)) == (1, 3, 4)
    assert vertex_spread(pt_g, pt_c, pt_m1) == sp.Rational(1, 4)
    assert vertex_spread(pt_m1, pt_g, pt_c) == sp.Rational(3, 4)
    assert vertex_spread(pt_g, pt_m1, pt_c) == 1
    assert quadrance(pt_a, pt_b) == quadrance(pt_b, pt_c) == quadrance(pt_c, pt_a) == 12

    cube = construct_timaeus_cube_face()
    _assert_exact_model(cube)
    co = cube.get_element_by_ID("O")
    ca = cube.get_element_by_ID("A")
    cb = cube.get_element_by_ID("B")
    assert (quadrance(co, ca), quadrance(co, cb), quadrance(ca, cb)) == (1, 1, 2)
    assert vertex_spread(ca, co, cb) == 1
    assert vertex_spread(co, ca, cb) == sp.Rational(1, 2)


def test_foundations_compass_and_peras() -> None:
    """Verify Parmenides 137e, Philebus 51c, and Laws VII 819d–820d (1, sqrt(2), sqrt(3))."""
    model = construct_compass_and_peras()
    _assert_exact_model(model)
    pt_o = model.get_element_by_ID("O")
    pt_c = model.get_element_by_ID("C")
    pt_d = model.get_element_by_ID("D")
    pt_e = model.get_element_by_ID("E")
    assert (quadrance(pt_o, pt_c), quadrance(pt_o, pt_d), quadrance(pt_o, pt_e)) == (1, 2, 3)


def test_euclid_graphic_svg_contract() -> None:
    """Verify interactive `.euclid-graphic` SVG layer and 3-vertex path contract on all 6 figures."""
    figs_dir = REPO_ROOT / "docsrc" / "_static" / "figures"
    expected_figures = [
        ("meno_diagonal_doubling", "meno-diag"),
        ("theodorus_spiral", "theodorus-spiral"),
        ("republic_divided_line", "divided-line"),
        ("timaeus_world_soul", "timaeus-means"),
        ("timaeus_triangles", "timaeus-triangles"),
        ("foundations_peras_compass", "foundations-peras"),
    ]
    ns = {"svg": "http://www.w3.org/2000/svg"}

    for slug, graphic_id in expected_figures:
        svg_path = figs_dir / f"{slug}.svg"
        assert svg_path.is_file(), f"Missing exported SVG {svg_path}"
        raw = svg_path.read_text(encoding="utf-8")
        assert 'class="euclid-graphic"' in raw
        assert f'data-graphic-id="{graphic_id}"' in raw
        assert 'class="bg"' in raw

        root = ET.fromstring(raw)
        marker_ids = {m.attrib.get("id") for m in root.findall(".//svg:defs/svg:marker", ns)}
        assert {"geom-tick-1", "geom-tick-2", "geom-tick-3"}.issubset(marker_ids)

        group_ids = {g.attrib.get("id") for g in root.findall(".//svg:g", ns) if "id" in g.attrib}
        assert {"elements", "graphics", "highlights", "points", "labels"}.issubset(group_ids)

        line_paths = root.findall(".//svg:g[@id='graphics']/svg:path", ns)
        assert len(line_paths) > 0
        for p in line_paths:
            d_attr = p.attrib.get("d", "")
            assert re.match(r"^M\s+\S+\s+\S+\s+L\s+\S+\s+\S+\s+L\s+\S+\s+\S+$", d_attr), (
                f"Line path in {slug} does not use 3-vertex midpoint geometry: {d_attr}"
            )

    # Also test direct string rendering
    direct_svg = render_svg_string(construct_compass_and_peras(), graphic_id="test_peras")
    assert 'data-graphic-id="test_peras"' in direct_svg


def test_sources_manifest_sha256_integrity() -> None:
    """Verify all 14 Burnet OCT XML and Jowett TXT primary witnesses match SHA-256 digests."""
    manifest_path = REPO_ROOT / "resources" / "loci_mathematici" / "sources_manifest.json"
    assert manifest_path.is_file()
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = manifest["files"]
    assert manifest["file_count"] == len(sources) == 14

    langs = {entry["language"] for entry in sources}
    assert langs == {"el", "en"}

    for entry in sources:
        fpath = REPO_ROOT / entry["relative_path"]
        assert fpath.is_file(), f"Missing primary source {fpath}"
        data = fpath.read_bytes()
        assert len(data) == entry["size_bytes"] > 10_000
        digest = hashlib.sha256(data).hexdigest()
        assert digest == entry["sha256"]


def test_concordance_apparatus_and_codex_purity() -> None:
    """Verify 58 cross-corpus citations, Stephanus anchor resolution, and zero embedded Python in Codex."""
    assert len(CODEX_UNITS) == 6
    assert len(GLOSSARY_DATA) >= 30
    assert len(PERSONS_DATA) >= 20
    assert len(CITATIONS_DATA) >= 25

    # Verify mirrored JSON registries exist in both resources/ and resources/loci_mathematici/
    for rel_dir in (REPO_ROOT / "resources", REPO_ROOT / "resources" / "loci_mathematici"):
        for fname in ("concordance.json", "glossary.json", "persons.json", "citations.json"):
            fpath = rel_dir / fname
            assert fpath.is_file(), f"Missing apparatus JSON {fpath}"
            parsed = json.loads(fpath.read_text(encoding="utf-8"))
            assert len(parsed) > 0

    conc = build_concordance_data()
    entries = conc["entries"]
    assert len(entries) == len(CROSS_CORPUS_PLATO_ENTRIES) == 36
    assert conc["repository_level_declarations"] == 58

    total_repo_refs = sum(len(item["repos"]) for item in entries)
    assert total_repo_refs == 58

    all_repos = {repo for item in entries for repo in item["repos"]}
    assert all_repos == {"euclid", "elements", "proclus", "aristotle", "pacioli", "hoenen"}

    # Collect all Stephanus labels across compiled Codex units and verify zero Python scripts in Codex
    codex_dir = REPO_ROOT / "docsrc" / "loci_mathematici"
    defined_labels: set[str] = set()
    rst_files = sorted(codex_dir.rglob("*.rst"))
    assert len(rst_files) >= 29  # index + 4 apparatus + 6*4 unit tracks

    for rst_path in rst_files:
        content = rst_path.read_text(encoding="utf-8")
        assert ".. code-block:: python" not in content, f"Forbidden Python block in {rst_path}"
        assert ":py_file:" not in content, f"Forbidden py_file in {rst_path}"
        for match in re.finditer(r"^\.\.\s+_([A-Za-z0-9_.-]+):", content, flags=re.MULTILINE):
            defined_labels.add(match.group(1))

    # Every in_codex entry's stephanus_anchor must exist in the compiled Codex
    in_codex_entries = [e for e in entries if e["in_codex"]]
    assert len(in_codex_entries) == 30
    for entry in in_codex_entries:
        anchor = entry["stephanus_anchor"]
        assert anchor in defined_labels, (
            f"Concordance entry {entry['cite_key']} anchor {anchor!r} missing from Codex labels"
        )


def test_sphinx_ext_and_cli(capsys: pytest.CaptureFixture[str]) -> None:
    """Verify `geometor.plato.sphinx_ext` Greek track registration and `geometor-plato` CLI."""
    mock_book = SimpleNamespace(
        _TRACK_SUFFIX_PATTERNS=[
            (r"^(.+)[._-]en$", "en", "English"),
            (r"^(.+)[._-]summary$", "summary", "Summary"),
            (r"^(.+)[._-]notes$", "notes", "Critical Notes"),
        ],
        _AUX_TRACK_BASENAMES={"summary", "notes"},
        _AUX_TRACK_PATTERNS=[],
        _extract_unit_stem=lambda base, _d: re.sub(r"-(en|el|summary|notes)$", "", base),
        detect_companion_tracks=lambda _env, pagename: [
            {"key": "en", "label": "English", "docname": "loci_mathematici/meno/meno-en", "active": pagename.endswith("-en")},
            {"key": "summary", "label": "Summary", "docname": "loci_mathematici/meno/meno-summary", "active": pagename.endswith("-summary")},
            {"key": "notes", "label": "Critical Notes", "docname": "loci_mathematici/meno/meno-notes", "active": pagename.endswith("-notes")},
        ],
    )
    assert register_greek_track(mock_book) is True
    env = SimpleNamespace(
        found_docs={
            "loci_mathematici/meno/meno-en",
            "loci_mathematici/meno/meno-el",
            "loci_mathematici/meno/meno-summary",
            "loci_mathematici/meno/meno-notes",
        }
    )
    tracks = mock_book.detect_companion_tracks(env, "loci_mathematici/meno/meno-en")
    assert [t["key"] for t in tracks] == ["en", "el", "summary", "notes"]
    assert tracks[1]["label"] == "Greek (Burnet OCT)"

    meta = sphinx_setup(SimpleNamespace())
    assert meta["parallel_read_safe"] is True

    assert cli_main(["scale"]) == 0
    assert cli_main(["concordance"]) == 0
    assert cli_main(["verify"]) == 0
    out = capsys.readouterr().out
    assert "384" in out
    assert "10368" in out
