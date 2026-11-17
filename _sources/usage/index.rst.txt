:navigation: header
:order: 20
:nav_title: Usage

.. _plato-usage:

==================
Using This Edition
==================

.. rubric:: Interactive Reader's Guide to the Digital Scriptorium Edition of Plato's Mathematical Dialogues

Welcome to the GEOMETOR critical edition of **Mathematical & Geometric Dialogues** (*Loci Mathematici et Geometrici*). This digital edition is designed for deep mathematical reading, polytonic Greek philology, and exact symbolic synthesis across Plato's mathematical dialogues. Below are the key interactive features available throughout the site.

1. Synchronized Reading Tracks
------------------------------

Every unit in the Book Codex provides up to four synchronized reading tracks accessible directly from the chapter header navigation bar:

* **English (Primary Translation)**: Benjamin Jowett's public-domain 3rd revised Oxford translation (1892), segmented to exact Stephanus ``a–e`` milestones and enhanced with calibrated vector figures.
* **Greek (Burnet OCT, ``-el``)**: Verbatim polytonic Greek from John Burnet's five-volume Oxford Classical Text critical edition (*Platonis Opera*, 1900–1907), parsed from Perseus Canonical GreekLit TEI-XML witnesses.
* **Summary (Structural Synopsis)**: Argumentative architecture, Stephanus overview tables, deductive progression, and dialogue context.
* **Critical Notes (Scholarly Commentary)**: Interactive ``.euclid-graphic`` SVG diagrams, literal mathematical philology correcting 19th-century literary paraphrases, and reception across Euclid, Proclus, Aristotle, Pacioli, and Hoenen.

Use the track switcher in the chapter header bar to toggle seamlessly between perspectives while preserving your reading position.

2. Primary-Source Folio Milestones
----------------------------------

Every passage is calibrated to universal Stephanus pagination:

* **Marginal Folio Badges**: Marginal milestone pills (e.g., ``[Meno 75d]``, ``[Theaet. 147d]``, ``[Rep. 509d]``, ``[Tim. 35b]``) mark the five lettered subdivisions (``a``, ``b``, ``c``, ``d``, ``e``) of Henri Estienne's 1578 Geneva edition (*Henricus Stephanus*).
* **Header Folio Indicator**: The top metadata bar identifies the active dialogue, Stephanus section range, and canonical identifier.
* **Stephanus Cross-Reference Anchors**: Explicit anchors (such as ``#stephanus-meno-82b``) enable direct deep linking across the GEOMETOR ecosystem.

3. Interactive Diagrams & Deductive Links
-----------------------------------------

The edition features six calibrated, theme-adaptive ``.euclid-graphic`` SVG vector plates:

* **Geometric Hover Cards (``:g:``)**: Hovering over or clicking a geometric symbol (e.g., :g:`ABCD <meno-diag:< A B C D >>`, :g:`[ B D ] <meno-diag:[ B D ]>`) highlights the corresponding geometric element in the diagram with coordinate and construction details.
* **Mathematical Equations (``:eq:``)**: Display formatted LaTeX typography with interactive term breakdowns.
* **Deductive Justifications (``:just:``)**: Citations to Euclidean definitions or Platonic hypotheses provide direct cross-references.

4. Full-Text Search with In-Page Highlighting
---------------------------------------------

The global search box in the sidebar provides instantaneous full-text search across all dialogues, apparatus tables, and commentary:

* Search queries automatically append `?highlight=` parameters to destination URLs.
* Matched terms are highlighted directly within the dialogue text, Greek apparatus, and scholia for immediate discovery.

5. Categories, Tags & Collection Views
--------------------------------------

Document collections throughout the site (such as the :doc:`Development Log <../log/index>`) support rich viewing modes:

* **Cards View**: Grid of entry cards with metadata badges and timestamps.
* **Banners View**: Wide banner layout for extended narrative overviews.
* **List View**: Dense tabular listing for fast scanning.
* **Taxonomy Facets**: Filter by topic tags (e.g., `meno`, `theaetetus`, `republic`, `timaeus`, `harmonics`).

6. People, Bibliography & Glossary Tooltips
-------------------------------------------

* **People (``:person:``)**: Historical figures and dialogue interlocutors (such as :person:`Plato of Athens <plato>`, :person:`Socrates <socrates>`, :person:`Theaetetus <theaetetus>`, :person:`Timaeus <timaeus>`, :person:`John Burnet <burnet>`, and :person:`Benjamin Jowett <jowett>`) display rich biographical hover cards linking to the :doc:`People Register </people/index>`.
* **Citations (``:cite:``)**: Inline citations link to critical editions and primary witnesses in the :doc:`Bibliography </bibliography>`.
* **Technical Terms (``:term:``)**: Platonic Greek mathematical terms (such as :term:`dynamis <dynamis>`, :term:`dianoia <dianoia>`, :term:`peras <peras>`, :term:`analogia <analogia>`, and :term:`schema <schema>`) link to the :doc:`Technical Glossary </glossary>`.
* **Theme Switching**: Toggle between Light and Dark themes via the header button to suit your reading environment.

7. Command-Line & Python API
----------------------------

The ``geometor-plato`` CLI and Python package provide tools for exact symbolic SymPy modeling, Rational Trigonometry verification, and apparatus management.

CLI Usage:

.. code-block:: bash

   # Verify 100% exact symbolic precision and SHA-256 witness checksums
   geometor-plato verify

   # Display summary of all 6 units, passages, and figures
   geometor-plato summary

   # Display exact diatonic frequencies of the 34-pitch Timaeus World-Soul scale
   geometor-plato scale

   # Recompile apparatus JSON files
   geometor-plato compile

Python API Example:

.. code-block:: python

   from geometor.plato.constructions import construct_meno_diagonal_doubling
   from geometor.plato.harmonics import build_timaeus_scale

   # Construct exact SymPy model of Socrates' diagonal doubling (zero floats)
   model = construct_meno_diagonal_doubling()
   print(f"Constructed Meno model with {len(model)} geometric elements.")

   # Build the 34-pitch Timaeus World-Soul scale
   gamut = build_timaeus_scale()
   print(f"Generated {len(gamut.pitches)} diatonic pitches (Crantor base {gamut.base_multiplier}).")
