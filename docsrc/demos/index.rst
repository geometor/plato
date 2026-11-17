:order: 25
:nav_title: Demos

.. _demos:

=====
Demos
=====

.. rubric:: 100% Exact Symbolic SymPy Models & Rational Trigonometry Proofs of Plato's Constructions

In strict accordance with **GEOMETOR's Content / Code Separation**, the historical Book Codex (:doc:`/index`) contains zero embedded Python scripts. All executable constructions live in the ``geometor.plato`` Python package and runnable ``demos/*.py`` scripts documented below, where every coordinate, intersection, quadrance, spread, and harmonic interval is verified symbolically over :math:`\mathbb{Q}` and closed-form quadratic extensions (:math:`\mathbb{Q}(\sqrt{2})`, :math:`\mathbb{Q}(\sqrt{3})`, :math:`\mathbb{Q}(\phi)`, and the Theodorus tower :math:`\mathbb{Q}(\sqrt{2}, \dots, \sqrt{17})`) with ``Model(..., auto_intersect=False)`` and **zero floating-point approximations**.

----

1. *Meno* ``82b–85b`` — Doubling the Square by the Diagonal
-----------------------------------------------------------

*Codex Reference*: :doc:`Meno: Doubling the Square (Critical Notes) </meno/82b-85b/notes>` · *Script*: ``demos/meno_diagonal.py``

.. picture:: /_static/figures/meno_diagonal_doubling.svg
   :caption: Exact symbolic model of Socrates' three-stage inquiry with Meno's attendant: given 2-foot square ``ABCD`` (quadrance 4), false 4-foot square ``AEFG`` (quadrance 16), false 3-foot square ``AMNP`` (quadrance 9), and diagonal square ``BHKD`` (quadrance 8).

* **Symbolic Verification**:
  Given :g:`A = (0, 0)` and :g:`B = (2, 0)`, :eq:`/ A B / = 2` has quadrance :math:`Q(A, B) = 4`. Doubling the side to :g:`E = (4, 0)` quadruples quadrance (:math:`Q(A, E) = 16`); taking the 3-foot side :g:`M = (3, 0)` yields :math:`Q(A, M) = 9` (leaving no rational integer solution to :math:`x^2 = 8`). Drawing the :term:`diagonal <diametros>` :g:`[ B D ]` (:g:`B = (2, 0)`, :g:`D = (0, 2)`) bisects ``ABCD`` into two triangles of area :math:`2` and establishes the diagonal square ``BHKD`` (:g:`H = (2, 2)`, :g:`K = (0, 4)` in the enclosing grid, or erected directly on :g:`/ B D /`) with exact quadrance :math:`Q(B, D) = 4 + 4 = 8 = 2 \cdot Q(A, B)`.

.. code-block:: python

   from geometor.model.invariants import quadrance
   from geometor.plato import construct_meno_diagonal_doubling

   model = construct_meno_diagonal_doubling()
   pt_a = model.get_element_by_ID("A")
   pt_b = model.get_element_by_ID("B")
   pt_d = model.get_element_by_ID("D")
   pt_e = model.get_element_by_ID("E")
   pt_m = model.get_element_by_ID("M")
   assert quadrance(pt_a, pt_b) == 4
   assert quadrance(pt_a, pt_e) == 16
   assert quadrance(pt_a, pt_m) == 9
   assert quadrance(pt_b, pt_d) == 8

----

2. *Theaetetus* ``147d–148b`` — Theodorus's Spiral (:math:`\sqrt{2} \dots \sqrt{17}`) & *Dynameis*
---------------------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Theaetetus: Theodorus's Radical Chain (Critical Notes) </theaetetus/147d-148b/notes>` · *Script*: ``demos/theodorus_spiral.py``

.. picture:: /_static/figures/theodorus_spiral.svg
   :caption: Exact compass-and-straightedge spiral from ``P1`` through ``P17`` around center ``O``. Square-number radii ``P1, P4, P9, P16`` are rational lengths (*mēkē*); all thirteen non-square radii are quadratic surds (*dynameis*).

* **Symbolic Verification**:
  At each step :math:`n \in \{1, \dots, 16\}`, a perpendicular line is erected at :math:`P_n` on carrier :math:`O P_n` and intersected with the unit circle centered at :math:`P_n` to select the counterclockwise vertex :math:`P_{n+1}` with unit step quadrance :math:`Q(P_n, P_{n+1}) = 1` and exact radial quadrance :math:`Q(O, P_n) = n` for all :math:`1 \le n \le 17`.

.. code-block:: python

   from geometor.model.invariants import quadrance
   from geometor.plato import classify_theaetetus_powers, construct_theodorus_spiral

   report = classify_theaetetus_powers(17)
   assert [r.area_n for r in report if "mekos" in r.line_kind] == [1, 4, 9, 16]

   spiral = construct_theodorus_spiral(max_n=17)
   origin = spiral.get_element_by_ID("O")
   for n in range(1, 18):
       assert quadrance(origin, spiral.get_element_by_ID(f"P{n}")) == n

----

3. *Republic* VI ``509d–511e`` — The Divided Line & Proportional Equality of the Middle Segments
------------------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Republic: The Divided Line (Critical Notes) </republic/509d-511e/notes>` · *Script*: ``demos/divided_line.py``

.. picture:: /_static/figures/republic_divided_line.svg
   :caption: Exact golden-section realization of Plato's Divided Line ``AE`` cut at ``C`` with sub-cuts ``B`` and ``D``, verifying ``|BC| = |CD|`` and the Euclid VI.13 semicircle mean proportional ``|BG| = |BC|``.

* **Symbolic Verification**:
  Cutting baseline :g:`/ A E /` in ratio :math:`1 : r` at :g:`C` and each main section in the same ratio :math:`1 : r` at :g:`B` and :g:`D` forces :math:`|AB| : |BC| : |CD| : |DE| = 1 : r : r : r^2` for *every* :math:`r \neq 1` (verified symbolically over ``sp.Symbol('r', positive=True)``) and specifically over :math:`\mathbb{Q}(\phi)` (:math:`r = \phi = \frac{1 + \sqrt{5}}{2}`), where the semicircle on :g:`/ A K /` meets the perpendicular at :g:`B` in :g:`G` with :math:`Q(B, G) = Q(B, C) = Q(C, D) = \phi^2`.

.. code-block:: python

   from geometor.model.invariants import quadrance
   from geometor.plato import construct_divided_line, verify_divided_line_identity

   ident = verify_divided_line_identity()
   assert ident["middle_segments_equal"] is True

   line_model = construct_divided_line()
   pt_b = line_model.get_element_by_ID("B")
   pt_c = line_model.get_element_by_ID("C")
   pt_d = line_model.get_element_by_ID("D")
   pt_g = line_model.get_element_by_ID("G")
   assert quadrance(pt_b, pt_c) == quadrance(pt_c, pt_d)
   assert quadrance(pt_b, pt_g) == quadrance(pt_b, pt_c)

----

4. *Timaeus* ``31b–36d`` — Three Means in a Semicircle & the 34-Pitch World-Soul Scale
--------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Timaeus: The World-Soul (Critical Notes) </timaeus/31b-36d/notes>` · *Script*: ``demos/timaeus_world_soul.py``

.. picture:: /_static/figures/timaeus_world_soul.svg
   :caption: Pappus's semicircle construction of arithmetic mean ``|OG| = 3``, geometric mean ``|JG| = 2√2``, and harmonic mean ``|GH| = 8/3`` on segments ``|AJ| = 2`` and ``|JB| = 4``, paired with the equatorial Circle of the Same and ecliptic Circle of the Different.

* **Symbolic Verification**:
  Starting from the seven integers ``1, 2, 3, 4, 8, 9, 27``, inserting harmonic means :math:`\frac{2ab}{a+b}` and arithmetic means :math:`\frac{a+b}{2}`, and filling every :math:`4:3` fourth with two :math:`9:8` whole tones leaves the exact Pythagorean *leimma* :math:`\frac{256}{243}`, generating **34 exact rational pitches** (:math:`24` tones and :math:`9` *leimmata*: :math:`(9/8)^{24} \cdot (256/243)^9 = 27`), cleared of fractions by :person:`Crantor's <crantor>` least integer multiplier ``384`` (``384 .. 10368``).

.. code-block:: python

   import sympy as sp
   from geometor.plato import CRANTOR_INTEGER_MULTIPLIER, EPOGDOOS, LEIMMA, build_timaeus_scale

   pitches = build_timaeus_scale()
   assert len(pitches) == 34
   assert pitches[0].crantor_integer == CRANTOR_INTEGER_MULTIPLIER == 384
   assert pitches[-1].crantor_integer == 10368
   assert sp.simplify(EPOGDOOS**24 * LEIMMA**9 - 27) == 0

----

5. *Timaeus* ``53c–56c`` — Elementary Right Triangles & Rational Trigonometry Spreads
-------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Timaeus: Elementary Triangles (Critical Notes) </timaeus/53c-56c/notes>` · *Script*: ``demos/timaeus_triangles.py``

.. picture:: /_static/figures/timaeus_triangles.svg
   :caption: Euclid I.1 two-circle construction of equilateral face ``ABC`` subdivided by its three medians/altitudes at centroid ``G`` into six ``1 : √3 : 2`` scalene right half-triangles (quadrances ``1, 3, 4``; spreads ``1/4, 3/4, 1``).

* **Symbolic Verification**:
  Both of Timaeus's elementary planar building blocks satisfy polynomial **Rational Trigonometry** identities without transcendental angles:

  - **Scalene Half-Equilateral** (:math:`\triangle GM_1C`): quadrances :math:`(1, 3, 4)`, spreads :math:`\left(\frac{1}{4}, \frac{3}{4}, 1\right)` ("the greater side triple in power of the lesser", ``54b5``).
  - **Isosceles Right Triangle** (cube face ``ABCD`` bisected by diagonals at center ``O``): quadrances :math:`(1, 1, 2)` around ``O``, spreads :math:`\left(\frac{1}{2}, \frac{1}{2}, 1\right)`.

.. code-block:: python

   import sympy as sp
   from geometor.model import quadrance, vertex_spread
   from geometor.plato import construct_timaeus_cube_face, construct_timaeus_triangles

   tri = construct_timaeus_triangles()
   pt_g = tri.get_element_by_ID("G")
   pt_m1 = tri.get_element_by_ID("M1")
   pt_c = tri.get_element_by_ID("C")
   assert (quadrance(pt_g, pt_m1), quadrance(pt_m1, pt_c), quadrance(pt_g, pt_c)) == (1, 3, 4)
   assert vertex_spread(pt_g, pt_c, pt_m1) == sp.Rational(1, 4)
   assert vertex_spread(pt_m1, pt_g, pt_c) == sp.Rational(3, 4)
   assert vertex_spread(pt_g, pt_m1, pt_c) == 1

   cube = construct_timaeus_cube_face()
   assert cube is not None

----

6. *Parmenides*, *Philebus* & *Laws* VII — Compass, Straightedge & Dimensional Surds
------------------------------------------------------------------------------------

*Codex Reference*: :doc:`Dialogues on Measure & Proportion (Critical Notes) </foundations/parmenides-137d-138a/notes>`

.. picture:: /_static/figures/foundations_peras_compass.svg
   :caption: Unit circle centered at ``O`` cut along optical sightline ``AB`` (Parmenides 137e), generating length ``1`` (``OC``), plane diagonal ``√2`` (``OD``), and space-diagonal power ``√3`` (``OE``) by compass and straightedge (Philebus 51c; Laws VII 819e).

* **CLI Quickstart**:
  Run all symbolic invariant checks, inspect the 34-pitch *Timaeus* table, or recompile all SVGs and 4-track RST units via ``geometor-plato``:

.. code-block:: bash

   geometor-plato verify
   geometor-plato scale
   geometor-plato concordance
   geometor-plato figures
   geometor-plato compile
