:layout: book
:type: notes
:title: Incommensurability — Notes
:canonical_id: Laws VII, 817e–820d
:folio: Laws 817e
:tracks: English: index | Greek (Burnet OCT): greek | Summary: summary | Notes: notes

.. _laws-817e-820d-notes:
.. _foundations-notes:

=======================================================
Incommensurability — Critical Commentary & Notes
=======================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Laws VII 817e–820d

.. picture:: /_static/figures/foundations_peras_compass.svg
   :alt: Compass (Tornos), Optical Straight Ray (Kanon) & Three-Dimensional Incommensurability
   :caption: Compass (Tornos), Optical Straight Ray (Kanon) & Three-Dimensional Incommensurability: circle (O, C) of equal radii Q = 1 (Parm. 137e, Phil. 51c), optical diameter [A, O, C], plane diagonal O D (Q = 2), and unfolded cube diagonal O E (Q = 3, Laws VII 819d–820c).

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_compass_and_peras`` (see :doc:`/demos/index`), the three foundational motifs of *Parmenides*, *Philebus*, and *Laws* VII are unified in a single compass-and-straightedge plate (`foundations_peras_compass.svg`):

1. **Equidistant Circle & Optical Straight Line (*Parmenides* 137e, 145b)**:

   - Circle :g:`(O, C) <foundations-peras:( O C )>` centered at :g:`O <foundations-peras:O>` :math:`= (0,0)` exhibits :eq:`equal radial quadrances <foundations-peras:/ O C / = foundations-peras:/ O A />` :math:`Q(O, A) = Q(O, C) = Q(O, B) = 1` ('that whose extremes are everywhere equally distant from the middle', `137e1–3`, verbatim ancestor of :cite:`Euclid Elements I, Def. 15 <euclid:I.def.4>`).
   - Collinear diameter :g:`A O C <foundations-peras:[ A C ]>` exhibits Plato's **optical straightness** (:term:`epiprosthēsis <epiprosthesis>`, `137e3–4`): looking from :g:`A <foundations-peras:A>` toward :g:`C <foundations-peras:C>`, midpoint :g:`O <foundations-peras:O>` blocks (*ἐπίπροσθεν*) both extremes—bridging Euclidean geometry and Euclidean *Optics*!

2. **Compass (*Tornos*) & Straightedge (*Kanōn*) Pure Beauty (*Philebus* 51c)**:

   - Erecting perpendicular radius :g:`O B <foundations-peras:/ O B />` by :cite:`I.11 <euclid:I.11>` and completing unit square ``OCDB`` yields plane diagonal :g:`O D <foundations-peras:/ O D />` of exact quadrance :math:`Q(O, D) = 1 + 1 = 2`.

3. **Three-Dimensional Incommensurability Triad (*Laws* VII 819d–820c)**:

   - Erecting a unit third-dimensional edge perpendicular to :g:`O D <foundations-peras:/ O D />` at :g:`D <foundations-peras:D>` yields the unfolded **cube space diagonal** :g:`O E <foundations-peras:/ O E />` of exact quadrance:

     .. math::

        Q(O, C) = 1 \;(\text{length } 1), \quad Q(O, D) = 2 \;(\text{plane } \sqrt{2}), \quad Q(O, E) = 3 \;(\text{solid } \sqrt{3}).

   - Pairwise ratios :math:`1 : \sqrt{2}`, :math:`1 : \sqrt{3}`, and :math:`\sqrt{2} : \sqrt{3}` (:math:`Q_D / Q_E = 2/3`, non-square!) prove that unit length, square diagonal, and cube diagonal are **mutually incommensurable** across all three pairs—illustrating the Athenian Stranger's shock (`819e–820a`) that educated Greeks falsely suppose length, breadth, and depth to be universally commensurable!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **Parmenides 137e3–4 — οὗ ἂν τὸ μέσον ἀμφοῖν τοῖν ἐσχάτοιν ἐπίπροσθεν ᾖ**: :person:`Jowett <jowett>` translates *'that of which the middle intercepts the view of the extremes'*. As :person:`Heath <heath>` (:cite:`Euclid Vol. I, pp. 165–166 <heath:euclid:1926>`; ``plato:parm:137E``) and :person:`Proclus <proclus>` (:cite:`Friedlein 109.21 <proclus:in-euclidem>`; ``plato:parmenides:137e``) observe, Euclid deliberately replaced Plato's optical *ἐπίπροσθεν* (which appeals to visual rays) with the purely intrinsic geometric definition *ἥτις ἐξ ἴσου τοῖς ἐφ’ ἑαυτῆς σημείοις κεῖται* ('a line which lies evenly with the points on itself', :cite:`I, Def. 4 <euclid:I.def.4>`), while retaining the optical principle as Postulate 1 of Euclid's *Optics*!
- **Philebus 25a7–b1 — ὁπόσα… ἀριθμὸν πρὸς ἀριθμὸν ἢ μέτρον πρὸς μέτρον**: Notice Plato's deliberate disjunction: **number to number** (*ἀριθμὸς πρὸς ἀριθμόν*, commensurable rational ratios of discrete arithmetic) **or measure to measure** (*μέτρον πρὸς μέτρον*, continuous geometric ratios encompassing incommensurable magnitudes via :person:`Eudoxus's <eudoxus>` Book V theory of proportion!).
- **Philebus 51c3–4 — εὐθύ τι λέγω… καὶ περιφερές, καὶ ἀπὸ τούτων δὴ τά τε τοῖς τόρνοις γιγνόμενα ἐπίπεδα καὶ στερεὰ καὶ τὰ τοῖς κανόσι καὶ γωνίαις**: Plato names the exact toolkit of constructive geometry: **τόρνος** (lathe/compass generating circles, cylinders, and spheres), **κανών** (straightedge), and **γωνία** (carpenter's/geometer's right-angle square).

III. Peripheral Sister-Corpus Optical & Axiom Loci Catalogued Here
------------------------------------------------------------------

Three peripheral sister-corpus citations in ``geometor/euclid`` and ``geometor/elements`` complement Unit VI's philosophy of measure and optical geometry:

- ``plato:laws:777D`` (*Laws* VI `777d`): Plato quotes as an old proverb *'if equals be added to unequals, the wholes become unequal'*—cited by Heath on Euclid Common Notion 3–4 as pre-Euclidean testimony to quantitative axioms.
- ``plato:rep:X.602c`` (*Republic* X `602c–603a`): A straight stick partially immersed in water appears bent to sense-perception, and concave/convex shading deceives sight; **numbering, measuring, and weighing** (*τὸ μετρεῖν καὶ ἀριθμεῖν καὶ ἱστάναι*) rescue the rational part of the soul from optical illusion.
- ``plato:sophist:235.d`` (*Sophist* `235d–236c`): Distinguishes **icastic art** (*εἰκαστική*), which preserves true invariant geometric proportions (*τὰς οἰκείας συμμετρίας*), from **phantastic perspective** (*φανταστική*), which alters upper vs. lower proportions in colossal statues to compensate for visual foreshortening (*scenographia*).

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit VI** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
