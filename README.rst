================
GEOMETOR • plato
================

**Loci Mathematici et Geometrici** — Scholarly 4-track Bilingual Book Codex (John Burnet's Oxford Classical Text polytonic Greek & Benjamin Jowett's 1892 English) and 100% exact SymPy / Rational Trigonometry symbolic construction suite for **Plato's Mathematical & Geometric Dialogues**.

Overview
--------

``geometor-plato`` unites the eleven foundational mathematical and geometric passages across seven dialogues of Plato (*Meno*, *Theaetetus*, *Republic* VI–VII, *Timaeus*, *Parmenides*, *Philebus*, and *Laws* VII), anchoring all **58 cross-corpus Platonic citations** across ``geometor/euclid``, ``geometor/elements``, ``geometor/proclus``, ``geometor/aristotle``, ``geometor/pacioli``, and ``geometor/hoenen``.

Every unit in ``docsrc/loci_mathematici/`` compiles as a synchronized **4-track Book Codex** (``:layout: book``) via ``photon-platform/publish``:

1. **English** (``-en.rst``) — Verbatim public-domain 3rd revised edition (1892) of Benjamin Jowett, anchored to Stephanus ``a–e`` folios.
2. **Greek (Burnet OCT)** (``-el.rst``) — Verbatim polytonic Greek from John Burnet's *Platonis Opera* (1900–1907).
3. **Summary** (``-summary.rst``) — Deductive synopsis and Stephanus passage breakdown.
4. **Critical Notes** (``-notes.rst``) — Interactive ``.euclid-graphic`` SVG diagrams (``:g:`` / ``:eq:``), literal Greek mathematical philology notes, and cross-corpus reception (with zero embedded Python scripts inside the historical Codex).

Codex Units & Exact Symbolic Constructions
------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 22 24 54

   * - Unit
     - Stephanus Loci
     - Symbolic Model & Mathematical Invariants
   * - **I. Meno**
     - ``75d–76a``, ``81e–85d``, ``86e–87b``
     - ``construct_meno_diagonal_doubling()`` — Square ``ABCD`` (:math:`Q=4`), false squares (:math:`Q=16`, :math:`Q=9`), and diagonal square ``BHKD`` (:math:`Q = 4 + 4 = 8`).
   * - **II. Theaetetus**
     - ``147c–148b``
     - ``construct_theodorus_spiral(max_n=17)`` & ``classify_theaetetus_powers()`` — Exact compass-and-straightedge spiral :math:`Q(O, P_n) = n` separating rational *mēkē* (``1, 4, 9, 16``) from 13 surd *dynameis*.
   * - **III. Republic VI–VII**
     - ``509d–511e``, ``525a–534e``
     - ``construct_divided_line()`` & ``verify_divided_line_identity()`` — Exact :math:`\mathbb{Q}(\phi)` Divided Line proving :math:`|BC| = |CD|` and semicircle mean proportional :math:`|BG| = |BC|`.
   * - **IV. Timaeus (World-Soul)**
     - ``31b–36d``
     - ``build_timaeus_scale()`` & ``construct_timaeus_proportion_circles()`` — 34-pitch rational scale (``1..27``, 24 tones of ``9/8``, 9 *leimmata* of ``256/243``, Crantor base ``384``) and 3 means in a semicircle.
   * - **V. Timaeus (Polyhedra)**
     - ``53c–56c``
     - ``construct_timaeus_triangles()`` & ``construct_timaeus_cube_face()`` — Scalene half-equilateral (:math:`Q=(1,3,4)`, spreads :math:`(1/4, 3/4, 1)`) and isosceles right triangle (:math:`Q=(1,1,2)`, spreads :math:`(1/2, 1/2, 1)`).
   * - **VI. Foundations**
     - *Parm.* ``137d–138a``, ``145a–b``; *Phil.* ``16c–26d``, ``51b–52c``; *Laws* ``817e–820d``
     - ``construct_compass_and_peras()`` — Optical sightline ``AB``, unit circle, and dimensional surd tower :math:`1, \sqrt{2}, \sqrt{3}`.

Installation & CLI Usage
------------------------

Managed with ``uv`` on Python 3.13:

.. code-block:: bash

   uv pip install -e .

   # Verify all exact SymPy invariants, SHA-256 sources, and Stephanus anchors
   geometor-plato verify

   # Display the 34-pitch Timaeus World-Soul harmonic scale (Crantor base 384)
   geometor-plato scale

   # Inspect the 58 cross-corpus Stephanus concordance mappings
   geometor-plato concordance

   # Re-export the 6 interactive .euclid-graphic SVGs and 4-track Codex RSTs
   geometor-plato compile

   # Build the Sphinx Book Codex HTML site
   publish build

License
-------

MIT License (code, apparatus, commentary, and SVG reconstructions); public-domain primary texts (Burnet OCT 1900–1907 & Jowett 3rd ed. 1892).
