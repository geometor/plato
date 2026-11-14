"""GEOMETOR • plato — Exact Symbolic Models & 4-Track Stephanus Book Codex.

Provides:

- Exact SymPy ``geometor.model`` constructions for Plato's mathematical dialogues
  (*Meno*, *Theaetetus*, *Republic* VI–VII, *Timaeus*, *Parmenides*, *Philebus*, *Laws* VII).
- Exact rational diatonic & proportional verification of the *Timaeus* World-Soul gamut.
- Interactive ``.euclid-graphic`` SVG plate export for light/dark Book Codices.
- Deterministic 4-track Stephanus Book Codex compilation from John Burnet's Oxford
  Classical Text TEI-XML and Benjamin Jowett's 1892 English translations.
"""

from __future__ import annotations

from geometor.plato.apparatus import (
    CITATIONS_DATA,
    GLOSSARY_DATA,
    PERSONS_DATA,
    write_apparatus_artifacts,
)
from geometor.plato.compile_codex import (
    compile_all_codex,
    extract_burnet_passage,
    extract_jowett_passage,
)
from geometor.plato.concordance import (
    CROSS_CORPUS_PLATO_ENTRIES,
    ConcordanceEntry,
    build_concordance_data,
    build_sources_manifest,
    write_concordance_artifacts,
)
from geometor.plato.constructions import (
    TheaetetusPowerEntry,
    classify_theaetetus_powers,
    construct_compass_and_peras,
    construct_divided_line,
    construct_meno_diagonal_doubling,
    construct_theodorus_spiral,
    construct_timaeus_cube_face,
    construct_timaeus_proportion_circles,
    construct_timaeus_triangles,
    verify_divided_line_identity,
)
from geometor.plato.harmonics import (
    APOTOME,
    COMMA_PYTHAGOREAN,
    CRANTOR_INTEGER_MULTIPLIER,
    EPITRITOS,
    EPOGDOOS,
    HEMIOLIOS,
    LEIMMA,
    TimaeusPitch,
    arithmetic_mean,
    build_timaeus_scale,
    build_timaeus_skeleton,
    geometric_mean_squared,
    harmonic_mean,
    verify_timaeus_gamut,
)
from geometor.plato.render import (
    export_all_codex_figures,
    export_svg,
    render_svg_string,
)
from geometor.plato.units import (
    CODEX_UNITS,
    CODEX_UNITS_BY_SLUG,
    DIALOGUE_METADATA,
    CodexUnitSpec,
    PassageSpec,
)

__version__ = "0.1.2"

__all__ = [
    "APOTOME",
    "CITATIONS_DATA",
    "CODEX_UNITS",
    "CODEX_UNITS_BY_SLUG",
    "COMMA_PYTHAGOREAN",
    "CRANTOR_INTEGER_MULTIPLIER",
    "CROSS_CORPUS_PLATO_ENTRIES",
    "CodexUnitSpec",
    "ConcordanceEntry",
    "DIALOGUE_METADATA",
    "EPITRITOS",
    "EPOGDOOS",
    "GLOSSARY_DATA",
    "HEMIOLIOS",
    "LEIMMA",
    "PERSONS_DATA",
    "PassageSpec",
    "TheaetetusPowerEntry",
    "TimaeusPitch",
    "__version__",
    "arithmetic_mean",
    "build_concordance_data",
    "build_sources_manifest",
    "build_timaeus_scale",
    "build_timaeus_skeleton",
    "classify_theaetetus_powers",
    "compile_all_codex",
    "construct_compass_and_peras",
    "construct_divided_line",
    "construct_meno_diagonal_doubling",
    "construct_theodorus_spiral",
    "construct_timaeus_cube_face",
    "construct_timaeus_proportion_circles",
    "construct_timaeus_triangles",
    "export_all_codex_figures",
    "export_svg",
    "extract_burnet_passage",
    "extract_jowett_passage",
    "geometric_mean_squared",
    "harmonic_mean",
    "render_svg_string",
    "verify_divided_line_identity",
    "verify_timaeus_gamut",
    "write_apparatus_artifacts",
    "write_concordance_artifacts",
]
