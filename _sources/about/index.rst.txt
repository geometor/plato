:navigation: header
:order: 20
:nav_title: About

.. _about:
.. _about-index:

About
=====

.. rubric:: Extracting Historical Semantic Knowledge & Repurposing It for Exact Symbolic Reasoning

About This Edition
------------------

``geometor/plato`` (*Loci Mathematici et Geometrici*) reconstructs the foundational mathematical and geometric passages across seven pivotal dialogues of :person:`Plato of Athens <plato>` (c. 428–347 BC)—the intellectual crucible of the fourth-century Athenian Academy. Over the portal of the Academy stood the celebrated maxim *Ἀγεωμέτρητος μηδεὶς εἰσίτω* ("Let no one ignorant of geometry enter"). Within its precincts, Plato united Pythagorean harmonic ratio theory with Theodorus's and Theaetetus's investigations of quadratic irrationals and Eudoxus's general theory of proportion, forging the philosophical and axiomatic foundations from which Hellenistic mathematics arose.

The implicit architecture of these dialogues—comprising eleven primary mathematical loci across *Meno*, *Theaetetus*, *Republic*, *Timaeus*, *Parmenides*, *Philebus*, and *Laws*—is extracted into addressable semantic elements across four synchronized tracks powered by ``photon-platform/publish``. Every unit coordinates verbatim English translations segmented to canonical Stephanus ``a–e`` folios, verbatim polytonic Greek from John Burnet's Oxford Classical Texts, deductive structural summaries, and philological critical notes equipped with interactive calibrated ``.euclid-graphic`` SVG diagrams and exact algebraic proofs.

This digital codex anchors **58 cross-corpus Platonic citations** across sister GEOMETOR repositories: establishing the pre-Euclidean terminology of limits, diagonals, and powers in :person:`Euclid's <euclid>` *Elements* (``geometor/euclid`` & ``geometor/elements``); providing the ontological framework of Limit (*peras*), Unlimited (*apeiron*), and discursive understanding (*dianoia*) in :person:`Proclus Diadochus's <proclus>` *Commentary* (``geometor/proclus``); framing demonstrative hypotheses and mathematical intermediates in :person:`Aristotle's <aristotle>` *Analytics* and *Metaphysics* (``geometor/aristotle``); and inspiring the regular polyhedral cosmologies of :person:`Fra Luca Pacioli's <pacioli>` *De Divina Proportione* (``geometor/pacioli``) and :person:`Fr. Peter Hoenen S.J.'s <hoenen>` *De Noetica Geometriae* (``geometor/hoenen``).

The GEOMETOR Mission
--------------------

The GEOMETOR project, initiated and directed by **phi ARCHITECT**, is dedicated to the complete digital renaissance and computational re-grounding of classical geometry and axiomatic thought. The mission advances across three foundational pillars:

1. **Extracting Historical Semantic Knowledge**: Moving beyond passive page scans, static PDFs, and raw OCR to recover the living deductive structure of 2,300+ years of geometric, axiomatic, and philosophical treatises. GEOMETOR elevates historical prose, marginal scholia, primary-source folios (via ``publish folio`` directives), and calibrated Ink-to-Vector ``.euclid-graphic`` diagrams into structured, machine-addressable semantic graphs. Each proposition, enunciation, step, hypothesis, and proof is rendered uniquely identifiable, computationally navigable, and interoperable across the entire historical canon.
2. **Exact Symbolic Grounding (``geometor.model``)**: Anchoring geometric constructions and spatial relations in 100% exact symbolic algebra via `SymPy` and Norman J. Wildberger's Rational Trigonometry invariants (quadrance, spread, cross-ratio). By operating strictly over exact algebraic number fields rather than floating-point approximations, GEOMETOR eliminates rounding degradation, preserves absolute mathematical truth, and guarantees that every geometric demonstration is provably exact.
3. **Repurposing Knowledge Across Mediums**: Re-deploying extracted semantic and algebraic structures across synchronized multi-track **Book Codices** and accessible EPUB 3 editions (powered by ``photon-platform/publish``), computable deductive canons (``geometor.elements``, ``geometor.etc``, ``geometor.pappus``, ``geometor.divine``), interactive SVG exploratory laboratories (``geometor.explorer``), ultra-high-definition visual broadcasts, and neuro-symbolic program synthesis (``geometor.seer``) across `geometor.com <https://geometor.com>`_.

Sources, Provenance & Methodology
---------------------------------

This edition adheres to rigorous Digital Scriptorium archival standards and strict separation of textual witness from computational model:

* **Greek Textual Witness**: Verbatim polytonic Greek text is drawn from :person:`John Burnet's <burnet>` five-volume critical edition, *Platonis Opera* (Oxford Classical Texts, Clarendon Press, 1900–1907), parsed from Perseus Digital Library Canonical GreekLit TEI-XML witnesses.
* **English Translation**: Verbatim English text is drawn from the public-domain 3rd revised edition (Clarendon Press, 1892) of :person:`Benjamin Jowett <jowett>` (*The Dialogues of Plato*), audited against Project Gutenberg witnesses with editorial corrections of Victorian literary paraphrases in the critical apparatus.
* **Stephanus Canonical Pagination**: All passages are anchored to Henri Estienne's (*Henricus Stephanus*) canonical 1578 Geneva Greek-Latin edition, generating deterministic ``.. folio::`` anchors (e.g. ``#stephanus-meno-82b``) for seamless deep linking.
* **Cryptographic Provenance**: Every staged source file in ``resources/loci_mathematici/sources/`` is audited by byte length and SHA-256 digest in ``resources/loci_mathematici/sources_manifest.json``.
* **Strict Content / Code Separation**: The 4-track Book Codex contains zero executable code, maintaining scholarly philological purity while linking to exact SymPy and Rational Trigonometry models in ``src/geometor/plato/`` and the accompanying symbolic demonstrations.

* :doc:`Burnet's Oxford Classical Text (1900–1907), Jowett (1892) & Stephanus Pagination <burnet-and-jowett>`

.. toctree::
   :maxdepth: 1
   :hidden:

   burnet-and-jowett
