:layout: book
:type: notes
:title: Unit III — Republic VI–VII: The Divided Line, Dianoia & the Quadrivium — Notes
:canonical_id: Republic VI 509d–511e; VII 525a–534e
:original_id: Stephanus Republic VI 509d–511e; VII 525a–534e
:folio: Republic VI 509d–511e; VII 525a–534e

.. _republic-notes:

====================================================================================================
Unit III — Republic VI–VII: The Divided Line, Dianoia & the Quadrivium — Critical Commentary & Notes
====================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Republic VI 509d–511e; VII 525a–534e

.. picture:: /_static/figures/republic_divided_line.svg
   :alt: Republic VI–VII: The Divided Line, Dianoia & the Quadrivium
   :caption: The Divided Line of Republic VI 509d–511e: cutting [A, E] at C and each realm in the same ratio 1 : r proves identically that sensible Pistis (/ B C /) equals mathematical Dianoia (/ C D /) as geometric mean ordinate B G between Eikasia (/ A B /) and Noesis (/ D E /).

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_divided_line`` and ``verify_divided_line_identity`` (see :doc:`/demos/index`), Socrates' double proportional section (`509d6–8`) is proved symbolically over an arbitrary ratio :math:`r > 0` and constructed by compass and straightedge under the canonical Academic **Golden Section** (:math:`r = \phi = \frac{1+\sqrt{5}}{2}`, :cite:`Elements II.11 & VI.30 <euclid:II.11>`):

- Let :g:`A B <divided-line:/ A B />` (:term:`eikasia <eikasia>`) have unit measure :math:`1`, and let :math:`AB : BC = AC : CE = CD : DE = 1 : r`. Then:

  .. math::

     |AB| = 1, \quad |BC| = r, \quad |AC| = 1 + r, \quad |CE| = r(1 + r), \quad |CD| = r, \quad |DE| = r^2.

- Therefore **for every ratio** :math:`r > 0`, the middle segments :g:`B C <divided-line:/ B C />` (:term:`pistis <pistis>`) and :g:`C D <divided-line:/ C D />` (:term:`dianoia <dianoia>`) satisfy :eq:`exact equality <divided-line:/ B C / = divided-line:/ C D />` :math:`|BC| = |CD| = r`, and each is the **geometric mean** between the extreme segments :g:`A B <divided-line:/ A B />` and :g:`D E <divided-line:/ D E />`, realized geometrically by erecting ordinate :g:`B G <divided-line:/ B G />` to semicircle :g:`(M, C) <divided-line:( M C )>` (:cite:`Elements VI.13 <euclid:II.14>`):

  .. math::

     Q(B, G) = Q(B, C) = Q(C, D) = Q(A, B) \cdot Q(D, E)^{1/2\text{ in length}} \implies |BG|^2 = |AB| \cdot |DE| = r^2.

- Under the **Golden Ratio** :math:`r = \phi` (:math:`\phi^2 = \phi + 1`), an additional self-similar harmony emerges: the Visible Realm :g:`A C <divided-line:/ A B C />` (:math:`1 + \phi = \phi^2`) equals pure :term:`noēsis <noesis>` :g:`D E <divided-line:/ D E />` (:math:`\phi^2`), making both :math:`(A, B, C)` and :math:`(C, D, E)` golden sections (:g:`golden range <divided-line:/ A C D E />`)!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **509d7–8 — ἀνὰ τὸν αὐτὸν λόγον**: :person:`Jowett <jowett>` translates *'in the same ratio'*, which strictly entails :math:`|BC| = |CD|`. Ancient and modern commentators (:person:`Proclus <proclus>`, Plutarch *Platonic Questions* III) noted that equality of the two middle sub-segments is not an embarrassing accident, but the mathematical seal of Plato's doctrine at `510b4–8`: *dianoia* uses as **images** (*ὡς εἰκόσιν χρωμένη*) the very physical objects imitated by shadows in the visible realm!
- **510c3–5 — ὑποθέμενοι τό τε περιττὸν καὶ τὸ ἄρτιον καὶ τὰ σχήματα καὶ γωνιῶν τριττὰ εἴδη**: Literally *'hypothesizing the odd and the even and the figures and three species of angles'*. The 'three species of angles' are right, obtuse, and acute (:cite:`Elements I, Defs. 10–12 <euclid:I.def.4>`), proving that pre-Euclidean Academic handbooks already opened with parallel arithmetic and geometric *hypotheseis*.
- **510d7–8 — τοῦ τετραγώνου αὐτοῦ ἕνεκα τοὺς λόγους ποιούμενοι καὶ διαμέτρου αὐτῆς**: Literally *'making their arguments for the sake of the Square itself and the Diagonal itself, not the one they draw'*—a direct echo of *Meno* `85b`!
- **528b1–3 — μετὰ ἐπίπεδον… ἐν περιφορᾷ ὂν ἤδη στερεὸν λαβόντες, πρὶν αὐτὸ καθ’ αὑτὸ λαβεῖν**: Socrates corrects his own initial sequence (`plane geometry -> astronomy`) because astronomy treats **solid body already in revolution** before investigating **three-dimensional solid in itself** (*ἡ τῶν κύβων αὔξη καὶ τὸ βάθους μετέχον*, `528b3`). Within one generation of this passage, :person:`Theaetetus <theaetetus>` and :person:`Eudoxus <eudoxus>` created the rigorous stereometry preserved in :cite:`Elements Books XI–XIII <euclid:XIII.13>`.

III. Reception & Sister-Corpus Civic-Arithmetic Locus (*Laws* V 737e–738b)
--------------------------------------------------------------------------

- **Proclus** (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 10–11, 29–32; ``plato:rep:VI.510b-511d``, ``VII.525a-534e``): Grounds the entire Neoplatonic ontology of *dianoia* and imaginative projection (*probolē* into geometric matter) in Republic VI–VII.
- **Hoenen & Civic Arithmetic** (``plato:rep:VI.510c``, ``VII.532c``, ``VII.533c``, and ``plato:leges:737e-738b``, ``738a``): In *De Noetica Geometriae* Cap. IV, :person:`Hoenen <hoenen>` pairs Republic VII's pure arithmetic (`525a–526c`) with Plato's remarkable divisor theorem in *Laws* V `737e–738b`, where the Athenian Stranger selects **5,040** (:math:`= 7! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 \cdot 6 \cdot 7 = 2^4 \cdot 3^2 \cdot 5 \cdot 7`) for civic land allotments because it possesses :math:`(4+1)(2+1)(1+1)(1+1) = 60` total divisors (`59` proper quotients excluding itself) and is evenly divisible by **every integer from 1 to 10** (and even by `12`, while `5,040 - 2 = 5,038 = 11 × 458` restores divisibility by `11`).

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit III** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
