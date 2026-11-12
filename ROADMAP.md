# Roadmap — `geometor/plato`

## v0.1.0 — Initial 4-Track Codex & Symbolic Engine (Completed)
- Stage and SHA-256 audit 14 public-domain Burnet OCT Greek (1900–1907) and Jowett 3rd ed. English (1892) source texts across *Meno*, *Theaetetus*, *Republic* VI–VII, *Timaeus*, *Parmenides*, *Philebus*, and *Laws* VII.
- Implement 100% exact SymPy & Rational Trigonometry models (`auto_intersect=False`, zero `sp.Float`) in `src/geometor/plato/constructions.py` and `harmonics.py`.
- Export 6 theme-adaptive interactive `.euclid-graphic` SVGs and compile 6 synchronized 4-track Book Codex units (`-en`, `-el`, `-summary`, `-notes`).
- Reconcile all 58 cross-corpus `plato:*` citations across `euclid`, `elements`, `proclus`, `aristotle`, `pacioli`, and `hoenen` into `resources/concordance.json`.

## v0.2.0 — Extended Mathematical Loci & 3D Polyhedral Nets
- Expand the Codex with *Republic* VIII `546a–d` (the Nuptial/Geometric Number), *Phaedo* `100b–105c` (hypotheses & odd/even parity), *Laws* V `737e–738b` (`5040 = 7!` civic divisibility), and *Epinomis* `990c–991b` (continuous geometric assimilation of plane and solid surds).
- Add exact planar net unfoldings and dihedral spread invariants (`1/9`, `8/9`, `4/9`, `4/5`) for all five regular polyhedra over $\mathbb{Q}(\sqrt{3}, \phi)$, cross-linked directly to `geometor/elements` Book XIII and `geometor/pacioli`.

## v0.3.0 — Elliptic Area Application & Antanairesis Explorer
- Add interactive `geometor.model` construction of Socrates' *Meno* `86e–87b` elliptic application of areas (`Euclid VI.27–28` *diorismos* for inscribing a triangle of given area in a given circle).
- Add Wilbur Knorr's `antanairesis` / parity-cascade comparison alongside Theodorus's spiral for $\sqrt{3}\dots\sqrt{17}$, demonstrating why parity case-splitting halts cleanly at $17 \equiv 1 \pmod 8$.

## v0.4.0 — Studio QHD Choreography (`videos/`)
- Produce `2560x1440` QHD `photon-platform/studio` episodes for *Meno*'s diagonal recollection, *Republic*'s Divided Line, and the audible 34-pitch *Timaeus* World-Soul scale paired with `harmonic-resonance/groove`.
