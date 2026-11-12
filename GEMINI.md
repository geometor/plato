# GEOMETOR • plato

Scholarly 4-track Bilingual Book Codex (*Loci Mathematici et Geometrici*: Burnet OCT Polytonic Greek & Jowett 3rd ed. English) and 100% exact SymPy / Rational Trigonometry symbolic construction library for **Plato's Mathematical & Geometric Dialogues**.

---

## 1. Purpose & Scope

`geometor/plato` (`geometor-plato`) bridges the fourth-century Athenian Academy with the entire GEOMETOR historical and constructive ecosystem, reconciling all **58 cross-corpus `plato:*` citation entries** across `euclid`, `elements`, `proclus`, `aristotle`, `pacioli`, and `hoenen` across six Codex units:

1. **Unit I (`meno`)**: *Meno* (`75d–76a`, `81e–85d`, `86e–87b`) — Figure as limit of solid, *anamnesis* & doubling the square by the diagonal ($Q = 4 + 4 = 8$), and inquiry from hypothesis (elliptic application of areas).
2. **Unit II (`theaetetus`)**: *Theaetetus* (`147c–148b`) — Theodorus's square-root diagrams ($\sqrt{3}\dots\sqrt{17}$) and Theaetetus's classification of commensurable lengths (*mēkē*) and quadratic powers (*dynameis*).
3. **Unit III (`republic`)**: *Republic* VI (`509d–511e`) & VII (`525a–534e`) — The Divided Line ($|BC| = |CD|$), *dianoia* vs. *noēsis*, mathematical hypotheses, and the five sciences of the Quadrivium.
4. **Unit IV (`timaeus-world-soul`)**: *Timaeus* (`31b–36d`) — Continuous geometric proportion ($a:b=b:c$), arithmetic & harmonic means, and the 34-pitch World-Soul diatonic scale (`1..27`, 24 tones of $9:8$, 9 *leimmata* of $256:243$, Crantor base `384`).
5. **Unit V (`timaeus-polyhedra`)**: *Timaeus* (`53c–56c`) — The isosceles ($1:1:\sqrt{2}$) and scalene ($1:\sqrt{3}:2$, spreads $\frac{1}{4}, \frac{3}{4}, 1$) elementary right triangles and assembly of the five cosmic polyhedra.
6. **Unit VI (`foundations`)**: *Parmenides* (`137d–138a`, `145a–b`), *Philebus* (`16c–26d`, `51b–52c`), and *Laws* VII (`817e–820d`) — Optical straightness, Limit (*peras*) & Unlimited (*apeiron*), pure geometric beauty by compass & straightedge, and three-dimensional incommensurability.

---

## 2. Key Modules (`src/geometor/plato/`)

- `harmonics.py`: Exact `sp.Rational` engine generating the 34-pitch *Timaeus* World-Soul scale, Crantor's integer multiplier (`384`), Archytean means, whole tones (`9/8`), and *leimmata* (`256/243`).
- `constructions.py`: Exact `geometor.model.Model(..., auto_intersect=False)` builders and `@proposition` proofs (`construct_meno_diagonal_doubling`, `classify_theaetetus_powers`, `construct_theodorus_spiral`, `verify_divided_line_identity`, `construct_divided_line`, `construct_timaeus_proportion_circles`, `construct_timaeus_triangles`, `construct_timaeus_cube_face`, `construct_compass_and_peras`).
- `render.py`: Theme-adaptive `.euclid-graphic` SVG renderer (`fast_line_coeffs`, `<defs>` tick markers, 3-vertex midpoint `<path>` segments, `data-ref` / `data-aliases`) compatible with `photon-platform/publish` `geometor_interactive.js`.
- `units.py`: Canonical `PassageSpec` and `CodexUnitSpec` metadata for all 11 passages across 6 units.
- `concordance.py`: Master Stephanus concordance reconciling all 58 cross-corpus `plato:*` entries into 36 canonical loci (`resources/concordance.json`).
- `apparatus.py`: Glossary (`34` Greek/Latin terms), persons (`23` entries), and bibliography (`30` entries) mirrored to `resources/` and `resources/loci_mathematici/`.
- `commentary.py`: Scholarly summaries, literal Greek mathematical philology notes, interactive `:g:`/`:eq:` reconstructions, and reception commentary.
- `compile_codex.py`: Deterministic compiler parsing Burnet OCT TEI-XML and Jowett 1892 TXT sources into the 4-track Book Codex (`docsrc/loci_mathematici/`).
- `sphinx_ext.py`: Sphinx extension registering the `-el` (`"Greek (Burnet OCT)"`) track in `photon_platform.publish.book`.
- `cli.py`: Rich CLI (`geometor-plato compile|figures|scale|concordance|verify`).

---

## 3. Architectural Mandates

1. **100% Exact Symbolic Precision**: Never introduce `float` or `sp.Float` into `geometor.model.Model`; always construct with `Model(..., auto_intersect=False)` and explicit `model.intersect(...)`.
2. **Strict Content / Code Separation**: Never place `.. code-block:: python` or `py_file` directives inside `docsrc/loci_mathematici/`. Executable constructions belong strictly in `src/geometor/plato/`, `demos/`, and `docsrc/demos/`.
3. **100% Public-Domain Provenance**: Primary texts in `resources/loci_mathematici/sources/` are strictly John Burnet's OCT Greek (1900–1907) and Benjamin Jowett's 3rd ed. English (1892), verified via SHA-256 in `sources_manifest.json`.

---

## 4. Verification Commands (Python 3.13 / Offline Sandbox)

```bash
ruff check src demos tests
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest -v
publish build
```
