:layout: book
:type: notes
:title: Unit V — Timaeus: Elementary Right Triangles & Construction of the Cosmic Polyhedra — Notes
:canonical_id: Timaeus 53c–56c
:original_id: Stephanus Timaeus 53c–56c
:folio: Timaeus 53c–56c

.. _timaeus-polyhedra-notes:

=================================================================================================================
Unit V — Timaeus: Elementary Right Triangles & Construction of the Cosmic Polyhedra — Critical Commentary & Notes
=================================================================================================================

.. rubric:: Exact Symbolic Reconstruction, Greek Mathematical Philology & Canon Reception · Timaeus 53c–56c

.. picture:: /_static/figures/timaeus_triangles.svg
   :alt: Timaeus: Elementary Right Triangles & Construction of the Cosmic Polyhedra
   :caption: Cosmic Equilateral Face Assembly (Timaeus 54d–55a): six elementary 1 : sqrt(3) : 2 right-angled scalene triangles (quadrances 1, 3, 4; spreads 1/4, 3/4, 1) meet thrice along their diagonals and altitudes at centroid G = X(2) to compose equilateral face < A B C >.

I. Exact Geometric & Symbolic Reconstruction
--------------------------------------------

In ``geometor.plato.constructions.construct_timaeus_triangles`` and ``construct_timaeus_cube_face`` (see :doc:`/demos/index`), Plato's two elementary right triangles (`53c–55c`) are constructed purely by compass and straightedge and audited via Rational Trigonometry invariants:

1. **The Fairest Scalene Half-Triangle (`1 : √3 : 2`, `54a–b`)**:

   - Constructing equilateral triangle :g:`ABC <timaeus-triangles:< A B C >>` of side :math:`2\sqrt{3}` (:math:`Q(A,B) = 12`, :cite:`Elements I.1 <euclid:I.1>`) and drawing its three medians/altitudes through midpoints :g:`M1 <timaeus-triangles:M1>`, :g:`M2 <timaeus-triangles:M2>`, :g:`M3 <timaeus-triangles:M3>` meeting at centroid :g:`G <timaeus-triangles:G>` (:math:`X(2)`) partitions the face into **six** congruent :term:`half-triangles <hemitrigonon>` (e.g., :g:`A M3 G <timaeus-triangles:< A M3 G >>` and :g:`B M3 G <timaeus-triangles:< B M3 G >>`).
   - Each elementary triangle :math:`\triangle G M_3 A` has exact rational quadrances and spreads over :math:`\mathbb{Q}`:

     .. math::

        Q(G, M_3) = 1, \quad Q(A, M_3) = 3, \quad Q(G, A) = 4, \qquad
        s_A = \frac{1}{4}, \quad s_G = \frac{3}{4}, \quad s_{M_3} = 1.

2. **Why Six Triangles Instead of Two? (54d–e)**: A geometric reader naturally asks why Timaeus composes each equilateral cosmic face out of **six** :math:`1:\sqrt{3}:2` triangles meeting at :g:`G <timaeus-triangles:G>` (`ἐκ ἓξ τοιούτων συμπαγέντων`, `54e1`) rather than just **two** back-to-back along altitude :g:`C M3 <timaeus-triangles:/ C M3 />`. As :person:`Cornford <heath>` (:cite:`1937 <cornford:timaeus:1937>`, pp. 214–218) and :person:`Taylor <heath>` (:cite:`1928 <taylor:timaeus:1928>`, p. 374) point out, bisecting an equilateral triangle along *one* altitude breaks its **threefold rotational symmetry**, whereas drawing all three altitudes (:g:`A M1 <timaeus-triangles:[ A M1 ]>`, :g:`B M2 <timaeus-triangles:[ B M2 ]>`, :g:`C M3 <timaeus-triangles:[ C M3 ]>`) restores complete :math:`D_3` symmetry around :math:`X(2)`!
3. **Exact Triangle Accounting & Chemical Transmutation Equations (`56a–c`)**:

   - Letting :math:`T` denote one equilateral cosmic face (`6` scalenes), the three transmutable regular solids satisfy exact integer conservation of faces and elementary triangles:

     - **1 Water** (icosahedron, :math:`20T = 120` scalenes) :math:`\longrightarrow` **1 Fire** (:math:`4T = 24`) :math:`+` **2 Air** (:math:`2 \times 8T = 16T = 96`): :math:`20 = 4 + 2(8)`.
     - **2.5 Air** (:math:`20T`) :math:`\Longleftrightarrow` **1 Water** (:math:`20T`); **1 Air** (:math:`8T`) :math:`\Longleftrightarrow` **2 Fire** (:math:`2 \times 4T = 8T`).

   - Conversely, **Earth** (cube, `6` square faces :math:`\times 4` isosceles :math:`1:1:\sqrt{2}` triangles :math:`= 24` isosceles triangles) belongs to the :math:`\mathbb{Q}(\sqrt{2})` quadratic field, algebraically disjoint from :math:`\mathbb{Q}(\sqrt{3})`, so Earth particles can disintegrate and recombine only into Earth (`56d`)!

II. Literal Greek Mathematical Philology (*Contra Paraphrasim*)
---------------------------------------------------------------

- **54b4–5 — οὗ ἡ ὑποτείνουσα τῆς ἐλάττονος πλευρᾶς διπλῆ μήκει· τίθεμεν δὴ τοῦτο… τὴν μείζω πλευρὰν τῆς ἐλάττονος τριπλῆν δυνάμει ἔχον** (`54b5` / `54b`): Notice Plato's razor-sharp contrast between **μήκει** (*in length*) and **δυνάμει** (*in square/power*): the hypotenuse (`2`) is *double in length* of the lesser leg (`1`), whereas the greater leg (:math:`\sqrt{3}`) is **triple in power** (:math:`Q = 3 = 3 \times 1`) of the lesser leg! :person:`Jowett <jowett>` paraphrases at `54b` *'having the square of the greater side three times the square of the lesser'*, which is mathematically sound, though in Greek Plato writes compactly *τριπλῆν δυνάμει* ('triple in power'), applying :person:`Theaetetus's <theaetetus>` exact vocabulary from Unit II.
- **55c4–6 — ἔτι δὲ οὔσης συστάσεως μιᾶς πέμπτης, ἐπὶ τὸ πᾶν ὁ θεὸς αὐτῇ κατεχρήσατο ἐκεῖνο διαζωγραφῶν**: The fifth regular construction—the **regular dodecahedron** bounded by twelve regular pentagons—cannot be tiled by :math:`1:1:\sqrt{2}` or :math:`1:\sqrt{3}:2` triangles because the pentagon diagonal-to-side ratio is the **Golden Ratio** :math:`\phi = \frac{1+\sqrt{5}}{2}` (:cite:`Elements XIII.8 & XIII.17 <euclid:XIII.13>`). Plato therefore reserves it for embroidering the spherical zodiacal cosmos itself (`διαζωγραφῶν`).

III. Reception in Euclid Book XIII, Aristotle & Pacioli
-------------------------------------------------------

- **Euclid Book XIII & Proclus**: :person:`Proclus <proclus>` (:cite:`In Euclidem <proclus:in-euclidem>`, Friedlein 68.20–23) famously declares that Euclid was a Platonist who composed the entire thirteen-book *Elements* with the construction and exhaustive uniqueness proof of the five cosmic Platonic figures (:cite:`XIII.13–18 <euclid:XIII.13>`) as its supreme architectural *telos*.
- **Aristotle** (:cite:`De Caelo III.7–8, 306a1–307b18 <aristotle:de-caelo>`; ``plato:timaeus``): Mounts a sustained physical and geometric critique—arguing that suspending division at two-dimensional weightless planes violates mathematical continuity, and that neither pyramids nor octahedra/icosahedra tile three-dimensional space without leaving voids (anticipating the honeycomb theorem that among regular Platonic solids only the cube tiles :math:`\mathbb{E}^3`, though combinations of regular tetrahedra and octahedra do tile :math:`\mathbb{E}^3`!).
- **Luca Pacioli** (:cite:`De Divina Proportione <pacioli:divina:1509>`, 9 occurrences of ``plato:timaeus:53c-56c``): Grounds his entire Renaissance treatise on the Golden Ratio and Leonardo da Vinci's sixty polyhedral plates in *Timaeus* `53c–56c`.

IV. Executable Symbolic Verification
------------------------------------

In accordance with GEOMETOR's strict content/code separation for historical editions, executable ``geometor.model`` SymPy constructions and Rational Trigonometry verification routines for **Unit V** live in ``src/geometor/plato/`` and the companion walkthrough :doc:`/demos/index`.
