:layout: book
:type: notes
:title: The Divided Line — Notes
:canonical_id: Republic VI, 509d–511e
:folio: Rep. 509d
:tracks: English: index | Greek (Burnet OCT): greek | Summary: summary | Notes: notes

.. _republic-509d-511e-notes:
.. _republic-notes:

===========================================
The Divided Line — Critical Notes
===========================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Republic VI 509d–511e

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

III. Reception
--------------

- **Proclus** (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 10–11; ``plato:rep:VI.510b-511d``): Grounds the entire Neoplatonic ontology of *dianoia* and imaginative projection (*probolē* into geometric matter) in Republic VI.

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions live in ``src/geometor/plato/`` and :doc:`/demos/index`.
