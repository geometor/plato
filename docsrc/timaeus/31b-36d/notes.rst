:layout: book
:type: notes
:title: World-Soul & Means — Notes
:canonical_id: Timaeus 31b–36d
:folio: Tim. 31b
:tracks: English: index | Greek (Burnet OCT): greek | Summary: summary | Notes: notes

.. _timaeus-31b-36d-notes:
.. _timaeus-world-soul-notes:

==================================================
World-Soul & Means — Critical Commentary & Notes
==================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Timaeus 31b–36d

.. picture:: /_static/figures/timaeus_world_soul.svg
   :alt: Timaeus: Geometric Proportion & Harmonic Division of the World-Soul
   :caption: The Three Platonic Means & Circles of the World-Soul (Timaeus 31c–36d): on octave diameter A J B (2 + 4 = 6), radius O G = 3 is the arithmetic mean, ordinate J G = 2*sqrt(2) is the geometric mean, projection G H = 8/3 is the harmonic mean (giving O G / G H = 9/8), and axis [P, Q] crosses at O like Chi (X).

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.harmonics`` and ``construct_timaeus_proportion_circles`` (see :doc:`/demos/index`), both proportions of *Timaeus* `31b–36d` are verified in 100% exact rational and quadratic arithmetic:

1. **Plane vs. Solid Geometric Means (31c–32b)**:
   - Between square plane numbers :math:`p^2` and :math:`q^2`, a single mean :math:`pq` yields :math:`p^2 : pq = pq : q^2` (e.g., :math:`4 : 6 = 6 : 9`).
   - Between cubic solid numbers :math:`p^3` and :math:`q^3`, two means :math:`p^2 q` and :math:`p q^2` yield :math:`p^3 : p^2 q = p^2 q : p q^2 = p q^2 : q^3` (e.g., :math:`8 : 12 = 12 : 18 = 18 : 27`, :cite:`Elements VIII.11–12 <euclid:VIII.11>`).
2. **Pappus Semicircle Construction of the Three Means (`timaeus_world_soul.svg`)**:
   - Joining segments :math:`AJ = 2` and :math:`JB = 4` along diameter :g:`A B <timaeus-means:/ A B />` of circle :g:`(O, B) <timaeus-means:( O B )>` (center :g:`O <timaeus-means:O>`, radius :math:`3`) and erecting ordinate :g:`J G <timaeus-means:/ J G />` with perpendicular projection :g:`G H <timaeus-means:/ G H />` onto radius :g:`O G <timaeus-means:/ O G />` exhibits all three Platonic :term:`means <mesotes>` simultaneously:

     .. math::

        A = |OG| = \frac{2+4}{2} = 3, \quad G = |JG| = \sqrt{2 \cdot 4} = 2\sqrt{2}, \quad H = |GH| = \frac{2 \cdot 2 \cdot 4}{2 + 4} = \frac{8}{3},

     with exact algebraic identity :math:`A \cdot H = G^2` (:math:`3 \cdot \frac{8}{3} = 8`) and whole-tone ratio :math:`\frac{|OG|}{|GH|} = \frac{3}{8/3} = \frac{9}{8}`!
3. **Exact Factorization of the 34-Term World-Soul Gamut (35b–36b)**:
   - Merging the double (`1, 2, 4, 8`) and triple (`1, 3, 9, 27`) chains with their harmonic and arithmetic means (`1, 4/3, 3/2, 2, 8/3, 3, 4, 9/2, 16/3, 6, 8, 9, 27/2, 18, 27`) and subdividing every :math:`4:3` fourth into two :math:`9:8` whole tones plus the :math:`256:243` :term:`leimma <leimma>` (and every :math:`3:2` fifth into :math:`4:3` plus :math:`9:8`) yields **34 unique exact rational pitches** containing **24 whole tones** and **9 leimmata**:

     .. math::

        \left(\frac{9}{8}\right)^{24} \cdot \left(\frac{256}{243}\right)^{9}
        = \frac{3^{48}}{2^{72}} \cdot \frac{2^{72}}{3^{45}} = 3^3 = 27.

   - Scaling by :person:`Crantor's <crantor>` least common denominator **384** clears every fraction across the entire :math:`27:1` gamut to exact integers from ``384`` to ``10,368`` (:cite:`Proclus In Timaeum II.167–236 <proclus:in-timaeum>`).

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **36a3–5 — τὴν μὲν ταὐτῷ μέρει τῶν ἄκρων αὐτῶν ὑπερέχουσαν καὶ ὑπερεχομένην**: :person:`Jowett <jowett>` translates accurately *'one mean exceeding and exceeded by equal parts of its extremes'*, which defines the **harmonic mean** :math:`H`: if :math:`H = a + \frac{a}{k} = b - \frac{b}{k}`, solving for :math:`1/k = \frac{b-a}{a+b}` yields :math:`H = a\left(1 + \frac{b-a}{a+b}\right) = \frac{2ab}{a+b}` (for :math:`a=1, b=2`, :math:`H = 4/3` exceeds :math:`1` by *one-third* of :math:`1` and falls short of :math:`2` by *one-third* of :math:`2`!).
- **36a6–b5 — ἡμιολίων δὲ διαστάσεων καὶ ἐπιτρίτων καὶ ἐπογδόων… λείπων αὐτῶν ἑκάστου μόριον… ἀριθμοῦ πρὸς ἀριθμὸν ἐχούσης τοὺς ὅρους ἓξ καὶ πεντήκοντα καὶ διακοσίων πρὸς τρία καὶ τετταράκοντα καὶ διακόσια**: Notice Plato's extraordinary numerical precision: Greek superparticular adjectives :term:`hēmiolios <hemiolios>` (:math:`1 + \frac{1}{2} = 3/2`), :term:`epitritos <epitritos>` (:math:`1 + \frac{1}{3} = 4/3`), and :term:`epogdoos <epogdoos>` (:math:`1 + \frac{1}{8} = 9/8`) culminate in spelling out verbatim in Attic prose **256 to 243** (*ἓξ καὶ πεντήκοντα καὶ διακοσίων πρὸς τρία καὶ τετταράκοντα καὶ διακόσια*). Note also that two leimmata fall short of a :math:`9:8` whole tone by the **Pythagorean comma** (:math:`531441 : 524288`), leaving the **apotome** :math:`(9/8)/(256/243) = 2187/2048`.

III. Reception in Euclid, Crantor & Proclus
-------------------------------------------

All four sister-corpus citations (`plato:timaeus:31c-36d`, `32-a-b`, `32-a-sqq`, `32.a.b` across ``euclid``, ``elements``, and ``proclus``) center on :cite:`Elements VIII.11–12 <euclid:VIII.11>` and :person:`Archytas's <archytas>` theorem (Euclid *Sectio Canonis* Prop. 3) that no superparticular ratio :math:`(n+1):n` admits a rational geometric mean—explaining why the Demiurge divides octaves and fourths via rational harmonic/arithmetic means (`4:3`, `3:2`, `9:8`, `256:243`) rather than equal-tempered irrational roots!

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit IV** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
