:navigation: header
:order: 5

.. _mission:

=======
Mission
=======

.. rubric:: Recovering the Academy's Architectural Blueprint of Geometry, Proportion & Noetic Ascent

``geometor/plato`` (*Loci Mathematici et Geometrici*) anchors the fourth-century Athenian fountainhead of the **GEOMETOR** historical and constructive canon. Over the portal of the Academy (c. 387 BC) stood the celebrated maxim *Ἀγεωμέτρητος μηδεὶς εἰσίτω* ("Let no one ignorant of geometry enter"). Within its precincts, :person:`Plato of Athens <plato>` united :person:`Pythagorean <pythagoras>` harmonic ratio theory with :person:`Theodorus's <theodorus>` and :person:`Theaetetus's <theaetetus>` investigations of quadratic irrationals and :person:`Eudoxus's <eudoxus>` general theory of proportion—creating the intellectual crucible out of which :person:`Euclid's <euclid>` thirteen books of *Elements* emerged.

Why GEOMETOR Needs Plato
------------------------

Across six existing editions and symbolic engines in GEOMETOR, **58 distinct ``plato:*`` citation declarations** converge upon seven dialogues:

1. **The Genesis & Telos of Euclid's *Elements*** (``geometor/euclid`` & ``geometor/elements`` — **21 citations**):
   In :cite:`The Thirteen Books of Euclid's Elements <heath:euclid:1926>`, :person:`Sir Thomas Heath <heath>` continually turns to Plato to establish pre-Euclidean mathematical terminology and method: figure as :term:`limit of solid <schema>` (*Meno* ``76a`` :math:`\rightarrow` *Elements* I, Defs. 13–14 & XI, Def. 2), doubling the square by the :term:`diagonal <diametros>` (*Meno* ``82b–85b`` :math:`\rightarrow` I.47 & X.9), elliptic :term:`application of areas <parateinein>` from hypothesis (*Meno* ``86e–87b`` :math:`\rightarrow` VI.27–28), :person:`Theodorus's <theodorus>` and :person:`Theaetetus's <theaetetus>` :term:`powers <dynamis>` (*Theaetetus* ``147d–148b`` :math:`\rightarrow` X, Defs. 1–4 & X.9), optical straightness (*Parmenides* ``137e`` :math:`\rightarrow` I, Def. 4), solid geometry's program (*Republic* VII ``528a–d`` :math:`\rightarrow` XI–XII), and the five cosmic solids (*Timaeus* ``53c–56c`` :math:`\rightarrow` XIII.13–18).
2. **Proclus's Neoplatonic Philosophy of Geometry** (``geometor/proclus`` — **15 citations**):
   In :cite:`In Primum Euclidis Elementorum Librum Commentarii <proclus:in-euclidem>`, :person:`Proclus Diadochus <proclus>` constructs his entire ontology of mathematical objects from four Platonic pillars: :term:`Limit <peras>` and :term:`Unlimited <apeiron>` (*Philebus* ``16c–26d``), the middle ontological station of :term:`discursive understanding <dianoia>` on the Divided Line (*Republic* VI ``509d–511e``), :term:`recollection <anamnesis>` awakened through diagrams (*Meno* ``82b–85d``), and the cosmic polyhedra as the *telos* of the *Elements* (*Timaeus* ``53c–56c``).
3. **Aristotle's Logic of Hypotheses & Mathematical Intermediates** (``geometor/aristotle`` — **8 citations**):
   :person:`Aristotle's <aristotle>` *Posterior Analytics* opens by resolving *Meno*'s paradox (``71a29``), contrasts demonstrative axioms with unexamined mathematical :term:`hypotheses <hypothesis>`, preserves Plato's doctrine of immutable mathematical intermediates (*Metaphysics* A.6 ``987b14–18``), and debates the planar-triangle physics of *Timaeus* ``53c–56c`` (*De Caelo* III.7–8).
4. **Renaissance Divine Proportion & Scholastic Noetics** (``geometor/pacioli`` — **9 citations**; ``geometor/hoenen`` — **5 citations**):
   :person:`Fra Luca Pacioli <pacioli>` builds *De Divina Proportione* (1509) directly around *Timaeus*'s geometric :term:`bond <desmos>` and five regular bodies, while :person:`Fr. Peter Hoenen, S.J. <hoenen>` (*De Noetica Geometriae*, 1954) invokes *Meno*'s diagonal inquiry and *Republic*'s Divided Line as perennial proof that geometric necessity is grasped by intellectual insight into concrete configurations rather than blind formalist manipulation.

Editorial & Symbolic Principles
-------------------------------

* **100% Verbatim Public-Domain Sources**: Every Greek passage is parsed directly from :person:`John Burnet's <burnet>` Oxford Classical Text (*Platonis Opera*, 1900–1907), synchronized by Stephanus page and section (``a–e``) with :person:`Benjamin Jowett's <jowett>` 3rd revised English edition (1892) and audited via SHA-256 digests in ``resources/loci_mathematici/sources_manifest.json``.
* **Corrective Mathematical Philology**: Where Jowett's literary Victorian prose paraphrases technical Greek mathematical expressions—such as rendering ``τρίγωνον`` as "figure" at *Meno* ``87a`` or compressing ``δυνάμει τριπλάσιον`` ("triple in square power", i.e. :math:`Q = 3`) at *Timaeus* ``54b``—the **Critical Notes** track supplies verbatim Greek mathematical translations and exact algebraic proofs.
* **Strict Content / Code Separation**: The 4-track Book Codex (:doc:`/loci_mathematici/index`) contains zero embedded Python scripts, preserving pure philological and philosophical integrity while linking to 100% exact SymPy & Rational Trigonometry models in ``src/geometor/plato/`` and :doc:`/demos/index`.
