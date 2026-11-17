:layout: book
:type: notes
:title: Theodorus's Irrationals — Notes
:canonical_id: Theaetetus 147d–148b
:folio: Theaet. 147d
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _theaetetus-147d-148b-notes:
.. _theaetetus-147c-148b-notes:
.. _theaetetus-notes:

=======================================================
Theodorus's Irrationals — Critical Commentary & Notes
=======================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Theaetetus 147c–148b

.. picture:: /_static/figures/theodorus_spiral.svg
   :alt: Theodorus's Right-Triangle Radical Chain (Theaetetus 147d–148b)
   :caption: Theodorus's Right-Triangle Radical Chain (Theaetetus 147d–148b): pure compass-and-straightedge construction of exact quadrances Q(O, Pn) = n for 1 <= n <= 17, highlighting rational lengths (P1, P4, P9, P16) vs. quadratic powers (dynameis).

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_theodorus_spiral`` and ``classify_theaetetus_powers`` (see :doc:`/demos/index`), :person:`Theodorus's <theodorus>` lesson (`147d`) is modeled by iterating pure Euclidean perpendicular erection (:cite:`I.11 <euclid:I.11>`) and unit compass transfer (:cite:`Post. 3 <euclid:elements>`):

- Starting from :g:`O <theodorus-spiral:O>` :math:`= (0,0)` and rational unit :g:`P1 <theodorus-spiral:P1>` :math:`= (1,0)` (:math:`Q(O, P_1) = 1`), each orthogonal unit leg :g:`P1 P2 <theodorus-spiral:/ P1 P2 />`, ..., :g:`P16 P17 <theodorus-spiral:/ P16 P17 />` satisfies :eq:`unit quadrance <theodorus-spiral:/ O P1 / = theodorus-spiral:/ P16 P17 />` :math:`Q(P_n, P_{n+1}) = 1` and exact perpendicularity :math:`\overrightarrow{OP_n} \perp \overrightarrow{P_n P_{n+1}}`.
- By Pythagoras's Theorem (:cite:`Elements I.47 <euclid:I.47>`), the spoke quadrances step through every integer from :math:`1` to :math:`17`:

  .. math::

     Q(O, P_{n+1}) = Q(O, P_n) + Q(P_n, P_{n+1}) = n + 1 \quad (1 \le n \le 16).

- **Why Did Theodorus Stop at 17 Square Feet?** (*μέχρι τῆς ἑπτακαιδεκαπόδος, ἐν δὲ ταύτῃ πως ἐνέσχετο*, `147d6`): Modern scholarship (:person:`Heath <heath>` :cite:`1921 <heath:greek-math:1921>`, :person:`Wilbur Knorr <heath>` :cite:`1975 <knorr:evolution:1975>`) highlights two converging reasons visible directly in our exact construction:
  1. **Geometric Self-Overlap**: Summing the interior angles :math:`\sum_{k=1}^{16} \arctan(1/\sqrt{k}) \approx 351.15^\circ < 360^\circ`, whereas adding the :math:`18`-foot triangle (:math:`\arctan(1/\sqrt{17}) \approx 13.63^\circ`) pushes the cumulative angle to :math:`364.78^\circ > 360^\circ`, causing the next spoke to cross the initial baseline :g:`O P1 <theodorus-spiral:/ O P1 />`!
  2. **Pebble/Parity Arithmetic**: In Pythagorean odd-even congruence modulo :math:`8`, every odd square satisfies :math:`(2k+1)^2 = 4k(k+1) + 1 \equiv 1 \pmod{8}`. For :math:`N = 3, 5, 7, 11, 13, 15`, assuming :math:`p^2 = N q^2` immediately fails modulo :math:`4` or :math:`8`, whereas :math:`N = 17 \equiv 1 \pmod{8}` is the **first prime** congruent to :math:`1 \pmod{8}`, requiring an infinite-descent peeling of powers of :math:`2` before contradiction emerges!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **147d3–5 — περὶ δυνάμεών τι ἡμῖν Θεόδωρος ὅδε ἔγραφε, τῆς τε τρίποδος πέρι καὶ πεντέποδος**: :person:`Jowett <jowett>` translates *'Theodorus was writing out for us something about roots, showing that the sides of squares containing three or five square feet...'*. Crucially, **ἔγραφε** means *was drawing geometric diagrams*, and **δύναμις** (:term:`dynamis <dynamis>`) does *not* mean an algebraic number 'root', but a **line segment named from the square area it has the power (*δύναται*) to form**. Likewise **τρίπους** and **πεντέπους** denote *squares of three and five square feet* (literally 'the three-foot [power]', where linear vs. areal 'foot' is determined by feminine *δύναμις*).
- **147e5–148a4 — τὸν ἴσον ἰσάκις… προμήκη δὲ ἀριθμόν**: Burnet's exact multiplicative syntax *ἴσος ἰσάκις γιγνόμενος* ('becoming equal-times-equal', :math:`k \times k`) vs. *πλείων ἐλαττονάκις ἢ ἐλάττων πλειονάκις* ('greater times less or less times greater') is preserved verbatim in :cite:`Euclid Elements VII, Defs. 16–19 <euclid:VII.def.16>`. Note that Plato uses :term:`promēkēs <promekes>` (*oblong*) broadly for *any* non-square integer, whereas later Neopythagoreans restricted *heteromēkēs* to :math:`k(k+1)`.
- **148b1–2 — ὡς μήκει μὲν οὐ συμμέτρους ἐκείναις, τοῖς δ’ ἐπιπέδοις ἃ δύνανται**: Literally *'incommensurable with those in length, but [commensurable] by the plane figures which they have the power to form'*—the verbatim ancestor of :cite:`Euclid Elements X, Defs. 1–2 <euclid:X.def.1>` (*εὐθεῖαι δυνάμει σύμμετροί εἰσιν, ὅταν τὰ ἀπ’ αὐτῶν τετράγωνα τῷ αὐτῷ χωρίῳ μετρῆται*, 'straight lines are commensurable in square/power when the squares on them are measured by the same area').

III. Reception in Euclid Books VII, X & Sister Repositories
-----------------------------------------------------------

All five sister-corpus citations (`plato:theaetetus`, `147.d`, `147D`, `147.d.sqq`, `147-e-148-b` in ``geometor/euclid`` and ``geometor/elements``) converge on **Elements X.9** (attributed explicitly to :person:`Theaetetus <theaetetus>` by an ancient scholium going back to Pappus): *Squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which do not have the ratio of square to square have sides incommensurable in length*.

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit II** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
