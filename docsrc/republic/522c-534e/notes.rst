:layout: book
:type: notes
:title: The Quadrivium & Dialectic — Notes
:canonical_id: Republic VII, 522c–534e
:folio: Rep. 522c
:tracks: English: index | Greek: greek | Summary: summary | Notes: notes

.. _republic-525a-534e-notes:
.. _republic-522c-534e-notes:

===========================================
The Quadrivium & Dialectic — Critical Notes
===========================================

.. rubric:: Stereometry, Philology & Canon Reception · Republic VII 522c–534e

I. Stereometry as the Missing Third Science
-------------------------------------------

- **528b1–3 — μετὰ ἐπίπεδον… ἐν περιφορᾷ ὂν ἤδη στερεὸν λαβόντες, πρὶν αὐτὸ καθ’ αὑτὸ λαβεῖν**: Socrates corrects his own initial sequence (`plane geometry -> astronomy`) because astronomy treats **solid body already in revolution** before investigating **three-dimensional solid in itself** (*ἡ τῶν κύβων αὔξη καὶ τὸ βάθους μετέχον*, `528b3`). Within one generation of this passage, :person:`Theaetetus <theaetetus>` and :person:`Eudoxus <eudoxus>` created the rigorous stereometry preserved in :cite:`Elements Books XI–XIII <euclid:XIII.13>`.

II. Reception & Sister-Corpus Civic-Arithmetic Locus (*Laws* V 737e–738b)
--------------------------------------------------------------------------

- **Proclus** (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 29–32; ``plato:rep:VII.525a-534e``): Reconciles Republic VII's five mathematical sciences with Euclidean methodology.
- **Hoenen & Civic Arithmetic** (``plato:rep:VI.510c``, ``VII.532c``, ``VII.533c``, and ``plato:leges:737e-738b``, ``738a``): In *De Noetica Geometriae* Cap. IV, :person:`Hoenen <hoenen>` pairs Republic VII's pure arithmetic (`525a–526c`) with Plato's remarkable divisor theorem in *Laws* V `737e–738b`, where the Athenian Stranger selects **5,040** (:math:`= 7! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 = 2^4 \cdot 3^2 \cdot 5 \cdot 7`) for civic land allotments because it possesses :math:`(4+1)(2+1)(1+1)(1+1) = 60` total divisors (`59` proper quotients excluding itself) and is evenly divisible by **every integer from 1 to 10** (and even by `12`, while `5,040 - 2 = 5,038 = 11 \times 458` restores divisibility by `11`).

III. Executable Symbolic Verification
-------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions live in ``src/geometor/plato/`` and :doc:`/demos/index`.
