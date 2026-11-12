.. _burnet-and-jowett:

===============================================================================
Burnet's Oxford Classical Text (1900–1907), Jowett (1892) & Stephanus Citations
===============================================================================

.. rubric:: Primary Textual Witness, Canonical ``a–e`` Folio Anchors & Cryptographic Provenance

Stephanus Pagination (Geneva, 1578)
-----------------------------------

All scholarly citations to :person:`Plato <plato>` across classical philology, history of mathematics, and the **GEOMETOR** ecosystem refer to the three-volume Greek-Latin edition printed in Geneva in 1578 by **Henri Estienne** (*Henricus Stephanus*, :cite:`Platonis opera quae extant omnia <stephanus:1578>`). Each page of Estienne's edition is divided into five vertical lettered sections (``a``, ``b``, ``c``, ``d``, ``e``) separating the Greek column from Jean de Serres's Latin translation:

* **Volume I**: *Euthyphro*, *Apology*, *Crito*, *Phaedo*, *Theaetetus* (``142a–210d``), *Sophist*, *Statesman*, *Cratylus*, *Parmenides* (``126a–166c``), *Philebus* (``11a–67b``), *Symposium*, *Phaedrus* (with *Laws* in Volume II).
* **Volume II**: *Alcibiades I–II*, *Hipparchus*, *Rivals*, *Theages*, *Charmides*, *Laches*, *Lysis*, *Euthydemus*, *Protagoras*, *Gorgias*, *Meno* (``70a–100b``), *Hippias Major & Minor*, *Ion*, *Menexenus*, *Clitophon*, *Republic* I–X (``327a–621d``), *Laws* I–XII (``624a–969d``), *Epinomis*.
* **Volume III**: *Timaeus* (``17a–92c``), *Critias*, *Minos*, *Epistles*.

In ``geometor/plato``, every Stephanus transition in the Greek text emits a synchronized ``.. folio::`` directive and explicit ``.. _stephanus-<dialogue>-<sec>:`` cross-reference anchor (for example ``#stephanus-meno-82b``, ``#stephanus-theaetetus-147d``, ``#stephanus-republic-509d``, ``#stephanus-timaeus-35b``, ``#stephanus-timaeus-53c``), enabling deterministic deep links from ``resources/concordance.json`` and sister repositories.

John Burnet's Oxford Classical Text (1900–1907)
-----------------------------------------------

The **Greek (Burnet OCT)** track (``-el.rst``) stages verbatim polytonic Greek from :person:`John Burnet's <burnet>` five-volume Clarendon Press critical edition (:cite:`Platonis Opera <burnet:opera:1900>`), parsed directly from the CC-BY-SA / public-domain Perseus Digital Library Canonical GreekLit TEI-XML witnesses stored in ``resources/loci_mathematici/sources/el/``:

* ``tlg0059.tlg024.burnet_oct.xml`` — *Meno* (Tomus III, 1903)
* ``tlg0059.tlg006.burnet_oct.xml`` — *Theaetetus* (Tomus I, 1900)
* ``tlg0059.tlg030.burnet_oct.xml`` — *Respublica* (Tomus IV, 1902)
* ``tlg0059.tlg031.burnet_oct.xml`` — *Timaeus* (Tomus IV, 1902)
* ``tlg0059.tlg009.burnet_oct.xml`` — *Parmenides* (Tomus II, 1901)
* ``tlg0059.tlg010.burnet_oct.xml`` — *Philebus* (Tomus II, 1901)
* ``tlg0059.tlg034.burnet_oct.xml`` — *Leges* (Tomus V, 1907)

All editorial footnotes (``<note>``) and bibliographic tags (``<bibl>``) embedded in the TEI apparatus are stripped deterministically during compilation while preserving Burnet's speaker labels (``ΣΩ.``, ``ΜΕΝ.``, ``ΠΑΙ.``, ``ΘΕΑΙ.``, ``ΓΛ.``, ``ΤΙ.``, ``ΠΑΡ.``, ``ΠΡΩ.``, ``ΑΘ.``), polytonic breathing/accentuation, and exact ``<milestone unit="section" resp="Stephanus" n="..."/>`` boundaries.

Benjamin Jowett's 3rd Revised Edition (1892)
--------------------------------------------

The **English** track (``-en.rst``) stages the public-domain 3rd revised Oxford Clarendon Press translation (1892) of :person:`Benjamin Jowett <jowett>` (:cite:`The Dialogues of Plato <jowett:dialogues:1892>`) from verified Project Gutenberg plain-text witnesses in ``resources/loci_mathematici/sources/en/``:

* ``meno_jowett_pg1643.txt`` (*Meno*, PG #1643)
* ``theaetetus_jowett_pg1726.txt`` (*Theaetetus*, PG #1726)
* ``republic_jowett_pg55201.txt`` (*Republic*, PG #55201 — cleaned of marginal sidenotes, footnotes, and Beta Code Greek escapes)
* ``timaeus_jowett_pg1572.txt`` (*Timaeus*, PG #1572)
* ``parmenides_jowett_pg1687.txt`` (*Parmenides*, PG #1687)
* ``philebus_jowett_pg1744.txt`` (*Philebus*, PG #1744)
* ``laws_jowett_pg1750.txt`` (*Laws*, PG #1750)

Every staged file in ``resources/loci_mathematici/sources/`` is audited by byte length and SHA-256 digest in ``resources/loci_mathematici/sources_manifest.json`` and automatically verified by ``pytest`` and ``geometor-plato verify``.
