\
:layout: book
:type: notes
:title: The Nuptial Number — Notes
:canonical_id: Republic VIII, 546b–d
:folio: Rep. 546b
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _republic-546b-d-notes:

===========================================
The Nuptial Number — Critical Notes
===========================================

.. rubric:: Philology, Mathematical Interpretations & Reception · Republic VIII 546b–d

I. Mathematical Architecture
----------------------------

The Platonic Nuptial Number (*arithmos geōmetrikos*) in *Republic* VIII 546b–d is the most celebrated mathematical crux in the Platonic corpus:

- **Epitritos Pythmēn (4:3)**: The *epitritos* is the 4:3 ratio (the diatonic fourth), and *pythmēn* denotes the lowest terms of the proportion—the legs :math:`3` and :math:`4` of the canonical Pythagorean right triangle.
- **Pempadi Syzygeis**: Paired with the hypotenuse :math:`5`, forming the fundamental right-angled triangle :math:`(3, 4, 5)`.
- **Involution & Evolution**: The sum of cubes of the sides :math:`3^3 + 4^3 + 5^3 = 27 + 64 + 125 = 216` equals :math:`6^3`, corresponding to the 216-day minimum period of human gestation.
- **Rational vs. Irrational Diameters**: The diameter of a square of side :math:`5` has length :math:`\sqrt{50}`. Its nearest rational approximation (*diametros rhētē*) is :math:`7` (since :math:`7^2 = 49 = 50 - 1`). The square on the rational diameter is less by one (:math:`49 = 50 - 1`), while that on the irrational diameter is less by two (:math:`48 = 50 - 2`).

II. Reception
-------------

- **Aristotle** (:cite:`Politics V.12, 1316a1–39 <aristotle:politics>`): Criticizes Plato's theory of cyclical state revolutions based on the geometrical number, asking why the ideal constitution must decline into timocracy rather than its opposite.
- **James Adam** (*The Nuptial Number of Plato*, Cambridge, 1891): Solved the philological riddle by demonstrating that the master period is :math:`(3 \times 4 \times 5)^4 = 60^4 = 12,960,000` days (:math:`36,000` years of :math:`360` days), which equals :math:`100` times :math:`(3600 + 4800 + 2700)` in cyclic harmonics.

III. Executable Symbolic Verification
-------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions live in ``src/geometor/plato/`` and :doc:`/demos/index`.
