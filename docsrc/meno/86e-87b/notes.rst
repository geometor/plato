:layout: book
:type: notes
:title: Method of Hypothesis — Notes
:canonical_id: Meno 86e–87b
:folio: Meno 86e
:tracks: English: index | Greek (Burnet OCT): greek | Summary: summary | Notes: notes

.. _meno-86e-87b-notes:

==============================================
Method of Hypothesis — Critical Notes
==============================================

.. rubric:: Geometric Reconstruction & Academic Hypothesis · Meno 86e–87b

I. Geometric Significance
-------------------------

**Socrates' Elliptic Application Hypothesis (86e–87b)**: As :person:`Sir Thomas Heath <heath>` demonstrated (:cite:`History of Greek Mathematics <heath:greek-math:1921>`, Vol. I, pp. 298–303), Socrates' famous geometric obscurity at `87a`—inscribing a given area :math:`C` as a triangle in a circle of diameter :math:`AB = d`—reduces to choosing a point :math:`X` on diameter :math:`AB` and erecting ordinate :math:`XY` to the circle so that rectangle :math:`AX \cdot XY = C`. Since in the semicircle :math:`XY^2 = AX \cdot XB`, squaring gives :math:`AX \cdot XB = (C / AX)^2`, meaning rectangle :math:`AX \cdot XY` is **applied** (:term:`parateinein <parateinein>`) along :math:`AB` while **falling short** (*ἐλλείπειν*) on :math:`XB` by a rectangle :math:`XB \cdot XY` *similar* to the applied rectangle :math:`AX \cdot XY` (:math:`AX : XY = XY : XB`)—an exact fourth-century instance of hyperbolic/elliptic application of areas (:cite:`Elements VI.28 <euclid:VI.28>`).

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **87a3–6 — παρὰ τὴν δοθεῖσαν αὐτοῦ γραμμὴν παρατείναντα ἐλλείπειν τοιούτῳ χωρίῳ οἷον ἂν αὐτὸ τὸ παρατεταμένον ᾖ**: Jowett renders loosely *'whether, if the figure be applied to the given line of the circle, it is deficient by another figure similar to that which is applied'*. Literally, *παρατείνειν παρὰ γραμμήν* is the technical Pythagorean-Academic idiom for **parabolic/elliptic application of an area along a given straight line** (*παραβολή / ἔλλειψις τῶν χωρίων*), later standardized by Euclid in Book VI and by Apollonius in naming the *parabola* and *ellipse*.

III. Reception
--------------

- **Euclid** (:cite:`Elements VI.28 <euclid:VI.28>`): Generalizes the elliptic application of area to arbitrary rectilineal figures.
- **Proclus** (:cite:`In Euclidem, Friedlein 45.15–46.3 <proclus:in-euclidem>`): Emphasizes that hypothesis is the supreme engine of Academic geometric reduction.

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions live in ``src/geometor/plato/`` and :doc:`/demos/index`.
