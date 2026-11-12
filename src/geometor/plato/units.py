"""Canonical unit and Stephanus passage definitions for *Loci Mathematici et Geometrici*."""

from __future__ import annotations

from dataclasses import dataclass

__all__ = [
    "CODEX_UNITS",
    "CODEX_UNITS_BY_SLUG",
    "DIALOGUE_METADATA",
    "CodexUnitSpec",
    "PassageSpec",
]


@dataclass(frozen=True)
class PassageSpec:
    """Exact primary-source passage specification within a Platonic dialogue.

    Attributes:
        passage_id: Short stable identifier (e.g., ``"meno-81e-85d"``).
        dialogue_key: Canonical dialogue slug (``"meno"``, ``"theaetetus"``, ``"republic"``,
            ``"timaeus"``, ``"parmenides"``, ``"philebus"``, ``"laws"``).
        dialogue_title_en: English title of the dialogue.
        dialogue_title_el: Greek title of the dialogue.
        heading: Scholarly section heading for this passage.
        stephanus_range: Human-readable Stephanus citation span (e.g., ``"81e–85d"``).
        start_stephanus: Inclusive starting Burnet ``<milestone unit="section">`` key (lowercase).
        end_stephanus: Inclusive ending Burnet ``<milestone unit="section">`` key (lowercase).
        burnet_xml: Filename in ``resources/loci_mathematici/sources/el/``.
        jowett_txt: Filename in ``resources/loci_mathematici/sources/en/``.
        jowett_start_line: 1-based start line in ``jowett_txt`` (``0`` when using Republic inline markers).
        jowett_end_line: 1-based inclusive end line in ``jowett_txt`` (``0`` when using Republic inline markers).
        republic_start_marker: Optional inline marker in PG #55201 (e.g., ``"509D"``).
        republic_end_marker: Optional exclusive stop marker in PG #55201 (e.g., ``"BOOK VII"`` or ``"535A"``).
    """

    passage_id: str
    dialogue_key: str
    dialogue_title_en: str
    dialogue_title_el: str
    heading: str
    stephanus_range: str
    start_stephanus: str
    end_stephanus: str
    burnet_xml: str
    jowett_txt: str
    jowett_start_line: int = 0
    jowett_end_line: int = 0
    republic_start_marker: str = ""
    republic_end_marker: str = ""


@dataclass(frozen=True)
class CodexUnitSpec:
    """Canonical unit in the 4-track Book Codex (``docsrc/loci_mathematici/``)."""

    slug: str
    unit_number: str
    title: str
    subtitle: str
    stephanus_summary: str
    figure_svg: str
    figure_caption: str
    demo_doc: str
    passages: tuple[PassageSpec, ...]


DIALOGUE_METADATA: dict[str, dict[str, str]] = {
    "meno": {
        "title_en": "Meno",
        "title_el": "Μένων",
        "tlg_id": "tlg0059.tlg024",
        "burnet_vol": "Platonis Opera, Tomus III (Oxford, 1903)",
        "jowett_pg": "Project Gutenberg #1643 (Jowett 3rd ed., 1892)",
    },
    "theaetetus": {
        "title_en": "Theaetetus",
        "title_el": "Θεαίτητος",
        "tlg_id": "tlg0059.tlg006",
        "burnet_vol": "Platonis Opera, Tomus I (Oxford, 1900; 2nd ed. 1905)",
        "jowett_pg": "Project Gutenberg #1726 (Jowett 3rd ed., 1892)",
    },
    "republic": {
        "title_en": "Republic",
        "title_el": "Πολιτεία",
        "tlg_id": "tlg0059.tlg030",
        "burnet_vol": "Platonis Opera, Tomus IV (Oxford, 1902/1905)",
        "jowett_pg": "Project Gutenberg #55201 (Jowett 3rd ed., 1892, with Stephanus pagination)",
    },
    "timaeus": {
        "title_en": "Timaeus",
        "title_el": "Τίμαιος",
        "tlg_id": "tlg0059.tlg031",
        "burnet_vol": "Platonis Opera, Tomus IV (Oxford, 1902/1905)",
        "jowett_pg": "Project Gutenberg #1572 (Jowett 3rd ed., 1892)",
    },
    "parmenides": {
        "title_en": "Parmenides",
        "title_el": "Παρμενίδης",
        "tlg_id": "tlg0059.tlg009",
        "burnet_vol": "Platonis Opera, Tomus II (Oxford, 1901; 2nd ed. 1910)",
        "jowett_pg": "Project Gutenberg #1687 (Jowett 3rd ed., 1892)",
    },
    "philebus": {
        "title_en": "Philebus",
        "title_el": "Φίληβος",
        "tlg_id": "tlg0059.tlg010",
        "burnet_vol": "Platonis Opera, Tomus II (Oxford, 1901; 2nd ed. 1910)",
        "jowett_pg": "Project Gutenberg #1744 (Jowett 3rd ed., 1892)",
    },
    "laws": {
        "title_en": "Laws",
        "title_el": "Νόμοι",
        "tlg_id": "tlg0059.tlg034",
        "burnet_vol": "Platonis Opera, Tomus V (Oxford, 1907)",
        "jowett_pg": "Project Gutenberg #1750 (Jowett 3rd ed., 1892)",
    },
}


CODEX_UNITS: tuple[CodexUnitSpec, ...] = (
    CodexUnitSpec(
        slug="meno",
        unit_number="Unit I",
        title="Meno: Definition of Figure, Doubling the Square & Geometric Hypothesis",
        subtitle=(
            "Figure as the Limit of Solid (75d–76a), Anamnesis & the Diagonal Square "
            "Q = 4 + 4 = 8 (81e–85d), and Inquiry from Hypothesis (86e–87b)"
        ),
        stephanus_summary="Meno 75d–76a, 81e–85d, 86e–87b",
        figure_svg="meno_diagonal_doubling.svg",
        figure_caption=(
            "Socrates' Geometric Demonstration in Meno 82b–85b: the 2×2 given square "
            "< A B C D > (Q = 4), the 4×4 fourfold square < A E F G > (Q = 16), the "
            "3×3 nine-foot trial < A M N P > (Q = 9), and the inscribed diagonal square "
            "< B H K D > (Q = 8)."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="meno-75d-76a",
                dialogue_key="meno",
                dialogue_title_en="Meno",
                dialogue_title_el="Μένων",
                heading="I.1 Dialectical Definition: Figure as the Limit of Solid (75d–76a)",
                stephanus_range="75d–76a",
                start_stephanus="75d",
                end_stephanus="76a",
                burnet_xml="tlg0059.tlg024.burnet_oct.xml",
                jowett_txt="meno_jowett_pg1643.txt",
                jowett_start_line=1190,
                jowett_end_line=1217,
            ),
            PassageSpec(
                passage_id="meno-81e-85d",
                dialogue_key="meno",
                dialogue_title_en="Meno",
                dialogue_title_el="Μένων",
                heading="I.2 Anamnesis & Doubling the Square by the Diagonal (81e–85d)",
                stephanus_range="81e–85d",
                start_stephanus="81e",
                end_stephanus="85d",
                burnet_xml="tlg0059.tlg024.burnet_oct.xml",
                jowett_txt="meno_jowett_pg1643.txt",
                jowett_start_line=1563,
                jowett_end_line=1961,
            ),
            PassageSpec(
                passage_id="meno-86e-87b",
                dialogue_key="meno",
                dialogue_title_en="Meno",
                dialogue_title_el="Μένων",
                heading="I.3 The Geometer's Method of Hypothesis & Application of Area (86e–87b)",
                stephanus_range="86e–87b",
                start_stephanus="86e",
                end_stephanus="87b",
                burnet_xml="tlg0059.tlg024.burnet_oct.xml",
                jowett_txt="meno_jowett_pg1643.txt",
                jowett_start_line=1984,
                jowett_end_line=2018,
            ),
        ),
    ),
    CodexUnitSpec(
        slug="theaetetus",
        unit_number="Unit II",
        title="Theaetetus: Theodorus's Radical Constructions & Classification of Powers",
        subtitle=(
            "Incommensurable Square Sides from Three to Seventeen Square Feet & "
            "Theaetetus's Dichotomy of Lengths (Mēkē) and Powers (Dynameis) (147c–148b)"
        ),
        stephanus_summary="Theaetetus 147c–148b",
        figure_svg="theodorus_spiral.svg",
        figure_caption=(
            "Theodorus's Right-Triangle Radical Chain (Theaetetus 147d–148b): pure "
            "compass-and-straightedge construction of exact quadrances Q(O, Pn) = n "
            "for 1 <= n <= 17, highlighting rational lengths (P1, P4, P9, P16) vs. "
            "quadratic powers (dynameis)."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="theaetetus-147c-148b",
                dialogue_key="theaetetus",
                dialogue_title_en="Theaetetus",
                dialogue_title_el="Θεαίτητος",
                heading="II.1 Theodorus's Diagram & Lengths vs. Powers (147c–148b)",
                stephanus_range="147c–148b",
                start_stephanus="147c",
                end_stephanus="148b",
                burnet_xml="tlg0059.tlg006.burnet_oct.xml",
                jowett_txt="theaetetus_jowett_pg1726.txt",
                jowett_start_line=3443,
                jowett_end_line=3493,
            ),
        ),
    ),
    CodexUnitSpec(
        slug="republic",
        unit_number="Unit III",
        title="Republic VI–VII: The Divided Line, Dianoia & the Quadrivium",
        subtitle=(
            "Proportional Section of the Visible and Intelligible Realms (509d–511e) & "
            "Arithmetic, Plane Geometry, Solid Geometry, Astronomy, Harmonics, and Dialectic (525a–534e)"
        ),
        stephanus_summary="Republic VI 509d–511e; VII 525a–534e",
        figure_svg="republic_divided_line.svg",
        figure_caption=(
            "The Divided Line of Republic VI 509d–511e: cutting [A, E] at C and each "
            "realm in the same ratio 1 : r proves identically that sensible Pistis "
            "(/ B C /) equals mathematical Dianoia (/ C D /) as geometric mean ordinate "
            "B G between Eikasia (/ A B /) and Noesis (/ D E /)."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="republic-509d-511e",
                dialogue_key="republic",
                dialogue_title_en="Republic Book VI",
                dialogue_title_el="Πολιτεία Ϛʹ",
                heading="III.1 The Divided Line, Geometric Hypotheses & Dianoia vs. Noēsis (509d–511e)",
                stephanus_range="VI, 509d–511e",
                start_stephanus="509d",
                end_stephanus="511e",
                burnet_xml="tlg0059.tlg030.burnet_oct.xml",
                jowett_txt="republic_jowett_pg55201.txt",
                jowett_start_line=19822,
                jowett_end_line=19953,
                republic_start_marker="509D",
                republic_end_marker="BOOK VII",
            ),
            PassageSpec(
                passage_id="republic-525a-534e",
                dialogue_key="republic",
                dialogue_title_en="Republic Book VII",
                dialogue_title_el="Πολιτεία Ζʹ",
                heading="III.2 The Five Mathematical Sciences of the Quadrivium & Dialectic (525a–534e)",
                stephanus_range="VII, 525a–534e",
                start_stephanus="525a",
                end_stephanus="534e",
                burnet_xml="tlg0059.tlg030.burnet_oct.xml",
                jowett_txt="republic_jowett_pg55201.txt",
                jowett_start_line=20614,
                jowett_end_line=21226,
                republic_start_marker="525A",
                republic_end_marker="535A",
            ),
        ),
    ),
    CodexUnitSpec(
        slug="timaeus-world-soul",
        unit_number="Unit IV",
        title="Timaeus: Geometric Proportion & Harmonic Division of the World-Soul",
        subtitle=(
            "Single and Double Geometric Means Between Plane and Solid Numbers (31b–32c), "
            "Arithmetic & Harmonic Means, the 9:8 Tone, the 256:243 Leimma, and the Circles of Same & Different (35a–36d)"
        ),
        stephanus_summary="Timaeus 31b–36d",
        figure_svg="timaeus_world_soul.svg",
        figure_caption=(
            "The Three Platonic Means & Circles of the World-Soul (Timaeus 31c–36d): "
            "on octave diameter A J B (2 + 4 = 6), radius O G = 3 is the arithmetic "
            "mean, ordinate J G = 2*sqrt(2) is the geometric mean, projection G H = 8/3 "
            "is the harmonic mean (giving O G / G H = 9/8), and axis [P, Q] crosses at O like Chi (X)."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="timaeus-31b-36d",
                dialogue_key="timaeus",
                dialogue_title_en="Timaeus",
                dialogue_title_el="Τίμαιος",
                heading="IV.1 Cosmic Analogia, Means & Harmonic Scale of the World-Soul (31b–36d)",
                stephanus_range="31b–36d",
                start_stephanus="31b",
                end_stephanus="36d",
                burnet_xml="tlg0059.tlg031.burnet_oct.xml",
                jowett_txt="timaeus_jowett_pg1572.txt",
                jowett_start_line=4548,
                jowett_end_line=4707,
            ),
        ),
    ),
    CodexUnitSpec(
        slug="timaeus-polyhedra",
        unit_number="Unit V",
        title="Timaeus: Elementary Right Triangles & Construction of the Cosmic Polyhedra",
        subtitle=(
            "The Isosceles (1:1:sqrt(2)) and Fairest Scalene (1:sqrt(3):2) Half-Triangles, "
            "Six-Triangle Equilateral Assembly, and the Five Regular Cosmic Solids (53c–56c)"
        ),
        stephanus_summary="Timaeus 53c–56c",
        figure_svg="timaeus_triangles.svg",
        figure_caption=(
            "Cosmic Equilateral Face Assembly (Timaeus 54d–55a): six elementary "
            "1 : sqrt(3) : 2 right-angled scalene triangles (quadrances 1, 3, 4; "
            "spreads 1/4, 3/4, 1) meet thrice along their diagonals and altitudes at "
            "centroid G = X(2) to compose equilateral face < A B C >."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="timaeus-53c-56c",
                dialogue_key="timaeus",
                dialogue_title_en="Timaeus",
                dialogue_title_el="Τίμαιος",
                heading="V.1 Stereometric Principles, Elementary Triangles & Cosmic Solids (53c–56c)",
                stephanus_range="53c–56c",
                start_stephanus="53c",
                end_stephanus="56c",
                burnet_xml="tlg0059.tlg031.burnet_oct.xml",
                jowett_txt="timaeus_jowett_pg1572.txt",
                jowett_start_line=5398,
                jowett_end_line=5525,
            ),
        ),
    ),
    CodexUnitSpec(
        slug="foundations",
        unit_number="Unit VI",
        title="Parmenides, Philebus & Laws VII: Straightness, Limit & Incommensurability",
        subtitle=(
            "Optical Straightness & Equidistant Roundness (Parm. 137d–138a, 145a–b), "
            "Limit & Pure Geometric Beauty by Compass & Rule (Phil. 16c–26d, 51b–52c), "
            "and Dimensional Incommensurability (Laws VII 817e–820d)"
        ),
        stephanus_summary="Parmenides 137d–138a, 145a–b; Philebus 16c–26d, 51b–52c; Laws VII 817e–820d",
        figure_svg="foundations_peras_compass.svg",
        figure_caption=(
            "Compass (Tornos), Optical Straight Ray (Kanon) & Three-Dimensional "
            "Incommensurability: circle (O, C) of equal radii Q = 1 (Parm. 137e, "
            "Phil. 51c), optical diameter [A, O, C], plane diagonal O D (Q = 2), and "
            "unfolded cube diagonal O E (Q = 3, Laws VII 819d–820c)."
        ),
        demo_doc="/demos/index",
        passages=(
            PassageSpec(
                passage_id="parmenides-137d-138a",
                dialogue_key="parmenides",
                dialogue_title_en="Parmenides",
                dialogue_title_el="Παρμενίδης",
                heading="VI.1 Round Equidistance & Optical Straightness: First Hypothesis (Parm. 137d–138a)",
                stephanus_range="137d–138a",
                start_stephanus="137d",
                end_stephanus="138a",
                burnet_xml="tlg0059.tlg009.burnet_oct.xml",
                jowett_txt="parmenides_jowett_pg1687.txt",
                jowett_start_line=2186,
                jowett_end_line=2221,
            ),
            PassageSpec(
                passage_id="parmenides-145a-b",
                dialogue_key="parmenides",
                dialogue_title_en="Parmenides",
                dialogue_title_el="Παρμενίδης",
                heading="VI.2 Beginning, Middle, Extremes & Figure: Second Hypothesis (Parm. 145a–b)",
                stephanus_range="145a–b",
                start_stephanus="145a",
                end_stephanus="145b",
                burnet_xml="tlg0059.tlg009.burnet_oct.xml",
                jowett_txt="parmenides_jowett_pg1687.txt",
                jowett_start_line=2922,
                jowett_end_line=2959,
            ),
            PassageSpec(
                passage_id="philebus-16c-26d",
                dialogue_key="philebus",
                dialogue_title_en="Philebus",
                dialogue_title_el="Φίληβος",
                heading="VI.3 Limit (Peras), the Unlimited (Apeiron) & Mathematical Measure (Phil. 16c–26d)",
                stephanus_range="16c–26d",
                start_stephanus="16c",
                end_stephanus="26d",
                burnet_xml="tlg0059.tlg010.burnet_oct.xml",
                jowett_txt="philebus_jowett_pg1744.txt",
                jowett_start_line=2326,
                jowett_end_line=2990,
            ),
            PassageSpec(
                passage_id="philebus-51b-52c",
                dialogue_key="philebus",
                dialogue_title_en="Philebus",
                dialogue_title_el="Φίληβος",
                heading="VI.4 Pure Geometric Beauty Constructed by Compass, Rule & Square (Phil. 51b–52c)",
                stephanus_range="51b–52c",
                start_stephanus="51b",
                end_stephanus="52c",
                burnet_xml="tlg0059.tlg010.burnet_oct.xml",
                jowett_txt="philebus_jowett_pg1744.txt",
                jowett_start_line=4673,
                jowett_end_line=4740,
            ),
            PassageSpec(
                passage_id="laws-817e-820d",
                dialogue_key="laws",
                dialogue_title_en="Laws Book VII",
                dialogue_title_el="Νόμοι Ζʹ",
                heading="VI.5 Commensurable & Incommensurable Lengths, Breadths, and Depths (Laws VII 817e–820d)",
                stephanus_range="VII, 817e–820d",
                start_stephanus="817e",
                end_stephanus="820d",
                burnet_xml="tlg0059.tlg034.burnet_oct.xml",
                jowett_txt="laws_jowett_pg1750.txt",
                jowett_start_line=16375,
                jowett_end_line=16528,
            ),
        ),
    ),
)

CODEX_UNITS_BY_SLUG: dict[str, CodexUnitSpec] = {u.slug: u for u in CODEX_UNITS}
