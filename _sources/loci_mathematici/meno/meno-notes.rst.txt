:layout: book
:type: notes
:title: Unit I — Meno: Definition of Figure, Doubling the Square & Geometric Hypothesis — Notes
:canonical_id: Meno 75d–76a, 81e–85d, 86e–87b
:original_id: Stephanus Meno 75d–76a, 81e–85d, 86e–87b
:folio: Meno 75d–76a, 81e–85d, 86e–87b

.. _meno-notes:

=============================================================================================================
Unit I — Meno: Definition of Figure, Doubling the Square & Geometric Hypothesis — Critical Commentary & Notes
=============================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Meno 75d–76a, 81e–85d, 86e–87b

.. picture:: /_static/figures/meno_diagonal_doubling.svg
   :alt: Meno: Definition of Figure, Doubling the Square & Geometric Hypothesis
   :caption: Socrates' Geometric Demonstration in Meno 82b–85b: the 2×2 given square < A B C D > (Q = 4), the 4×4 fourfold square < A E F G > (Q = 16), the 3×3 nine-foot trial < A M N P > (Q = 9), and the inscribed diagonal square < B H K D > (Q = 8).

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_meno_diagonal_doubling`` (see :doc:`/demos/index`), Socrates' sand diagram (`82b–85b`) is modeled with 100% exact rational coordinates over :math:`\mathbb{Q}` without introducing irrational square roots until linear magnitude is requested—directly vindicating Rational Trigonometry's primacy of **quadrance**:

- **Given Two-Foot Square** :g:`ABCD <meno-diag:< A B C D >>` (`82c–d`): Anchored at :g:`A <meno-diag:A>` :math:`= (0,0)` and :g:`B <meno-diag:B>` :math:`= (2,0)`, every side has quadrance :math:`Q(A,B) = 4`, enclosing area :math:`4` square feet.
- **First Refutation — Doubling the Side** (`82e–83c`): Extending :g:`A B <meno-diag:/ A B />` to :g:`E <meno-diag:E>` :math:`= (4,0)` produces the fourfold square :g:`AEFG <meno-diag:< A E F G >>` of quadrance :math:`Q(A,E) = 16` (composed of four :math:`4`-foot squares meeting at interior center :g:`C <meno-diag:C>` :math:`= (2,2)`).
- **Second Refutation — The Three-Foot Trial** (`83d–e`): Searching strictly between :math:`2` and :math:`4`, the attendant proposes the arithmetic midpoint :g:`M <meno-diag:M>` :math:`= (3,0)` (`sesquialter` :math:`3:2`), which generates square :g:`AMNP <meno-diag:< A M N P >>` of quadrance :math:`Q(A,M) = 9 \neq 8`, bringing on the purifying **aporia** (`84a–c`).
- **Constructive Resolution via the Four Diagonals** (`84d–85b`): Drawing the four :term:`diagonals <diametros>` :g:`BD <meno-diag:[ B D ]>`, :g:`BH <meno-diag:[ B H ]>`, :g:`HK <meno-diag:[ H K ]>`, and :g:`KD <meno-diag:[ K D ]>` across the four sub-squares cuts each :math:`4`-foot square into two equal isosceles right triangles of area :math:`2`. The inscribed tilted square :g:`BHKD <meno-diag:< B H K D >>` therefore has exact area and side quadrance:

  .. math::

     Q(B, D) = Q(A, B) + Q(A, D) = 4 + 4 = 8 = 2 \, Q(A, B).

**Socrates' Elliptic Application Hypothesis (86e–87b)**: As :person:`Sir Thomas Heath <heath>` demonstrated (:cite:`History of Greek Mathematics <heath:greek-math:1921>`, Vol. I, pp. 298–303), Socrates' famous geometric obscurity at `87a`—inscribing a given area :math:`C` as a triangle in a circle of diameter :math:`AB = d`—reduces to choosing a point :math:`X` on diameter :math:`AB` and erecting ordinate :math:`XY` to the circle so that rectangle :math:`AX \cdot XY = C`. Since in the semicircle :math:`XY^2 = AX \cdot XB`, squaring gives :math:`AX \cdot XB = (C / AX)^2`, meaning rectangle :math:`AX \cdot XY` is **applied** (:term:`parateinein <parateinein>`) along :math:`AB` while **falling short** (*ἐλλείπειν*) on :math:`XB` by a rectangle :math:`XB \cdot XY` *similar* to the applied rectangle :math:`AX \cdot XY` (:math:`AX : XY = XY : XB`)—an exact fourth-century instance of hyperbolic/elliptic application of areas (:cite:`Elements VI.28 <euclid:VI.28>`).

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **76a7 — στερεοῦ πέρας σχῆμα εἶναι**: :person:`Jowett <jowett>` translates *'figure is the limit of solid'*, faithfully preserving :person:`Burnet's <burnet>` technical pairing of :term:`stereon <stereon>` and :term:`peras <peras>`. Compare :cite:`Elements XI, Def. 2 <euclid:I.def.13>` (*στερεοῦ δὲ πέρας ἐπιφάνεια*, 'the extremity of a solid is a surface') and :cite:`I, Def. 14 <euclid:I.def.13>` ('a figure is that which is contained by any boundary or boundaries').
- **85b4 — διάμετρον ὄνομα, καλοῦσιν δὲ ταύτην οἱ σοφισταί**: Here *σοφισταί* denotes technical mathematical experts/professors rather than eristic rhetoricians; :term:`diametros <diametros>` means the diagonal of the square (preserved throughout :person:`Euclid <euclid>` and :person:`Aristotle <aristotle>`).
- **87a3–6 — παρὰ τὴν δοθεῖσαν αὐτοῦ γραμμὴν παρατείναντα ἐλλείπειν τοιούτῳ χωρίῳ οἷον ἂν αὐτὸ τὸ παρατεταμένον ᾖ**: Jowett renders loosely *'whether, if the figure be applied to the given line of the circle, it is deficient by another figure similar to that which is applied'*. Literally, *παρατείνειν παρὰ γραμμήν* is the technical Pythagorean-Academic idiom for **parabolic/elliptic application of an area along a given straight line** (*παραβολή / ἔλλειψις τῶν χωρίων*), later standardized by Euclid in Book VI and by Apollonius in naming the *parabola* and *ellipse*.

III. Reception in Aristotle, Euclid, Proclus & Hoenen
-----------------------------------------------------

- **Aristotle** (:cite:`Anal. Post. I.1, 71a29 <aristotle:anal-post>`; ``plato:meno``): Resolves Meno's dilemma by distinguishing universal pre-existent knowledge (*that every triangle has 2R*) from simultaneous recognition (*ἅμα ἐπαγόμενος*) that the drawn figure falls under the universal.
- **Proclus** (:cite:`In Euclidem, Friedlein 45.15–46.3 <proclus:in-euclidem>`; ``plato:meno:81e-85d``): Cites Socrates' questioning of the boy as proof that mathematical *logoi* reside substantially within the soul rather than being stamped from outside by sense-impressions.
- **Hoenen** (:cite:`De Noetica Geometriae <hoenen:noetica:1952>`, Cap. I & VII; ``plato:meno:82b-85b``): Highlights `82b–85b` as the locus classicus for **intellectual vision in the singular phantasm**: the boy counts neither decimal approximations of :math:`2\sqrt{2} \approx 2.828` nor syllogistic major premises, but beholds universal necessity (:math:`4 \times \frac{1}{2} \times 4 = 8`) directly in the bisected grid.

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit I** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
