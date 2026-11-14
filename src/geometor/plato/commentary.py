"""Scholarly summaries, mathematical reconstructions, and Greek philology notes for Units I–VI.

Maintains strict separation of concerns: primary Codex companion tracks (``-summary.rst``
and ``-notes.rst``) contain zero embedded Python code blocks, pairing interactive
``:g:`` / ``:eq:`` SVG references, literal Greek philology (correcting Jowett's literary
paraphrases), and Euclidean/Neoplatonic/Scholastic reception with forward links to
``/demos/index``.
"""

from __future__ import annotations

__all__ = [
    "UNIT_EPIGRAPHS",
    "UNIT_NOTES",
    "UNIT_SUMMARIES",
]

UNIT_EPIGRAPHS: dict[str, tuple[str, str, str]] = {
    "meno": (
        "«ἔστιν γὰρ σχήματος τοῦτο ὃ μόνον τῶν ὄντων τυγχάνει χρώματι ἀεὶ ἑπόμενον… φαίην ἂν ἔγωγε πᾶν σχῆμα τοῦτο εἶναι, εἰς ὃ τὸ στερεὸν περαίνει· ὅπερ ἂν συλλαβὼν εἴποιμι στερεοῦ πέρας σχῆμα εἶναι.»",
        "“Every figure is that in which the solid terminates; which I may sum up by saying that figure is the limit of solid.”",
        "Meno 76a4–7",
    ),
    "theaetetus": (
        "«ὅσαι μὲν γραμμαὶ τὸν ἰσόπλευρον καὶ ἐπίπεδον ἀριθμὸν τετραγωνίζουσι, μῆκος ὡρισάμεθα, ὅσαι δὲ τὸν ἑτερομήκη, δυνάμεις, ὡς μήκει μὲν οὐ συμμέτρους ἐκείναις, τοῖς δ’ ἐπιπέδοις ἃ δύνανται.»",
        "“All lines that form in square an equilateral plane number we defined as length, while all that form an oblong number we defined as powers—incommensurable with the former in length, yet commensurable by the plane areas they have the power to form.”",
        "Theaetetus 148a9–b2",
    ),
    "republic": (
        "«ὥσπερ τοίνυν γραμμὴν δίχα τετμημένην λαβὼν ἄνισα τμήματα, πάλιν τέμνε ἑκάτερον τὸ τμῆμα ἀνὰ τὸν αὐτὸν λόγον, τό τε τοῦ ὁρωμένου γένους καὶ τὸ τοῦ νοουμένου…»",
        "“Take then a line cut in two into unequal segments, and cut each segment again according to the same ratio—both that of the visible genus and that of the intelligible…”",
        "Republic VI, 509d6–8",
    ),
    "timaeus-world-soul": (
        "«δεσμῶν δὲ κάλλιστος ὃς ἂν αὑτὸν καὶ τὰ συνδούμενα ὅτι μάλιστα ἓν ποιῇ, τοῦτο δὲ πέφυκεν ἀναλογία κάλλιστα ἀποτελεῖν.»",
        "“And the fairest of bonds is that which makes itself and the things bound together one to the utmost degree; and geometric proportion is by nature suited to accomplish this most nobly.”",
        "Timaeus 31c2–4",
    ),
    "timaeus-polyhedra": (
        "«τὰ δὲ τρίγωνα πάντα ἐκ δυοῖν ἄρχεται τριγώνοιν, μίαν μὲν ὀρθὴν ἔχοντος ἑκατέρου γωνίαν, τὰς δὲ ὀξείας· ὧν τὸ μὲν ἕτερον ἑκατέρωθεν ἔχει μέρος γωνίας ὀρθῆς πλευραῖς ἴσαις διῃρημένης, τὸ δ’ ἕτερον ἀνίσους ἄνισα μέρη νενεμημένης.»",
        "“All triangles derive their origin from two triangles, each having one right angle and two acute: one having on either side a half-right angle bounded by equal sides, the other unequal parts allotted to unequal sides.”",
        "Timaeus 53c8–d4",
    ),
    "foundations": (
        "«καὶ γὰρ εὐθύ γε, οἶμαι, ἐστὶν οὗ ἂν τὸ μέσον ἀμφοῖν τοῖν ἐσχάτοιν ἐπίπροσθεν ᾖ.»",
        "“For straight, I take it, is that of which the middle stands in front of both extremes.”",
        "Parmenides 137e3–4",
    ),
}

UNIT_SUMMARIES: dict[str, str] = {
    "meno": """
Architectural Thesis
--------------------

Unit I gathers the three foundational mathematical episodes of :person:`Plato's <plato>` *Meno*—the earliest surviving Greek text to stage an explicit geometric diagram step by step:

1. **Dialectical Definition of Figure (75d–76a)**: Before defining virtue, :person:`Socrates <socrates>` offers :person:`Meno <meno>` a model geometric definition: roundness (*strongylotēs*) is merely *a* figure, whereas universal :term:`figure <schema>` (*schēma*) is **the limit of solid** (*στερεοῦ πέρας*, :ref:`76a <stephanus-meno-76a>`).
2. **Anamnesis & Doubling the Square by the Diagonal (81e–85d)**: Answering Meno's eristic paradox of inquiry, Socrates summons an untutored household attendant and constructs the :math:`2 \\times 2` square :g:`ABCD <meno-diag:< A B C D >>` (:math:`Q = 4`). After exposing two false arithmetic intuitions—doubling the side to :g:`AE <meno-diag:/ A E />` (:math:`4 \\times 4 = 16`, :g:`AEFG <meno-diag:< A E F G >>`) and taking the sesquialter side :g:`AM <meno-diag:/ A M />` (:math:`3 \\times 3 = 9`, :g:`AMNP <meno-diag:< A M N P >>`)—Socrates draws the four :term:`diagonals <diametros>` :g:`BD <meno-diag:[ B D ]>`, :g:`BH <meno-diag:[ B H ]>`, :g:`HK <meno-diag:[ H K ]>`, and :g:`KD <meno-diag:[ K D ]>`, cutting each :math:`4`-foot square in half (:math:`2 + 2 + 2 + 2 = 8`) to enclose the exact double square :g:`BHKD <meno-diag:< B H K D >>`.
3. **Inquiry from Hypothesis & Application of Area (86e–87b)**: Pressed to ask whether virtue is teachable prior to knowing its essence, Socrates adopts the geometer's method of :term:`hypothesis <hypothesis>` (*ἐξ ὑποθέσεως*, :ref:`86e <stephanus-meno-86e>`): reducing the inscription of a triangular area inside a given circle to an elliptic :term:`application of area <parateinein>` along the diameter.

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 22 18 42 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **I.1 Definition of Figure**
     - ``75d–76a``
     - Genus vs. species; surface, solid (*stereon*), and :term:`limit <peras>` (*peras*).
     - :ref:`EN <stephanus-meno-75d>` · :ref:`EL <stephanus-el-meno-75d>`
   * - **I.2 Diagonal Doubling**
     - ``81e–85d``
     - Given square (:math:`Q=4`), refutation of :math:`Q=16` & :math:`Q=9`, aporia, and diagonal proof (:math:`Q=8`).
     - :ref:`EN <stephanus-meno-81e>` · :ref:`EL <stephanus-el-meno-81e>`
   * - **I.3 Geometric Hypothesis**
     - ``86e–87b``
     - Analytic reduction of circular inscription to elliptic application of areas (:cite:`Elements VI.28 <euclid:VI.28>`).
     - :ref:`EN <stephanus-meno-86e>` · :ref:`EL <stephanus-el-meno-86e>`
""".strip(),
    "theaetetus": """
Architectural Thesis
--------------------

In *Theaetetus* `147c–148b`, the young Athenian geometer :person:`Theaetetus <theaetetus>` offers :person:`Socrates <socrates>` the supreme model of universal scientific definition by recounting how he and young Socrates generalized a geometric lesson of :person:`Theodorus of Cyrene <theodorus>`:

1. **Theodorus's Case-by-Case Irrationality Proofs (147d)**: Theodorus drew diagrams (*ἔγραφε*) proving separately for squares of area :math:`3` square feet (:g:`O P3 <theodorus-spiral:/ O P3 />`) and :math:`5` square feet (:g:`O P5 <theodorus-spiral:/ O P5 />`) up to :math:`17` square feet (:g:`O P17 <theodorus-spiral:/ O P17 />`) that their sides are not :term:`commensurable <symmetros-asymmetros>` in length with the :math:`1`-foot unit (:g:`O P1 <theodorus-spiral:/ O P1 />`), coming to a halt (*ἐνέσχετο*) at :math:`17`.
2. **Partition of All Integers into Equilateral & Oblong (147e–148a)**: Recognizing that incommensurable powers are infinite in multitude, the boys partitioned every integer into two classes: **equilateral square numbers** (:term:`isos isakis <isos-isakis>`, :math:`n = k^2`, such as :math:`4, 9, 16`) and **oblong numbers** (:term:`promēkēs <promekes>`, non-square integers bounded by unequal factors).
3. **Dichotomy of Lengths (*Mēkē*) & Powers (*Dynameis*) (148a–b)**: Lines squaring to equilateral numbers—highlighted at :g:`P1 <theodorus-spiral:P1>`, :g:`P4 <theodorus-spiral:P4>`, :g:`P9 <theodorus-spiral:P9>`, and :g:`P16 <theodorus-spiral:P16>`—are defined as :term:`lengths <mekos>` (*μήκη*); lines squaring to oblong numbers are defined as :term:`powers <dynamis>` (*δυνάμεις*), commensurable not in linear measure but by the plane areas they have the power to generate, adding that the analogous distinction holds for **solids** (*καὶ περὶ τὰ στερεὰ ἄλλο τοιοῦτον*, i.e., cube roots :math:`\\sqrt[3]{n}`).

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 18 40 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **II.1 Theodorus's Diagram**
     - ``147c–147d``
     - Case-by-case irrationality of :math:`\\sqrt{3}, \\sqrt{5}, \\dots, \\sqrt{17}`.
     - :ref:`EN <stephanus-theaetetus-147c>` · :ref:`EL <stephanus-el-theaetetus-147c>`
   * - **II.2 Lengths & Powers**
     - ``147e–148b``
     - Universal number-theoretic criterion (:cite:`Elements X.9 <euclid:X.def.1>`) & extension to solids.
     - :ref:`EN <stephanus-theaetetus-147e>` · :ref:`EL <stephanus-el-theaetetus-147e>`
""".strip(),
    "republic": """
Architectural Thesis
--------------------

Unit III unites the two monumental architects of Western mathematical epistemology—Book VI's **Divided Line** (`509d–511e`) and Book VII's **Curriculum of the Five Mathematical Sciences & Dialectic** (`525a–534e`):

1. **The Divided Line & Geometric Equality of Middle Segments (VI, 509d–511e)**: :person:`Socrates <socrates>` instructs :person:`Glaucon <glaucon>` to cut a line :g:`AE <divided-line:/ A C D E />` unequally at :g:`C <divided-line:C>` into the Visible (:g:`AC <divided-line:/ A B C />`) and Intelligible, and to subdivide each realm **in the same ratio** (:math:`1 : r`). By pure algebraic necessity (:math:`AB : BC = CD : DE = AC : CE = 1 : r`), the sensible segment of :term:`pistis <pistis>` (:g:`BC <divided-line:/ B C />`) is :eq:`strictly equal <divided-line:/ B C / = divided-line:/ C D />` to the mathematical segment of :term:`dianoia <dianoia>` (:g:`CD <divided-line:/ C D />`), materialized by the geometric mean ordinate :g:`BG <divided-line:/ B G />` on semicircle :g:`(M, C) <divided-line:( M C )>`—reflecting the exact ontological law that geometry redeploys physical things of *pistis* as visible diagrams!
2. **Methodological Critique of Geometric Hypotheses (VI, 510c–511d)**: Geometers hypothesize the odd and even, the figures, and the three kinds of angles as self-evident without giving an account of them, using drawn squares and diagonals only to behold **the Square itself** and **the Diagonal itself** through :term:`dianoia <dianoia>`, whereas :term:`noēsis <noesis>` ascends without images to the :term:`unhypothetical principle <anhypotheton>`.
3. **The Five Sciences of the Quadrivium & the Lament on Stereometry (VII, 525a–534e)**: To turn the soul from becoming to eternal being (`525b–527b`), Socrates orders five ascending sciences: (i) :term:`Arithmetic & Logistic <arithmetike>` (`525a–526c`), (ii) Plane Geometry (`526c–527c`), (iii) :term:`Solid Geometry <stereometria>` (`528a–d`—inserting his prophetic lament that three-dimensional stereometry remains neglected and unguided by cities), (iv) Mathematical Astronomy (`528e–530c`), and (v) Pythagorean Harmonics of Ratios (`530d–531c`), crowned by :term:`Dialectic <dialektike>` (`531d–534e`).

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 18 40 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **III.1 The Divided Line**
     - ``VI, 509d–511e``
     - *Eikasia*, *pistis*, *dianoia*, *noēsis*; geometric hypotheses & diagrams.
     - :ref:`EN <stephanus-republic-509d>` · :ref:`EL <stephanus-el-republic-509d>`
   * - **III.2 Arithmetic & Geometry**
     - ``VII, 525a–528d``
     - Indivisible unit, plane geometry of eternal being, and neglected 3D stereometry (`528b`).
     - :ref:`EN <stephanus-republic-525a>` · :ref:`EL <stephanus-el-republic-525a>`
   * - **III.3 Astronomy, Harmonics & Dialectic**
     - ``VII, 528e–534e``
     - Kinematics of true ratios, critique of empirical harmonics, and *dialektikē* as coping-stone.
     - :ref:`EN <stephanus-republic-529a>` · :ref:`EL <stephanus-el-republic-529a>`
""".strip(),
    "timaeus-world-soul": """
Architectural Thesis
--------------------

In *Timaeus* `31b–36d`, :person:`Timaeus of Locri <timaeus>` presents the grandest proportional and harmonic synthesis of antiquity, constructing both the four-element body of the cosmos and the musical fabric of the World-Soul from exact rational and quadratic invariants:

1. **Single vs. Double Geometric Means (31b–32c)**: To bind fire and earth together, the Demiurge employs continuous :term:`geometric proportion <analogia>` (*ἀναλογία*), the fairest of :term:`bonds <desmos>`. Had the cosmos been a two-dimensional plane without depth, one mean proportional would have sufficed (:math:`a^2 : ab : b^2`, :cite:`Elements VIII.11 <euclid:VIII.11>`); because the cosmos is a three-dimensional solid, **two mean proportionals** are required (:math:`a^3 : a^2 b : a b^2 : b^3`, :cite:`Elements VIII.12 <euclid:VIII.11>`), placing air and water between fire and earth so that ``fire : air = air : water = water : earth``.
2. **Harmonic Division of the World-Soul (35a–36b)**: Slicing the mixed psychic substance into the geometric tetractys of doubles ``1, 2, 4, 8`` and triples ``1, 3, 9, 27`` (spanning four octaves plus a major sixth, :math:`27:1`), the Demiurge inserts into every interval the **harmonic mean** :math:`H = \\frac{2ab}{a+b}` (:g:`G H <timaeus-means:/ G H />`) and **arithmetic mean** :math:`A = \\frac{a+b}{2}` (:g:`O G <timaeus-means:/ O G />`), generating :term:`sesquialter <hemiolios>` fifths (:math:`3:2`), :term:`sesquitertian <epitritos>` fourths (:math:`4:3`), and :term:`epogdoic <epogdoos>` whole tones (:math:`9:8`), and filling every :math:`4:3` fourth with two :math:`9:8` tones plus the exact diatonic :term:`leimma <leimma>` **256 : 243**.
3. **Circles of the Same and the Different (36b–d)**: Splitting the calibrated harmonic strip lengthwise and bending the two bands into great circles intersecting like the letter **Chi** (:math:`\\mathrm{X}`, :g:`P Q <timaeus-means:[ P Q ]>` across equator :g:`A B <timaeus-means:/ A B />` on :g:`(O, B) <timaeus-means:( O B )>`), the Demiurge establishes the celestial equator (Same) and the ecliptic subdivided in the seven ratios ``1, 2, 3, 4, 8, 9, 27`` (Different).

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 18 40 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **IV.1 Cosmic Analogia**
     - ``31b–32c``
     - Plane (1 mean) vs. solid (2 means) proportion binding Fire, Air, Water, and Earth.
     - :ref:`EN <stephanus-timaeus-31b>` · :ref:`EL <stephanus-el-timaeus-31b>`
   * - **IV.2 World-Soul Gamut**
     - ``35a–36d``
     - Doubles & triples, arithmetic/harmonic means, ``9:8`` tone, ``256:243`` *leimma*, and :math:`\\mathrm{X}`-circles.
     - :ref:`EN <stephanus-timaeus-35a>` · :ref:`EL <stephanus-el-timaeus-35a>`
""".strip(),
    "timaeus-polyhedra": """
Architectural Thesis
--------------------

In *Timaeus* `53c–56c`, :person:`Plato <plato>` executes the boldest geometrical reduction in ancient natural philosophy: fire, air, water, and earth are not ultimate *stoicheia* ('not even syllables', `48b`), because all three-dimensional bodies are bounded by planar surfaces, every rectilinear plane surface resolves into triangles, and all triangles derive from **two elementary right-angled triangles** (:term:`stoicheia <stoicheion>`):

1. **The Two Elementary Right Triangles (53c–54b)**:
   - The **isosceles right triangle** (:math:`1 : 1 : \\sqrt{2}`, quadrances :math:`1, 1, 2`, spreads :math:`\\frac{1}{2}, \\frac{1}{2}, 1`), unique of its kind; four assemble around a central right-angle vertex to form each square face of the **Cube** (Earth).
   - The **fairest scalene right triangle** (:term:`hēmitrigōnon <hemitrigonon>`, :math:`1 : \\sqrt{3} : 2`, quadrances :math:`1, 3, 4`—*'having the greater leg triple in power of the lesser'*, `54b5`—and rational spreads :math:`\\frac{1}{4}, \\frac{3}{4}, 1`), formed by bisecting an equilateral triangle :g:`ABC <timaeus-triangles:< A B C >>` along its altitude :g:`C M3 <timaeus-triangles:/ C M3 />`.
2. **Six-Triangle Assembly of the Cosmic Equilateral Face (54d–55a)**: Six elementary :math:`1 : \\sqrt{3} : 2` right triangles—such as :g:`A M3 G <timaeus-triangles:< A M3 G >>` and :g:`B M3 G <timaeus-triangles:< B M3 G >>`—converge along their diagonals and short legs at centroid :g:`G <timaeus-triangles:G>` (:math:`X(2)`) to compose a single equilateral triangle :g:`ABC <timaeus-triangles:< A B C >>`.
3. **Generation & Transmutation of the Five Cosmic Polyhedra (54e–56c)**:
   - **Tetrahedron** (`4` equilateral faces = `24` scalenes) :math:`\\rightarrow` **Fire**
   - **Octahedron** (`8` equilateral faces = `48` scalenes) :math:`\\rightarrow` **Air**
   - **Icosahedron** (`20` equilateral faces = `120` scalenes) :math:`\\rightarrow` **Water**
   - **Cube** (`6` square faces = `24` isosceles right triangles) :math:`\\rightarrow` **Earth** (incommensurable with the :math:`\\sqrt{3}` family and therefore non-transmutable into fire/air/water)
   - **Dodecahedron** (`12` regular pentagonal faces, requiring :math:`\\mathbb{Q}(\\phi)`) :math:`\\rightarrow` **The Whole Cosmos** (`55c4–6`).

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 24 18 40 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **V.1 Elementary Triangles**
     - ``53c–54d``
     - Stereometric genesis; :math:`1:1:\\sqrt{2}` isosceles vs. :math:`1:\\sqrt{3}:2` half-equilateral (*triple in power*).
     - :ref:`EN <stephanus-timaeus-53c>` · :ref:`EL <stephanus-el-timaeus-53c>`
   * - **V.2 Five Cosmic Solids**
     - ``54d–56c``
     - 6-triangle equilateral face, 4-triangle square face, 5 regular solids, and transmutation equations.
     - :ref:`EN <stephanus-timaeus-54d>` · :ref:`EL <stephanus-el-timaeus-54d>`
""".strip(),
    "foundations": """
Architectural Thesis
--------------------

Unit VI gathers the late-Platonic axiomatic, ontological, aesthetic, and pedagogical foundations of geometry across *Parmenides*, *Philebus*, and *Laws* Book VII:

1. **Optical Straightness & Equidistant Roundness (*Parmenides* 137d–138a, 145a–b)**: In the First and Second Hypotheses of the *Parmenides*, :person:`Plato <plato>` gives the earliest preserved Greek definitions of **round/circular** (*that whose extremes are everywhere equally distant from the middle*, :g:`(O, C) <foundations-peras:( O C )>` with :eq:`equal radii <foundations-peras:/ O C / = foundations-peras:/ O A />` :g:`O C <foundations-peras:/ O C />` and :g:`O A <foundations-peras:/ O A />`) and **straight** (*that whose middle stands in front of both extremes*, :term:`epiprosthēsis <epiprosthesis>` along diameter :g:`A C <foundations-peras:[ A C ]>`).
2. **Limit (*Peras*), Unlimited (*Apeiron*) & Pure Constructive Beauty (*Philebus* 16c–26d, 51b–52c)**: In *Philebus* `16c–26d`, :person:`Socrates <socrates>` establishes :term:`Limit <peras>` (*πέρας*—the equal, double, and every exact ratio of number to number or measure to measure) and the :term:`Unlimited <apeiron>` (*ἄπειρον*—the indeterminate continuum of more and less) as the universal principles of mathematical order, Adopted verbatim by :person:`Proclus <proclus>` at the head of his *Euclid* commentary. At `51b–52c`, Socrates defines **pure, non-relative beauty**: surfaces and solids constructed cleanly by :term:`compass and straightedge <tornos-kanon>` (*τόρνοις… καὶ κανόσι*).
3. **Dimensional Incommensurability (*Laws* VII 817e–820d)**: In his final work, the :person:`Athenian Stranger <athenian-stranger>` mandates three liberal mathematical disciplines (arithmetic, metrics of line/surface/solid, and celestial kinematics) and castigates Greek education for assuming that length (:g:`O C <foundations-peras:/ O C />`, :math:`Q=1`), plane surface (:g:`O D <foundations-peras:/ O D />`, :math:`Q=2`), and solid depth (:g:`O E <foundations-peras:/ O E />`, :math:`Q=3`) are universally :term:`commensurable <symmetros-asymmetros>`.

Stephanus Overview
------------------

.. list-table::
   :header-rows: 1
   :widths: 26 18 38 18

   * - Section
     - Stephanus Span
     - Mathematical & Philosophical Argument
     - Tracks
   * - **VI.1–2 Parmenides Definitions**
     - ``137d–138a, 145a–b``
     - Round equidistance, optical straightness, and figure (*schēma*).
     - :ref:`EN <stephanus-parmenides-137d>` · :ref:`EL <stephanus-el-parmenides-137d>`
   * - **VI.3–4 Philebus Limit & Beauty**
     - ``16c–26d, 51b–52c``
     - *Peras* & *apeiron*; pure geometric beauty wrought by *tornos* and *kanōn*.
     - :ref:`EN <stephanus-philebus-16c>` · :ref:`EL <stephanus-el-philebus-16c>`
   * - **VI.5 Laws VII Incommensurability**
     - ``VII, 817e–820d``
     - Commensurable vs. incommensurable lengths, planes, and solids (:math:`1, \\sqrt{2}, \\sqrt{3}`).
     - :ref:`EN <stephanus-laws-817e>` · :ref:`EL <stephanus-el-laws-817e>`
""".strip(),
}

UNIT_NOTES: dict[str, str] = {
    "meno": """
I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_meno_diagonal_doubling`` (see :doc:`/demos/index`), Socrates' sand diagram (`82b–85b`) is modeled with 100% exact rational coordinates over :math:`\\mathbb{Q}` without introducing irrational square roots until linear magnitude is requested—directly vindicating Rational Trigonometry's primacy of **quadrance**:

- **Given Two-Foot Square** :g:`ABCD <meno-diag:< A B C D >>` (`82c–d`): Anchored at :g:`A <meno-diag:A>` :math:`= (0,0)` and :g:`B <meno-diag:B>` :math:`= (2,0)`, every side has quadrance :math:`Q(A,B) = 4`, enclosing area :math:`4` square feet.
- **First Refutation — Doubling the Side** (`82e–83c`): Extending :g:`A B <meno-diag:/ A B />` to :g:`E <meno-diag:E>` :math:`= (4,0)` produces the fourfold square :g:`AEFG <meno-diag:< A E F G >>` of quadrance :math:`Q(A,E) = 16` (composed of four :math:`4`-foot squares meeting at interior center :g:`C <meno-diag:C>` :math:`= (2,2)`).
- **Second Refutation — The Three-Foot Trial** (`83d–e`): Searching strictly between :math:`2` and :math:`4`, the attendant proposes the arithmetic midpoint :g:`M <meno-diag:M>` :math:`= (3,0)` (`sesquialter` :math:`3:2`), which generates square :g:`AMNP <meno-diag:< A M N P >>` of quadrance :math:`Q(A,M) = 9 \\neq 8`, bringing on the purifying **aporia** (`84a–c`).
- **Constructive Resolution via the Four Diagonals** (`84d–85b`): Drawing the four :term:`diagonals <diametros>` :g:`BD <meno-diag:[ B D ]>`, :g:`BH <meno-diag:[ B H ]>`, :g:`HK <meno-diag:[ H K ]>`, and :g:`KD <meno-diag:[ K D ]>` across the four sub-squares cuts each :math:`4`-foot square into two equal isosceles right triangles of area :math:`2`. The inscribed tilted square :g:`BHKD <meno-diag:< B H K D >>` therefore has exact area and side quadrance:

  .. math::

     Q(B, D) = Q(A, B) + Q(A, D) = 4 + 4 = 8 = 2 \\, Q(A, B).

**Socrates' Elliptic Application Hypothesis (86e–87b)**: As :person:`Sir Thomas Heath <heath>` demonstrated (:cite:`History of Greek Mathematics <heath:greek-math:1921>`, Vol. I, pp. 298–303), Socrates' famous geometric obscurity at `87a`—inscribing a given area :math:`C` as a triangle in a circle of diameter :math:`AB = d`—reduces to choosing a point :math:`X` on diameter :math:`AB` and erecting ordinate :math:`XY` to the circle so that rectangle :math:`AX \\cdot XY = C`. Since in the semicircle :math:`XY^2 = AX \\cdot XB`, squaring gives :math:`AX \\cdot XB = (C / AX)^2`, meaning rectangle :math:`AX \\cdot XY` is **applied** (:term:`parateinein <parateinein>`) along :math:`AB` while **falling short** (*ἐλλείπειν*) on :math:`XB` by a rectangle :math:`XB \\cdot XY` *similar* to the applied rectangle :math:`AX \\cdot XY` (:math:`AX : XY = XY : XB`)—an exact fourth-century instance of hyperbolic/elliptic application of areas (:cite:`Elements VI.28 <euclid:VI.28>`).

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **76a7 — στερεοῦ πέρας σχῆμα εἶναι**: :person:`Jowett <jowett>` translates *'figure is the limit of solid'*, faithfully preserving :person:`Burnet's <burnet>` technical pairing of :term:`stereon <stereon>` and :term:`peras <peras>`. Compare :cite:`Elements XI, Def. 2 <euclid:I.def.13>` (*στερεοῦ δὲ πέρας ἐπιφάνεια*, 'the extremity of a solid is a surface') and :cite:`I, Def. 14 <euclid:I.def.13>` ('a figure is that which is contained by any boundary or boundaries').
- **85b4 — διάμετρον ὄνομα, καλοῦσιν δὲ ταύτην οἱ σοφισταί**: Here *σοφισταί* denotes technical mathematical experts/professors rather than eristic rhetoricians; :term:`diametros <diametros>` means the diagonal of the square (preserved throughout :person:`Euclid <euclid>` and :person:`Aristotle <aristotle>`).
- **87a3–6 — παρὰ τὴν δοθεῖσαν αὐτοῦ γραμμὴν παρατείναντα ἐλλείπειν τοιούτῳ χωρίῳ οἷον ἂν αὐτὸ τὸ παρατεταμένον ᾖ**: Jowett renders loosely *'whether, if the figure be applied to the given line of the circle, it is deficient by another figure similar to that which is applied'*. Literally, *παρατείνειν παρὰ γραμμήν* is the technical Pythagorean-Academic idiom for **parabolic/elliptic application of an area along a given straight line** (*παραβολή / ἔλλειψις τῶν χωρίων*), later standardized by Euclid in Book VI and by Apollonius in naming the *parabola* and *ellipse*.

III. Reception in Aristotle, Euclid, Proclus & Hoenen
-----------------------------------------------------

- **Aristotle** (:cite:`Anal. Post. I.1, 71a29 <aristotle:anal-post>`; ``plato:meno``): Resolves Meno's dilemma by distinguishing universal pre-existent knowledge (*that every triangle has 2R*) from simultaneous recognition (*ἅμα ἐπαγόμενος*) that the drawn figure falls under the universal.
- **Proclus** (:cite:`In Euclidem, Friedlein 45.15–46.3 <proclus:in-euclidem>`; ``plato:meno:81e-85d``): Cites Socrates' questioning of the boy as proof that mathematical *logoi* reside substantially within the soul rather than being stamped from outside by sense-impressions.
- **Hoenen** (:cite:`De Noetica Geometriae <hoenen:noetica:1952>`, Cap. I & VII; ``plato:meno:82b-85b``): Highlights `82b–85b` as the locus classicus for **intellectual vision in the singular phantasm**: the boy counts neither decimal approximations of :math:`2\\sqrt{2} \\approx 2.828` nor syllogistic major premises, but beholds universal necessity (:math:`4 \\times \\frac{1}{2} \\times 4 = 8`) directly in the bisected grid.
""".strip(),
    "theaetetus": """
I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_theodorus_spiral`` and ``classify_theaetetus_powers`` (see :doc:`/demos/index`), :person:`Theodorus's <theodorus>` lesson (`147d`) is modeled by iterating pure Euclidean perpendicular erection (:cite:`I.11 <euclid:I.11>`) and unit compass transfer (:cite:`Post. 3 <euclid:elements>`):

- Starting from :g:`O <theodorus-spiral:O>` :math:`= (0,0)` and rational unit :g:`P1 <theodorus-spiral:P1>` :math:`= (1,0)` (:math:`Q(O, P_1) = 1`), each orthogonal unit leg :g:`P1 P2 <theodorus-spiral:/ P1 P2 />`, ..., :g:`P16 P17 <theodorus-spiral:/ P16 P17 />` satisfies :eq:`unit quadrance <theodorus-spiral:/ O P1 / = theodorus-spiral:/ P16 P17 />` :math:`Q(P_n, P_{n+1}) = 1` and exact perpendicularity :math:`\\overrightarrow{OP_n} \\perp \\overrightarrow{P_n P_{n+1}}`.
- By Pythagoras's Theorem (:cite:`Elements I.47 <euclid:I.47>`), the spoke quadrances step through every integer from :math:`1` to :math:`17`:

  .. math::

     Q(O, P_{n+1}) = Q(O, P_n) + Q(P_n, P_{n+1}) = n + 1 \\quad (1 \\le n \\le 16).

- **Why Did Theodorus Stop at 17 Square Feet?** (*μέχρι τῆς ἑπτακαιδεκαπόδος, ἐν δὲ ταύτῃ πως ἐνέσχετο*, `147d6`): Modern scholarship (:person:`Heath <heath>` :cite:`1921 <heath:greek-math:1921>`, :person:`Wilbur Knorr <heath>` :cite:`1975 <knorr:evolution:1975>`) highlights two converging reasons visible directly in our exact construction:
  1. **Geometric Self-Overlap**: Summing the interior angles :math:`\\sum_{k=1}^{16} \\arctan(1/\\sqrt{k}) \\approx 351.15^\\circ < 360^\\circ`, whereas adding the :math:`18`-foot triangle (:math:`\\arctan(1/\\sqrt{17}) \\approx 13.63^\\circ`) pushes the cumulative angle to :math:`364.78^\\circ > 360^\\circ`, causing the next spoke to cross the initial baseline :g:`O P1 <theodorus-spiral:/ O P1 />`!
  2. **Pebble/Parity Arithmetic**: In Pythagorean odd-even congruence modulo :math:`8`, every odd square satisfies :math:`(2k+1)^2 = 4k(k+1) + 1 \\equiv 1 \\pmod{8}`. For :math:`N = 3, 5, 7, 11, 13, 15`, assuming :math:`p^2 = N q^2` immediately fails modulo :math:`4` or :math:`8`, whereas :math:`N = 17 \\equiv 1 \\pmod{8}` is the **first prime** congruent to :math:`1 \\pmod{8}`, requiring an infinite-descent peeling of powers of :math:`2` before contradiction emerges!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **147d3–5 — περὶ δυνάμεών τι ἡμῖν Θεόδωρος ὅδε ἔγραφε, τῆς τε τρίποδος πέρι καὶ πεντέποδος**: :person:`Jowett <jowett>` translates *'Theodorus was writing out for us something about roots, showing that the sides of squares containing three or five square feet...'*. Crucially, **ἔγραφε** means *was drawing geometric diagrams*, and **δύναμις** (:term:`dynamis <dynamis>`) does *not* mean an algebraic number 'root', but a **line segment named from the square area it has the power (*δύναται*) to form**. Likewise **τρίπους** and **πεντέπους** denote *squares of three and five square feet* (literally 'the three-foot [power]', where linear vs. areal 'foot' is determined by feminine *δύναμις*).
- **147e5–148a4 — τὸν ἴσον ἰσάκις… προμήκη δὲ ἀριθμόν**: Burnet's exact multiplicative syntax *ἴσος ἰσάκις γιγνόμενος* ('becoming equal-times-equal', :math:`k \\times k`) vs. *πλείων ἐλαττονάκις ἢ ἐλάττων πλειονάκις* ('greater times less or less times greater') is preserved verbatim in :cite:`Euclid Elements VII, Defs. 16–19 <euclid:VII.def.16>`. Note that Plato uses :term:`promēkēs <promekes>` (*oblong*) broadly for *any* non-square integer, whereas later Neopythagoreans restricted *heteromēkēs* to :math:`k(k+1)`.
- **148b1–2 — ὡς μήκει μὲν οὐ συμμέτρους ἐκείναις, τοῖς δ’ ἐπιπέδοις ἃ δύνανται**: Literally *'incommensurable with those in length, but [commensurable] by the plane figures which they have the power to form'*—the verbatim ancestor of :cite:`Euclid Elements X, Defs. 1–2 <euclid:X.def.1>` (*εὐθεῖαι δυνάμει σύμμετροί εἰσιν, ὅταν τὰ ἀπ’ αὐτῶν τετράγωνα τῷ αὐτῷ χωρίῳ μετρῆται*, 'straight lines are commensurable in square/power when the squares on them are measured by the same area').

III. Reception in Euclid Books VII, X & Sister Repositories
-----------------------------------------------------------

All five sister-corpus citations (`plato:theaetetus`, `147.d`, `147D`, `147.d.sqq`, `147-e-148-b` in ``geometor/euclid`` and ``geometor/elements``) converge on **Elements X.9** (attributed explicitly to :person:`Theaetetus <theaetetus>` by an ancient scholium going back to Pappus): *Squares on straight lines commensurable in length have to one another the ratio which a square number has to a square number; and squares which do not have the ratio of square to square have sides incommensurable in length*.
""".strip(),
    "republic": """
I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_divided_line`` and ``verify_divided_line_identity`` (see :doc:`/demos/index`), Socrates' double proportional section (`509d6–8`) is proved symbolically over an arbitrary ratio :math:`r > 0` and constructed by compass and straightedge under the canonical Academic **Golden Section** (:math:`r = \\phi = \\frac{1+\\sqrt{5}}{2}`, :cite:`Elements II.11 & VI.30 <euclid:II.11>`):

- Let :g:`A B <divided-line:/ A B />` (:term:`eikasia <eikasia>`) have unit measure :math:`1`, and let :math:`AB : BC = AC : CE = CD : DE = 1 : r`. Then:

  .. math::

     |AB| = 1, \\quad |BC| = r, \\quad |AC| = 1 + r, \\quad |CE| = r(1 + r), \\quad |CD| = r, \\quad |DE| = r^2.

- Therefore **for every ratio** :math:`r > 0`, the middle segments :g:`B C <divided-line:/ B C />` (:term:`pistis <pistis>`) and :g:`C D <divided-line:/ C D />` (:term:`dianoia <dianoia>`) satisfy :eq:`exact equality <divided-line:/ B C / = divided-line:/ C D />` :math:`|BC| = |CD| = r`, and each is the **geometric mean** between the extreme segments :g:`A B <divided-line:/ A B />` and :g:`D E <divided-line:/ D E />`, realized geometrically by erecting ordinate :g:`B G <divided-line:/ B G />` to semicircle :g:`(M, C) <divided-line:( M C )>` (:cite:`Elements VI.13 <euclid:II.14>`):

  .. math::

     Q(B, G) = Q(B, C) = Q(C, D) = Q(A, B) \\cdot Q(D, E)^{1/2\\text{ in length}} \\implies |BG|^2 = |AB| \\cdot |DE| = r^2.

- Under the **Golden Ratio** :math:`r = \\phi` (:math:`\\phi^2 = \\phi + 1`), an additional self-similar harmony emerges: the Visible Realm :g:`A C <divided-line:/ A B C />` (:math:`1 + \\phi = \\phi^2`) equals pure :term:`noēsis <noesis>` :g:`D E <divided-line:/ D E />` (:math:`\\phi^2`), making both :math:`(A, B, C)` and :math:`(C, D, E)` golden sections (:g:`golden range <divided-line:/ A C D E />`)!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **509d7–8 — ἀνὰ τὸν αὐτὸν λόγον**: :person:`Jowett <jowett>` translates *'in the same ratio'*, which strictly entails :math:`|BC| = |CD|`. Ancient and modern commentators (:person:`Proclus <proclus>`, Plutarch *Platonic Questions* III) noted that equality of the two middle sub-segments is not an embarrassing accident, but the mathematical seal of Plato's doctrine at `510b4–8`: *dianoia* uses as **images** (*ὡς εἰκόσιν χρωμένη*) the very physical objects imitated by shadows in the visible realm!
- **510c3–5 — ὑποθέμενοι τό τε περιττὸν καὶ τὸ ἄρτιον καὶ τὰ σχήματα καὶ γωνιῶν τριττὰ εἴδη**: Literally *'hypothesizing the odd and the even and the figures and three species of angles'*. The 'three species of angles' are right, obtuse, and acute (:cite:`Elements I, Defs. 10–12 <euclid:I.def.4>`), proving that pre-Euclidean Academic handbooks already opened with parallel arithmetic and geometric *hypotheseis*.
- **510d7–8 — τοῦ τετραγώνου αὐτοῦ ἕνεκα τοὺς λόγους ποιούμενοι καὶ διαμέτρου αὐτῆς**: Literally *'making their arguments for the sake of the Square itself and the Diagonal itself, not the one they draw'*—a direct echo of *Meno* `85b`!
- **528b1–3 — μετὰ ἐπίπεδον… ἐν περιφορᾷ ὂν ἤδη στερεὸν λαβόντες, πρὶν αὐτὸ καθ’ αὑτὸ λαβεῖν**: Socrates corrects his own initial sequence (`plane geometry -> astronomy`) because astronomy treats **solid body already in revolution** before investigating **three-dimensional solid in itself** (*ἡ τῶν κύβων αὔξη καὶ τὸ βάθους μετέχον*, `528b3`). Within one generation of this passage, :person:`Theaetetus <theaetetus>` and :person:`Eudoxus <eudoxus>` created the rigorous stereometry preserved in :cite:`Elements Books XI–XIII <euclid:XIII.13>`.

III. Reception & Sister-Corpus Civic-Arithmetic Locus (*Laws* V 737e–738b)
--------------------------------------------------------------------------

- **Proclus** (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 10–11, 29–32; ``plato:rep:VI.510b-511d``, ``VII.525a-534e``): Grounds the entire Neoplatonic ontology of *dianoia* and imaginative projection (*probolē* into geometric matter) in Republic VI–VII.
- **Hoenen & Civic Arithmetic** (``plato:rep:VI.510c``, ``VII.532c``, ``VII.533c``, and ``plato:leges:737e-738b``, ``738a``): In *De Noetica Geometriae* Cap. IV, :person:`Hoenen <hoenen>` pairs Republic VII's pure arithmetic (`525a–526c`) with Plato's remarkable divisor theorem in *Laws* V `737e–738b`, where the Athenian Stranger selects **5,040** (:math:`= 7! = 1 \\cdot 2 \\cdot 3 \\cdot 4 \\cdot 5 \\cdot 6 \\cdot 7 = 2^4 \\cdot 3^2 \\cdot 5 \\cdot 7`) for civic land allotments because it possesses :math:`(4+1)(2+1)(1+1)(1+1) = 60` total divisors (`59` proper quotients excluding itself) and is evenly divisible by **every integer from 1 to 10** (and even by `12`, while `5,040 - 2 = 5,038 = 11 × 458` restores divisibility by `11`).
""".strip(),
    "timaeus-world-soul": """
I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.harmonics`` and ``construct_timaeus_proportion_circles`` (see :doc:`/demos/index`), both proportions of *Timaeus* `31b–36d` are verified in 100% exact rational and quadratic arithmetic:

1. **Plane vs. Solid Geometric Means (31c–32b)**:
   - Between square plane numbers :math:`p^2` and :math:`q^2`, a single mean :math:`pq` yields :math:`p^2 : pq = pq : q^2` (e.g., :math:`4 : 6 = 6 : 9`).
   - Between cubic solid numbers :math:`p^3` and :math:`q^3`, two means :math:`p^2 q` and :math:`p q^2` yield :math:`p^3 : p^2 q = p^2 q : p q^2 = p q^2 : q^3` (e.g., :math:`8 : 12 = 12 : 18 = 18 : 27`, :cite:`Elements VIII.11–12 <euclid:VIII.11>`).
2. **Pappus Semicircle Construction of the Three Means (`timaeus_world_soul.svg`)**:
   - Joining segments :math:`AJ = 2` and :math:`JB = 4` along diameter :g:`A B <timaeus-means:/ A B />` of circle :g:`(O, B) <timaeus-means:( O B )>` (center :g:`O <timaeus-means:O>`, radius :math:`3`) and erecting ordinate :g:`J G <timaeus-means:/ J G />` with perpendicular projection :g:`G H <timaeus-means:/ G H />` onto radius :g:`O G <timaeus-means:/ O G />` exhibits all three Platonic :term:`means <mesotes>` simultaneously:

     .. math::

        A = |OG| = \\frac{2+4}{2} = 3, \\quad G = |JG| = \\sqrt{2 \\cdot 4} = 2\\sqrt{2}, \\quad H = |GH| = \\frac{2 \\cdot 2 \\cdot 4}{2 + 4} = \\frac{8}{3},

     with exact algebraic identity :math:`A \\cdot H = G^2` (:math:`3 \\cdot \\frac{8}{3} = 8`) and whole-tone ratio :math:`\\frac{|OG|}{|GH|} = \\frac{3}{8/3} = \\frac{9}{8}`!
3. **Exact Factorization of the 34-Term World-Soul Gamut (35b–36b)**:
   - Merging the double (`1, 2, 4, 8`) and triple (`1, 3, 9, 27`) chains with their harmonic and arithmetic means (`1, 4/3, 3/2, 2, 8/3, 3, 4, 9/2, 16/3, 6, 8, 9, 27/2, 18, 27`) and subdividing every :math:`4:3` fourth into two :math:`9:8` whole tones plus the :math:`256:243` :term:`leimma <leimma>` (and every :math:`3:2` fifth into :math:`4:3` plus :math:`9:8`) yields **34 unique exact rational pitches** containing **24 whole tones** and **9 leimmata**:

     .. math::

        \\left(\\frac{9}{8}\\right)^{24} \\cdot \\left(\\frac{256}{243}\\right)^{9}
        = \\frac{3^{48}}{2^{72}} \\cdot \\frac{2^{72}}{3^{45}} = 3^3 = 27.

   - Scaling by :person:`Crantor's <crantor>` least common denominator **384** clears every fraction across the entire :math:`27:1` gamut to exact integers from ``384`` to ``10,368`` (:cite:`Proclus In Timaeum II.167–236 <proclus:in-timaeum>`).

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **36a3–5 — τὴν μὲν ταὐτῷ μέρει τῶν ἄκρων αὐτῶν ὑπερέχουσαν καὶ ὑπερεχομένην**: :person:`Jowett <jowett>` translates accurately *'one mean exceeding and exceeded by equal parts of its extremes'*, which defines the **harmonic mean** :math:`H`: if :math:`H = a + \\frac{a}{k} = b - \\frac{b}{k}`, solving for :math:`1/k = \\frac{b-a}{a+b}` yields :math:`H = a\\left(1 + \\frac{b-a}{a+b}\\right) = \\frac{2ab}{a+b}` (for :math:`a=1, b=2`, :math:`H = 4/3` exceeds :math:`1` by *one-third* of :math:`1` and falls short of :math:`2` by *one-third* of :math:`2`!).
- **36a6–b5 — ἡμιολίων δὲ διαστάσεων καὶ ἐπιτρίτων καὶ ἐπογδόων… λείπων αὐτῶν ἑκάστου μόριον… ἀριθμοῦ πρὸς ἀριθμὸν ἐχούσης τοὺς ὅρους ἓξ καὶ πεντήκοντα καὶ διακοσίων πρὸς τρία καὶ τετταράκοντα καὶ διακόσια**: Notice Plato's extraordinary numerical precision: Greek superparticular adjectives :term:`hēmiolios <hemiolios>` (:math:`1 + \\frac{1}{2} = 3/2`), :term:`epitritos <epitritos>` (:math:`1 + \\frac{1}{3} = 4/3`), and :term:`epogdoos <epogdoos>` (:math:`1 + \\frac{1}{8} = 9/8`) culminate in spelling out verbatim in Attic prose **256 to 243** (*ἓξ καὶ πεντήκοντα καὶ διακοσίων πρὸς τρία καὶ τετταράκοντα καὶ διακόσια*). Note also that two leimmata fall short of a :math:`9:8` whole tone by the **Pythagorean comma** (:math:`531441 : 524288`), leaving the **apotome** :math:`(9/8)/(256/243) = 2187/2048`.

III. Reception in Euclid, Crantor & Proclus
-------------------------------------------

All four sister-corpus citations (`plato:timaeus:31c-36d`, `32-a-b`, `32-a-sqq`, `32.a.b` across ``euclid``, ``elements``, and ``proclus``) center on :cite:`Elements VIII.11–12 <euclid:VIII.11>` and :person:`Archytas's <archytas>` theorem (Euclid *Sectio Canonis* Prop. 3) that no superparticular ratio :math:`(n+1):n` admits a rational geometric mean—explaining why the Demiurge divides octaves and fourths via rational harmonic/arithmetic means (`4:3`, `3:2`, `9:8`, `256:243`) rather than equal-tempered irrational roots!
""".strip(),
    "timaeus-polyhedra": """
I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_timaeus_triangles`` and ``construct_timaeus_cube_face`` (see :doc:`/demos/index`), Plato's two elementary right triangles (`53c–55c`) are constructed purely by compass and straightedge and audited via Rational Trigonometry invariants:

1. **The Fairest Scalene Half-Triangle (`1 : √3 : 2`, `54a–b`)**:

   - Constructing equilateral triangle :g:`ABC <timaeus-triangles:< A B C >>` of side :math:`2\\sqrt{3}` (:math:`Q(A,B) = 12`, :cite:`Elements I.1 <euclid:I.1>`) and drawing its three medians/altitudes through midpoints :g:`M1 <timaeus-triangles:M1>`, :g:`M2 <timaeus-triangles:M2>`, :g:`M3 <timaeus-triangles:M3>` meeting at centroid :g:`G <timaeus-triangles:G>` (:math:`X(2)`) partitions the face into **six** congruent :term:`half-triangles <hemitrigonon>` (e.g., :g:`A M3 G <timaeus-triangles:< A M3 G >>` and :g:`B M3 G <timaeus-triangles:< B M3 G >>`).
   - Each elementary triangle :math:`\\triangle G M_3 A` has exact rational quadrances and spreads over :math:`\\mathbb{Q}`:

     .. math::

        Q(G, M_3) = 1, \\quad Q(A, M_3) = 3, \\quad Q(G, A) = 4, \\qquad
        s_A = \\frac{1}{4}, \\quad s_G = \\frac{3}{4}, \\quad s_{M_3} = 1.

2. **Why Six Triangles Instead of Two? (54d–e)**: A geometric reader naturally asks why Timaeus composes each equilateral cosmic face out of **six** :math:`1:\\sqrt{3}:2` triangles meeting at :g:`G <timaeus-triangles:G>` (`ἐκ ἓξ τοιούτων συμπαγέντων`, `54e1`) rather than just **two** back-to-back along altitude :g:`C M3 <timaeus-triangles:/ C M3 />`. As :person:`Cornford <heath>` (:cite:`1937 <cornford:timaeus:1937>`, pp. 214–218) and :person:`Taylor <heath>` (:cite:`1928 <taylor:timaeus:1928>`, p. 374) point out, bisecting an equilateral triangle along *one* altitude breaks its **threefold rotational symmetry**, whereas drawing all three altitudes (:g:`A M1 <timaeus-triangles:[ A M1 ]>`, :g:`B M2 <timaeus-triangles:[ B M2 ]>`, :g:`C M3 <timaeus-triangles:[ C M3 ]>`) restores complete :math:`D_3` symmetry around :math:`X(2)`!
3. **Exact Triangle Accounting & Chemical Transmutation Equations (`56a–c`)**:

   - Letting :math:`T` denote one equilateral cosmic face (`6` scalenes), the three transmutable regular solids satisfy exact integer conservation of faces and elementary triangles:

     - **1 Water** (icosahedron, :math:`20T = 120` scalenes) :math:`\\longrightarrow` **1 Fire** (:math:`4T = 24`) :math:`+` **2 Air** (:math:`2 \\times 8T = 16T = 96`): :math:`20 = 4 + 2(8)`.
     - **2.5 Air** (:math:`20T`) :math:`\\Longleftrightarrow` **1 Water** (:math:`20T`); **1 Air** (:math:`8T`) :math:`\\Longleftrightarrow` **2 Fire** (:math:`2 \\times 4T = 8T`).

   - Conversely, **Earth** (cube, `6` square faces :math:`\\times 4` isosceles :math:`1:1:\\sqrt{2}` triangles :math:`= 24` isosceles triangles) belongs to the :math:`\\mathbb{Q}(\\sqrt{2})` quadratic field, algebraically disjoint from :math:`\\mathbb{Q}(\\sqrt{3})`, so Earth particles can disintegrate and recombine only into Earth (`56d`)!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **54b4–5 — οὗ ἡ ὑποτείνουσα τῆς ἐλάττονος πλευρᾶς διπλῆ μήκει· τίθεμεν δὴ τοῦτο… τὴν μείζω πλευρὰν τῆς ἐλάττονος τριπλῆν δυνάμει ἔχον** (`54b5` / `54b`): Notice Plato's razor-sharp contrast between **μήκει** (*in length*) and **δυνάμει** (*in square/power*): the hypotenuse (`2`) is *double in length* of the lesser leg (`1`), whereas the greater leg (:math:`\\sqrt{3}`) is **triple in power** (:math:`Q = 3 = 3 \\times 1`) of the lesser leg! :person:`Jowett <jowett>` paraphrases at `54b` *'having the square of the greater side three times the square of the lesser'*, which is mathematically sound, though in Greek Plato writes compactly *τριπλῆν δυνάμει* ('triple in power'), applying :person:`Theaetetus's <theaetetus>` exact vocabulary from Unit II.
- **55c4–6 — ἔτι δὲ οὔσης συστάσεως μιᾶς πέμπτης, ἐπὶ τὸ πᾶν ὁ θεὸς αὐτῇ κατεχρήσατο ἐκεῖνο διαζωγραφῶν**: The fifth regular construction—the **regular dodecahedron** bounded by twelve regular pentagons—cannot be tiled by :math:`1:1:\\sqrt{2}` or :math:`1:\\sqrt{3}:2` triangles because the pentagon diagonal-to-side ratio is the **Golden Ratio** :math:`\\phi = \\frac{1+\\sqrt{5}}{2}` (:cite:`Elements XIII.8 & XIII.17 <euclid:XIII.13>`). Plato therefore reserves it for embroidering the spherical zodiacal cosmos itself (`διαζωγραφῶν`).

III. Reception in Euclid Book XIII, Aristotle & Pacioli
-------------------------------------------------------

- **Euclid Book XIII & Proclus**: :person:`Proclus <proclus>` (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 68.20–23) famously declares that Euclid was a Platonist who composed the entire thirteen-book *Elements* with the construction and exhaustive uniqueness proof of the five cosmic Platonic figures (:cite:`XIII.13–18 <euclid:XIII.13>`) as its supreme architectural *telos*.
- **Aristotle** (:cite:`De Caelo III.7–8, 306a1–307b18 <aristotle:de-caelo>`; ``plato:timaeus``): Mounts a sustained physical and geometric critique—arguing that suspending division at two-dimensional weightless planes violates mathematical continuity, and that neither pyramids nor octahedra/icosahedra tile three-dimensional space without leaving voids (anticipating the honeycomb theorem that among regular Platonic solids only the cube tiles :math:`\\mathbb{E}^3`, though combinations of regular tetrahedra and octahedra do tile :math:`\\mathbb{E}^3`!).
- **Luca Pacioli** (:cite:`De Divina Proportione <pacioli:divina:1509>`, 9 occurrences of ``plato:timaeus:53c-56c``): Grounds his entire Renaissance treatise on the Golden Ratio and Leonardo da Vinci's sixty polyhedral plates in *Timaeus* `53c–56c`.
""".strip(),
    "foundations": """
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

        Q(O, C) = 1 \\;(\\text{length } 1), \\quad Q(O, D) = 2 \\;(\\text{plane } \\sqrt{2}), \\quad Q(O, E) = 3 \\;(\\text{solid } \\sqrt{3}).

   - Pairwise ratios :math:`1 : \\sqrt{2}`, :math:`1 : \\sqrt{3}`, and :math:`\\sqrt{2} : \\sqrt{3}` (:math:`Q_D / Q_E = 2/3`, non-square!) prove that unit length, square diagonal, and cube diagonal are **mutually incommensurable** across all three pairs—illustrating the Athenian Stranger's shock (`819e–820a`) that educated Greeks falsely suppose length, breadth, and depth to be universally commensurable!

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
""".strip(),
}
