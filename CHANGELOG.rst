=========
changelog
=========

0.1.0 (2026-11-12)
------------------

Initial scholarly edition and exact symbolic modeling release of ``geometor-plato`` (*Loci Mathematici et Geometrici*):

* **4-Track Synchronized Book Codex** (``docsrc/loci_mathematici/``, ``:layout: book``):

  - **Unit I — Meno** (``75d–76a``, ``81e–85d``, ``86e–87b``): Figure as limit of solid, *anamnesis* & doubling the square by the diagonal (:math:`Q = 4 + 4 = 8`), and inquiry from hypothesis (elliptic application of areas).
  - **Unit II — Theaetetus** (``147c–148b``): Theodorus's square-root diagrams (:math:`\sqrt{3}\dots\sqrt{17}`) and Theaetetus's classification of commensurable lengths (*mēkē*) and quadratic powers (*dynameis*).
  - **Unit III — Republic VI–VII** (``509d–511e``, ``525a–534e``): The Divided Line, *dianoia* vs. *noēsis*, mathematical hypotheses, and the five sciences of the Quadrivium (arithmetic, plane geometry, stereometry, astronomy, harmonics).
  - **Unit IV — Timaeus: Cosmic Proportion & World-Soul** (``31b–36d``): Continuous geometric proportion (:math:`a:b=b:c`), arithmetic & harmonic means, and the 34-pitch diatonic scale (``1..27``, 24 tones of ``9:8``, 9 *leimmata* of ``256:243``, Crantor integer base ``384``).
  - **Unit V — Timaeus: Elementary Triangles & Polyhedra** (``53c–56c``): Isosceles (:math:`1:1:\sqrt{2}`) and scalene (:math:`1:\sqrt{3}:2`, spreads :math:`1/4, 3/4, 1`) right triangles and assembly of the five cosmic solids.
  - **Unit VI — Parmenides, Philebus & Laws VII** (``137d–138a``, ``145a–b``; ``16c–26d``, ``51b–52c``; ``817e–820d``): Optical straightness, Limit (*peras*) & Unlimited (*apeiron*), pure compass-and-straightedge beauty, and three-dimensional incommensurability.

* **Exact Symbolic Engine & Interactive ``.euclid-graphic`` SVGs** (``src/geometor/plato/``):

  - Exact SymPy ``geometor.model`` constructions (``auto_intersect=False``, zero ``sp.Float``) in ``constructions.py``, rational World-Soul harmonics in ``harmonics.py``, theme-adaptive ``.euclid-graphic`` SVG exporter in ``render.py``, and Rich CLI ``geometor-plato`` in ``cli.py``.
  - Runnable exact demonstrations in ``demos/`` and Sphinx walkthroughs in ``docsrc/demos/index.rst`` (strictly separated from the historical Codex).

* **Cross-Corpus Stephanus Concordance & Apparatus**:

  - Reconciled all 58 ``plato:*`` citations across ``euclid``, ``elements``, ``proclus``, ``aristotle``, ``pacioli``, and ``hoenen`` into 36 canonical Stephanus entries in ``resources/concordance.json``, paired with SHA-256 ``sources_manifest.json``, ``glossary.json``, ``persons.json``, and ``citations.json``.
