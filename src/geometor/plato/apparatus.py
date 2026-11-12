"""Scholarly apparatus registries (glossary, persons, bibliography) for *geometor-plato*.

Exports canonical JSON dictionaries to both ``resources/`` and
``resources/loci_mathematici/`` for ``photon-platform/publish`` inline roles
(``:term:``, ``:person:``, ``:cite:``) and compiles ``glossary.rst``,
``persons.rst``, and ``bibliography.rst`` for the Book Codex.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

__all__ = [
    "CITATIONS_DATA",
    "GLOSSARY_DATA",
    "PERSONS_DATA",
    "render_bibliography_rst",
    "render_glossary_rst",
    "render_persons_rst",
    "write_apparatus_artifacts",
]

GLOSSARY_DATA: dict[str, dict[str, str]] = {
    "schema": {
        "headword": "σχῆμα (schēma)",
        "greek": "σχῆμα",
        "latin": "figura",
        "translation": "Geometric figure",
        "loci": "Meno 75d–76a; Parmenides 145b; Philebus 51c",
        "definition": (
            "Defined dialectically by Socrates at Meno 76a7 as 'the limit of solid' "
            "(στερεοῦ πέρας), anticipating Euclid Elements I, Defs. 13–14 and XI, Def. 2."
        ),
    },
    "stereon": {
        "headword": "στερεόν (stereon)",
        "greek": "στερεόν",
        "latin": "solidum",
        "translation": "Solid / Three-dimensional body",
        "loci": "Meno 76a; Theaetetus 148b; Republic VII 528a–d; Timaeus 32b; Laws VII 817e",
        "definition": (
            "Magnitude possessing depth (βάθος) in addition to length and breadth; "
            "requires two geometric means for continuous proportion (Timaeus 32b; Elements VIII.12)."
        ),
    },
    "epipedon": {
        "headword": "ἐπίπεδον (epipedon)",
        "greek": "ἐπίπεδον",
        "latin": "planum / superficies",
        "translation": "Plane surface / Plane number",
        "loci": "Meno 76a; Theaetetus 148a; Republic VII 528a; Timaeus 32a, 53c",
        "definition": (
            "Two-dimensional surface or plane product of two factors; joined in continuous "
            "proportion by a single mean proportional (Timaeus 32a; Elements VIII.11)."
        ),
    },
    "peras": {
        "headword": "πέρας (peras)",
        "greek": "πέρας",
        "latin": "terminus / finis",
        "translation": "Limit / Determinate ratio",
        "loci": "Meno 76a; Philebus 16c–26d",
        "definition": (
            "In Meno 76a, the bounding extremity of a magnitude; in Philebus 25a–d, the "
            "supreme ontological genus of equal, double, and every exact ratio of number to "
            "number or measure to measure that brings indeterminate continua into symmetry."
        ),
    },
    "apeiron": {
        "headword": "ἄπειρον (apeiron)",
        "greek": "ἄπειρον",
        "latin": "infinitum / indeterminatum",
        "translation": "The Unlimited / Indeterminate continuum",
        "loci": "Parmenides 137d, 145a; Philebus 16c–26d",
        "definition": (
            "The domain of 'the more and less' (τὸ μᾶλλόν τε καὶ ἧττον) lacking intrinsic "
            "numeric or geometric measure prior to the imposition of Limit (peras)."
        ),
    },
    "anamnesis": {
        "headword": "ἀνάμνησις (anamnēsis)",
        "greek": "ἀνάμνησις",
        "latin": "reminiscentia",
        "translation": "Noetic recollection",
        "loci": "Meno 81d–85d",
        "definition": (
            "Plato's epistemological thesis that geometric discovery—exemplified when Meno's "
            "untutored attendant recognizes Q = 4 + 4 = 8 from the diagonal diagram—consists "
            "in recovering necessary truths latent within rational soul."
        ),
    },
    "diametros": {
        "headword": "διάμετρος (diametros)",
        "greek": "διάμετρος",
        "latin": "diameter / diagonalis",
        "translation": "Diagonal of a square or diameter of a circle",
        "loci": "Meno 85b; Republic VI 510d",
        "definition": (
            "Technical geometric term ('as the sophists/geometers call it', Meno 85b4) for "
            "the line cutting a square into two equal isosceles right triangles, whose square "
            "has double the area of the original square."
        ),
    },
    "hypothesis": {
        "headword": "ὑπόθεσις (hypothesis)",
        "greek": "ὑπόθεσις",
        "latin": "suppositio",
        "translation": "Mathematical hypothesis / Starting assumption",
        "loci": "Meno 86e–87b; Republic VI 510b–511d; VII 533c",
        "definition": (
            "Both the geometer's analytic reduction of a problem to an auxiliary condition "
            "(Meno 86e–87a) and the unexamined postulates of odd, even, figures, and angles "
            "from which dianoia reasons downward (Republic VI 510c)."
        ),
    },
    "parateinein": {
        "headword": "παρατείνειν / ἐλλείπειν (parateinein / elleipein)",
        "greek": "παρατείνειν, ἐλλείπειν",
        "latin": "applicatio arearum cum defectu",
        "translation": "Elliptic application of area",
        "loci": "Meno 87a",
        "definition": (
            "To apply (παρατείνειν) a given area along the diameter of a circle so as to fall "
            "short (ἐλλείπειν) by a figure similar to the applied area—equivalent to inscribing "
            "a triangle of given area in a circle and to Euclid Elements VI.28."
        ),
    },
    "mekos": {
        "headword": "μῆκος (mēkos)",
        "greek": "μῆκος",
        "latin": "longitudo",
        "translation": "Rational / Commensurable length",
        "loci": "Theaetetus 148a–b; Laws VII 819e",
        "definition": (
            "In Theaetetus's classification (148a–b), any line segment commensurable in linear "
            "measure with the chosen unit—specifically the side of an equilateral square number "
            "(1, 4, 9, 16, ...)."
        ),
    },
    "dynamis": {
        "headword": "δύναμις (dynamis)",
        "greek": "δύναμις",
        "latin": "potentia",
        "translation": "Quadratic power / Incommensurable square-root line",
        "loci": "Theaetetus 147d–148b; Republic VIII 546b; Timaeus 31c",
        "definition": (
            "A line segment incommensurable in length (μήκει οὐ σύμμετρος) with the unit, yet "
            "commensurable by the plane square area it has the 'power' (δύναται) to generate "
            "(√2, √3, √5, ..., √17; cf. Euclid Elements X, Defs. 1–4 & X.9)."
        ),
    },
    "isos-isakis": {
        "headword": "ἴσος ἰσάκις (isos isakis)",
        "greek": "ἴσος ἰσάκις",
        "latin": "aequaliter aequalis / numerus quadratus",
        "translation": "Equilateral square number",
        "loci": "Theaetetus 147e",
        "definition": (
            "An integer factorable as equal times equal (n = k · k), likened to a square geometric "
            "figure; its side is commensurable in length (mēkos) with the unit (Euclid VII, Def. 18)."
        ),
    },
    "promekes": {
        "headword": "προμήκης (promēkēs)",
        "greek": "προμήκης ἀριθμός",
        "latin": "numerus oblongus",
        "translation": "Oblong (non-square) number",
        "loci": "Theaetetus 148a",
        "definition": (
            "An integer enclosed by unequal factors (greater times less, e.g., 3 = 3×1, 6 = 3×2), "
            "whose equivalent square has a side that is a quadratic surd (dynamis)."
        ),
    },
    "eikasia": {
        "headword": "εἰκασία (eikasia)",
        "greek": "εἰκασία",
        "latin": "imaginatio / conjectura",
        "translation": "Apprehension of shadows and reflections",
        "loci": "Republic VI 509e–511e; VII 534a",
        "definition": (
            "Lowest segment (/ A B /) of the Divided Line, directed toward cast shadows and "
            "specular reflections in water and polished surfaces."
        ),
    },
    "pistis": {
        "headword": "πίστις (pistis)",
        "greek": "πίστις",
        "latin": "fides",
        "translation": "Sensible belief / Conviction",
        "loci": "Republic VI 510a, 511e; VII 534a",
        "definition": (
            "Upper segment (/ B C /) of the visible realm on the Divided Line, grasping physical "
            "organisms and artifacts—the very objects geometers redeploy as visible diagrams "
            "in dianoia (/ C D /) with exact proportional equality ``|BC| = |CD|``."
        ),
    },
    "dianoia": {
        "headword": "διάνοια (dianoia)",
        "greek": "διάνοια",
        "latin": "ratio discursiva / cogitatio",
        "translation": "Discursive mathematical understanding",
        "loci": "Republic VI 510b–511e; VII 533d–534a",
        "definition": (
            "Lower segment (/ C D /) of the intelligible realm: the proper cognitive state of "
            "geometry and the sister sciences, reasoning deductively from unexamined hypotheses "
            "with the aid of visible diagrams toward immutable intelligible figures."
        ),
    },
    "noesis": {
        "headword": "νόησις / νοῦς (noēsis / nous)",
        "greek": "νόησις, νοῦς",
        "latin": "intellectus / intelligentia",
        "translation": "Pure dialectical intuition",
        "loci": "Republic VI 511b–e; VII 534a",
        "definition": (
            "Supreme segment (/ D E /) of the Divided Line, treating hypotheses literally as "
            "stepping-stones to ascend to the unhypothetical first principle without sensible images."
        ),
    },
    "anhypotheton": {
        "headword": "ἀνυπόθετον (anhypotheton)",
        "greek": "τὸ ἀνυπόθετον",
        "latin": "principium non suppositum",
        "translation": "The unhypothetical first principle",
        "loci": "Republic VI 510b, 511b; VII 533c",
        "definition": (
            "The self-grounding first principle of the whole (ἡ τοῦ παντὸς ἀρχή), identified "
            "with the Idea of the Good, from which dialectic validates the axioms of mathematics."
        ),
    },
    "arithmetike": {
        "headword": "ἀριθμητική (arithmētikē)",
        "greek": "ἀριθμητική",
        "latin": "arithmetica",
        "translation": "Pure number theory",
        "loci": "Republic VII 525a–526c; Philebus 56d–e",
        "definition": (
            "First science of the Platonic Quadrivium, contemplating abstract equal units "
            "completely indivisible and free of sensible inequality (cf. Euclid Books VII–IX)."
        ),
    },
    "logistike": {
        "headword": "λογιστική (logistikē)",
        "greek": "λογιστική",
        "latin": "logistica",
        "translation": "Science of numerical ratios and calculation",
        "loci": "Republic VII 525a–c; Laws VII 817e",
        "definition": (
            "Paired with arithmetic as the study of the mutual quantitative relations of "
            "numbers; distinguished into vulgar mercantile reckoning vs. philosophical ratio theory."
        ),
    },
    "stereometria": {
        "headword": "στερεομετρία / τριχῇ αὔξη (stereometria)",
        "greek": "ἡ τῶν κύβων αὔξη / στερεόν",
        "latin": "stereometria",
        "translation": "Solid geometry (three-dimensional increase)",
        "loci": "Republic VII 528a–d",
        "definition": (
            "Third science of the Quadrivium—inserted by Socrates between plane geometry and "
            "astronomy—investigating cubes and figures sharing depth; historically realized in "
            "Theaetetus's and Eudoxus's work culminating in Euclid Elements Books XI–XIII."
        ),
    },
    "dialektike": {
        "headword": "διαλεκτική / θριγκός (dialektikē / thrinkos)",
        "greek": "διαλεκτική, θριγκός",
        "latin": "dialectica",
        "translation": "Dialectic, coping-stone of the mathematical sciences",
        "loci": "Republic VII 531d–534e",
        "definition": (
            "The synoptic science that grasps the kinship (συγγένεια) and community of the five "
            "mathematical disciplines and ascends to the essence (λόγος τῆς οὐσίας) of each thing."
        ),
    },
    "analogia": {
        "headword": "ἀναλογία (analogia)",
        "greek": "ἀναλογία",
        "latin": "proportio",
        "translation": "Geometric proportion",
        "loci": "Timaeus 31c–32c; Republic VI 509d, VII 534a",
        "definition": (
            "Continuous equality of ratios (a : b = b : c), revered in Timaeus 31c as the "
            "fairest of all bonds because it makes the mean simultaneously first, middle, and last."
        ),
    },
    "desmos": {
        "headword": "δεσμός (desmos)",
        "greek": "δεσμός",
        "latin": "vinculum",
        "translation": "Proportional bond",
        "loci": "Timaeus 31c",
        "definition": (
            "The unifying mathematical relation binding disparate elements into an indissoluble "
            "cosmos: one mean for planes (a, ab, b²), two means for solids (a³, a²b, ab², b³)."
        ),
    },
    "mesotes": {
        "headword": "μεσότης (mesotēs)",
        "greek": "μεσότης",
        "latin": "medietas",
        "translation": "Mathematical mean (arithmetic, geometric, harmonic)",
        "loci": "Timaeus 32a, 36a",
        "definition": (
            "The three classical Archytean means inscribed in Timaeus 31c–36a: geometric √(ab), "
            "harmonic 2ab/(a+b) ('exceeding and exceeded by the same fraction of the extremes'), "
            "and arithmetic (a+b)/2 ('exceeding and exceeded by an equal number')."
        ),
    },
    "epitritos": {
        "headword": "ἐπίτριτος (epitritos)",
        "greek": "ἐπίτριτος διάστασις",
        "latin": "proportio sesquitertia",
        "translation": "Sesquitertian ratio / Perfect fourth (4 : 3)",
        "loci": "Timaeus 36a–b",
        "definition": (
            "Superparticular ratio 1 + 1/3 = 4/3 generated between a double-interval baseline a "
            "and its harmonic mean 4a/3, as well as between its arithmetic mean 3a/2 and double 2a."
        ),
    },
    "hemiolios": {
        "headword": "ἡμιόλιος (hēmiolios)",
        "greek": "ἡμιόλιος διάστασις",
        "latin": "proportio sesquialtera",
        "translation": "Sesquialter ratio / Perfect fifth (3 : 2)",
        "loci": "Timaeus 36a",
        "definition": (
            "Superparticular ratio 1 + 1/2 = 3/2 generated both in the double intervals (between "
            "1 and 3/2) and throughout the triple intervals (1, 3/2, 2, 3)."
        ),
    },
    "epogdoos": {
        "headword": "ἐπόγδοος (epogdoos)",
        "greek": "ἐπόγδοον διάστημα",
        "latin": "proportio sesquioctava / tonus",
        "translation": "Whole-tone ratio (9 : 8)",
        "loci": "Timaeus 36a–b",
        "definition": (
            "Superparticular ratio 1 + 1/8 = 9/8 separating the arithmetic mean (3/2) from the "
            "harmonic mean (4/3), used by the Demiurge to measure out every 4:3 fourth."
        ),
    },
    "leimma": {
        "headword": "λεῖμμα (leimma)",
        "greek": "λεῖμμα",
        "latin": "limma",
        "translation": "Pythagorean diatonic semitone (256 : 243)",
        "loci": "Timaeus 36b",
        "definition": (
            "The exact rational remainder left when two 9:8 whole tones (81/64) are divided out "
            "of a 4:3 fourth: (4/3) / (81/64) = 256/243 ('number to number, 256 to 243')."
        ),
    },
    "stoicheion": {
        "headword": "στοιχεῖον (stoicheion)",
        "greek": "στοιχεῖον",
        "latin": "elementum",
        "translation": "Geometric element",
        "loci": "Theaetetus 201e; Timaeus 48b, 53c–55c",
        "definition": (
            "Originally a letter/syllabic element; transferred by Plato in Timaeus 48b–53d from "
            "fire, air, water, and earth (which are 'not even syllables') down to their planar "
            "right-triangle constituents—whence Euclid's title Στοιχεῖα."
        ),
    },
    "hemitrigonon": {
        "headword": "ἡμιτρίγωνον (hēmitrigōnon)",
        "greek": "τρίγωνον σκαληνές / ἡμιτρίγωνον",
        "latin": "semitriangulum",
        "translation": "Fairest scalene right triangle (1 : √3 : 2)",
        "loci": "Timaeus 54a–55b",
        "definition": (
            "Half of an equilateral triangle bisected by its altitude, having exact side "
            "quadrances 1, 3, 4 ('the greater side triple in power of the lesser', 54b5) and "
            "rational spreads 1/4, 3/4, 1."
        ),
    },
    "epiprosthesis": {
        "headword": "ἐπιπρόσθησις (epiprosthēsis)",
        "greek": "ἐπίπροσθεν εἶναι",
        "latin": "occultatio optica",
        "translation": "Optical line-of-sight occultation",
        "loci": "Parmenides 137e",
        "definition": (
            "Plato's celebrated definition of the straight line (εὐθύ): 'that of which the "
            "middle stands in front of (blocks) both extremes' along a visual ray."
        ),
    },
    "tornos-kanon": {
        "headword": "τόρνος καὶ κανών (tornos kai kanōn)",
        "greek": "τόρνος, κανών, διαβήτης",
        "latin": "circinus et regula",
        "translation": "Compass/lathe and straightedge",
        "loci": "Philebus 51c, 56b",
        "definition": (
            "Canonical constructive instruments generating pure, non-relative geometric beauty "
            "(circles, straight lines, planes, and solids) intrinsic to form itself."
        ),
    },
    "symmetros-asymmetros": {
        "headword": "σύμμετρος / ἀσύμμετρος (symmetros / asymmetros)",
        "greek": "σύμμετρος, ἀσύμμετρος",
        "latin": "commensurabilis / incommensurabilis",
        "translation": "Commensurable & Incommensurable",
        "loci": "Theaetetus 147d–148b; Laws VII 819e–820c",
        "definition": (
            "Having (or lacking) a common unit measure across lengths, surfaces, and solids; "
            "declared in Laws VII 819e–820c indispensable knowledge distinguishing rational "
            "human beings from 'swine-like' ignorance."
        ),
    },
}

PERSONS_DATA: dict[str, dict[str, str]] = {
    "plato": {
        "name": "Plato of Athens",
        "dates": "c. 428 – 347 BC",
        "role": "Founder of the Academy & Architect of Mathematical Philosophy",
        "bio": (
            "Founded the Athenian Academy (c. 387 BC), elevating pure arithmetic, plane geometry, "
            "solid geometry, mathematical astronomy, and harmonics into the indispensable propaedeutic "
            "to dialectic and catalyzing the research of Theaetetus and Eudoxus."
        ),
    },
    "socrates": {
        "name": "Socrates of Athens",
        "dates": "469 – 399 BC",
        "role": "Dialectical Interlocutor in Meno, Theaetetus, Republic & Philebus",
        "bio": (
            "Guides Meno's attendant through the diagonal doubling proof, frames Theaetetus's "
            "classification of powers, expounds the Divided Line and Quadrivium, and analyzes "
            "Limit (peras) and pure geometric beauty in the Philebus."
        ),
    },
    "meno": {
        "name": "Meno of Pharsalus",
        "dates": "c. 423 – 400 BC",
        "role": "Thessalian Aristocrat & Interlocutor of the Meno",
        "bio": (
            "Raises the celebrated paradox of inquiry (Meno 80d), prompting Socrates' geometric "
            "demonstration of recollection on his Greek-speaking household attendant and the "
            "method of inquiry from hypothesis."
        ),
    },
    "theodorus": {
        "name": "Theodorus of Cyrene",
        "dates": "c. 465 – 398 BC",
        "role": "Pythagorean Geometer & Teacher of Plato and Theaetetus",
        "bio": (
            "Proved case-by-case via diagrams that the sides of squares of 3, 5, ..., 17 square "
            "feet are incommensurable in length with the 1-foot unit (Theaetetus 147d)."
        ),
    },
    "theaetetus": {
        "name": "Theaetetus of Athens",
        "dates": "c. 417 – 369 BC",
        "role": "Academic Geometer of Irrational Powers & the Five Regular Solids",
        "bio": (
            "Generalized Theodorus's surds into the universal classification of lengths (mēkē) and "
            "powers (dynameis), founded the theory of medial/binomial/apotome irrationals (Euclid "
            "Book X), and first constructed all five regular polyhedra (Euclid Book XIII)."
        ),
    },
    "glaucon": {
        "name": "Glaucon of Athens",
        "dates": "c. 445 – 4th c. BC",
        "role": "Elder Brother of Plato & Interlocutor of Republic Books VI–VII",
        "bio": (
            "Converse partner with Socrates throughout the Divided Line (509d–511e) and the "
            "mathematical curriculum of the Quadrivium (525a–534e)."
        ),
    },
    "timaeus": {
        "name": "Timaeus of Locri",
        "dates": "5th c. BC (dramatic persona)",
        "role": "Italic Pythagorean Astronomer-Statesman & Speaker of the Timaeus",
        "bio": (
            "Expounds the geometric proportion binding the four elements, the harmonic division "
            "of the World-Soul (31b–36d), and the reconstruction of physical bodies from "
            "elementary isosceles and scalene right triangles (53c–56c)."
        ),
    },
    "parmenides": {
        "name": "Parmenides of Elea",
        "dates": "fl. early 5th c. BC",
        "role": "Founder of Eleatic Ontology & Speaker of the Eight Hypotheses",
        "bio": (
            "Conducts the dialectical exercise of Parmenides 137c–166c, articulating the "
            "foundational definitions of equidistant roundness and optical straightness (137e, 145b)."
        ),
    },
    "protarchus": {
        "name": "Protarchus of Athens",
        "dates": "late 5th c. BC",
        "role": "Interlocutor of the Philebus",
        "bio": (
            "Examines with Socrates the fourfold ontology of Limit, Unlimited, Mixture, and Cause "
            "(16c–26d) and the pure beauty of compass-and-straightedge forms (51b–52c)."
        ),
    },
    "athenian-stranger": {
        "name": "The Athenian Stranger",
        "dates": "4th c. BC (dramatic persona)",
        "role": "Philosophical Legislator of the Laws",
        "bio": (
            "Denounces Greek pedagogical ignorance of three-dimensional incommensurability in "
            "Laws VII (817e–820d) before Clinias of Crete and Megillus of Sparta."
        ),
    },
    "pythagoras": {
        "name": "Pythagoras & the Italic Pythagoreans",
        "dates": "6th – 4th c. BC",
        "role": "Pioneers of Harmonic Ratios, Figurate Numbers & Application of Areas",
        "bio": (
            "Discovered the diatonic ratios (2:1, 3:2, 4:3, 9:8, 256:243), the application of "
            "areas, and quadratic incommensurability; commended in Republic VII 530d as treating "
            "astronomy and harmonics as sister sciences."
        ),
    },
    "archytas": {
        "name": "Archytas of Tarentum",
        "dates": "c. 428 – 347 BC",
        "role": "Pythagorean Geometer, Theorist of the Three Means & Friend of Plato",
        "bio": (
            "Defined the arithmetic, geometric, and harmonic means in music (DK 47 B2), proved "
            "no superparticular ratio (n+1):n admits a rational mean proportional, and solved "
            "the doubling of the cube in three dimensions by intersecting a cylinder, torus, and cone."
        ),
    },
    "eudoxus": {
        "name": "Eudoxus of Cnidus",
        "dates": "c. 390 – c. 337 BC",
        "role": "Academic Geometer of General Proportion & Method of Exhaustion",
        "bio": (
            "Answered Plato's challenges with the general theory of proportion valid for "
            "commensurable and incommensurable magnitudes alike (Euclid Book V) and rigorous "
            "stereometric volume theorems (Euclid Book XII)."
        ),
    },
    "aristotle": {
        "name": "Aristotle of Stagira",
        "dates": "384 – 322 BC",
        "role": "Student of Plato & Author of the Analytics, Physics, De Caelo & Metaphysics",
        "bio": (
            "Preserves vital testimony on Plato's mathematical intermediates (ta mathēmatika), "
            "resolves Meno's paradox in Posterior Analytics I.1, and critiques the Timaeus "
            "planar-triangle physics in De Caelo III.7–8."
        ),
    },
    "euclid": {
        "name": "Euclid of Alexandria",
        "dates": "fl. c. 300 BC",
        "role": "Author of the Thirteen Books of Elements",
        "bio": (
            "Systematized the geometric heritage of Plato's Academy, culminating in Book X "
            "(Theaetetus's irrationals) and Book XIII (construction and uniqueness of the five "
            "Platonic cosmic polyhedra, praised by Proclus as the telos of the Elements)."
        ),
    },
    "crantor": {
        "name": "Crantor of Soli",
        "dates": "c. 335 – 275 BC",
        "role": "Old Academic First Exegete of Plato's Timaeus",
        "bio": (
            "Introduced the lambda (Λ) arrangement of the doubles (1, 2, 4, 8) and triples "
            "(1, 3, 9, 27) and the least integer base 384 clearing all fractions of the "
            "34-term World-Soul diatonic scale."
        ),
    },
    "proclus": {
        "name": "Proclus Diadochus",
        "dates": "412 – 485 AD",
        "role": "Neoplatonic Diadochus & Commentator on Euclid I and Plato's Timaeus",
        "bio": (
            "Wove Philebus's Limit/Unlimited, Republic's Divided Line (dianoia), Meno's "
            "anamnesis, and Timaeus's polyhedra into the Prologue of his Commentary on the "
            "First Book of Euclid's Elements."
        ),
    },
    "thomas-aquinas": {
        "name": "St. Thomas Aquinas",
        "dates": "1225 – 1274",
        "role": "Scholastic Doctor of Mathematical Abstraction & Judgment",
        "bio": (
            "Synthesized Platonic-Aristotelian mathematical epistemology through abstraction in "
            "intelligible matter and resolution to imagination (resolutio ad imaginationem)."
        ),
    },
    "pacioli": {
        "name": "Fra Luca Pacioli",
        "dates": "c. 1447 – 1517",
        "role": "Renaissance Mathematician & Author of De Divina Proportione (1509)",
        "bio": (
            "Celebrated Timaeus 53c–56c across nine chapters of De Divina Proportione, pairing "
            "Leonardo da Vinci's skeletal polyhedral plates with Euclid Book XIII and the golden ratio."
        ),
    },
    "burnet": {
        "name": "John Burnet",
        "dates": "1863 – 1928",
        "role": "Editor of the Oxford Classical Text Platonis Opera (1900–1907)",
        "bio": (
            "Scottish classicist at St Andrews whose five-volume Clarendon Press critical edition "
            "established the authoritative modern Greek text and Stephanus apparatus of Plato."
        ),
    },
    "jowett": {
        "name": "Benjamin Jowett",
        "dates": "1817 – 1893",
        "role": "Master of Balliol College, Oxford & Translator of The Dialogues of Plato",
        "bio": (
            "Produced the monumental five-volume English translation of Plato (3rd revised "
            "edition, 1892), staged in the English track of this Codex alongside corrective "
            "mathematical philology notes."
        ),
    },
    "heath": {
        "name": "Sir Thomas Little Heath",
        "dates": "1861 – 1940",
        "role": "Historian of Greek Mathematics & Editor of Euclid's Elements",
        "bio": (
            "Author of A History of Greek Mathematics (1921) and The Thirteen Books of Euclid's "
            "Elements (1926), reconstructing Meno 86e–87b, Theodorus's proofs, and Timaeus's astronomy."
        ),
    },
    "hoenen": {
        "name": "Fr. Petrus H. J. Hoenen, S.J.",
        "dates": "1880 – 1961",
        "role": "Gregorian University Philosopher of Science & Author of De Noetica Geometriae (1952)",
        "bio": (
            "Analyzed Meno 82b–85b and Republic VI–VII as perennial witnesses to intellectual "
            "insight into geometric necessity within the singular diagram."
        ),
    },
}

CITATIONS_DATA: dict[str, dict[str, str]] = {
    "burnet:opera:1900": {
        "author": "Burnet, John (ed.)",
        "work": "Platonis Opera, recognovit brevique adnotatione critica instruxit Ioannes Burnet, Tomi I–V (Oxford: Clarendon Press, 1900–1907)",
        "locus": "Tomi I–V",
        "notes": "Authoritative Oxford Classical Text staged verbatim in the Greek (el) track via Perseus Canonical GreekLit TEI-XML.",
    },
    "jowett:dialogues:1892": {
        "author": "Jowett, Benjamin (trans.)",
        "work": "The Dialogues of Plato, Translated into English with Analyses and Introductions, 3rd ed., 5 vols. (Oxford: Clarendon Press, 1892)",
        "locus": "Vols. I–V",
        "notes": "Public-domain English translation staged in the English (en) track with exact mathematical philology notes.",
    },
    "stephanus:1578": {
        "author": "Estienne, Henri (Henricus Stephanus, ed.)",
        "work": "Platonis opera quae extant omnia, 3 vols. (Geneva, 1578)",
        "locus": "Vols. I–III (a–e sections)",
        "notes": "Universal pagination and five-section column standard (a–e) governing all Platonic references.",
    },
    "euclid:elements": {
        "author": "Euclid of Alexandria",
        "work": "Στοιχεῖα — The Thirteen Books of Euclid's Elements (ed. Heiberg 1883–1888; trans. Heath 1926)",
        "locus": "Books I–XIII",
        "notes": "Deductive culmination of the fourth-century Academic curriculum (geometor/euclid & geometor/elements).",
    },
    "euclid:I.def.4": {
        "author": "Euclid",
        "work": "Elements, Book I, Definitions 4 & 15 (Straight Line & Circle)",
        "locus": "I, Defs. 4, 15",
        "notes": "Euclidean counterpart to Plato's optical straightness and equidistant roundness in Parmenides 137e.",
    },
    "euclid:I.def.13": {
        "author": "Euclid",
        "work": "Elements, Book I, Definitions 13–14 & Book XI, Definition 2 (Boundary, Figure & Solid)",
        "locus": "I, Defs. 13–14; XI, Def. 2",
        "notes": "Formalizes Socrates' definition of figure as limit (peras) in Meno 76a.",
    },
    "euclid:I.1": {
        "author": "Euclid",
        "work": "Elements, Book I, Proposition 1 (Equilateral Triangle Construction)",
        "locus": "I.1",
        "notes": "Constructs the cosmic equilateral face bisected into six Timaeus 1:√3:2 half-triangles.",
    },
    "euclid:I.11": {
        "author": "Euclid",
        "work": "Elements, Book I, Propositions 11–12 (Perpendicular Lines)",
        "locus": "I.11–12",
        "notes": "Erects orthogonal legs in Meno's square, Theodorus's spiral, and the Divided Line mean ordinate.",
    },
    "euclid:I.46": {
        "author": "Euclid",
        "work": "Elements, Book I, Proposition 46 (Construction of a Square)",
        "locus": "I.46",
        "notes": "Constructs the given square ABCD and diagonal square BHKD in Meno 82b–85b.",
    },
    "euclid:I.47": {
        "author": "Euclid",
        "work": "Elements, Book I, Proposition 47 (Pythagorean Theorem)",
        "locus": "I.47",
        "notes": "General theorem generalizing Socrates' isosceles case Q = 4 + 4 = 8 and iterating Theodorus's spiral Q_{n+1} = Q_n + 1.",
    },
    "euclid:II.11": {
        "author": "Euclid",
        "work": "Elements, Book II, Proposition 11 & Book VI, Proposition 30 (Extreme and Mean Ratio)",
        "locus": "II.11, VI.30",
        "notes": "Canonical Academic 'section' (ἡ τομή) realizing the Divided Line under golden ratio φ.",
    },
    "euclid:II.14": {
        "author": "Euclid",
        "work": "Elements, Book II, Proposition 14 & Book VI, Proposition 13 (Quadrature & Mean Proportional)",
        "locus": "II.14, VI.13",
        "notes": "Semicircle ordinate construction of quadratic powers √n (Theaetetus 147d) and geometric mean √(ab) (Timaeus 32a).",
    },
    "euclid:V.def.5": {
        "author": "Euclid (Eudoxus)",
        "work": "Elements, Book V, Definition 5 & Proposition 16 (General Theory of Proportion)",
        "locus": "V, Def. 5; V.16",
        "notes": "Proves alternation (A:B = C:D => A:C = B:D) required for the Divided Line equality ``|BC| = |CD|`` even for irrational ratios.",
    },
    "euclid:VI.28": {
        "author": "Euclid",
        "work": "Elements, Book VI, Propositions 27–28 (Elliptic Application of Areas & Diorismos)",
        "locus": "VI.27–28",
        "notes": "Exact Euclidean counterpart to Socrates' hypothesis of applying an area with similar defect in Meno 87a.",
    },
    "euclid:VII.def.16": {
        "author": "Euclid",
        "work": "Elements, Book VII, Definitions 16–19 (Plane, Solid, Square & Oblong Numbers)",
        "locus": "VII, Defs. 16–19",
        "notes": "Preserves Theaetetus's arithmetic distinction between equilateral square and oblong numbers (147e–148a).",
    },
    "euclid:VIII.11": {
        "author": "Euclid",
        "work": "Elements, Book VIII, Propositions 11–12 (Means Between Square and Cube Numbers)",
        "locus": "VIII.11–12",
        "notes": "Demonstrates Timaeus 32a–b: one mean proportional between two squares, two means between two cubes.",
    },
    "euclid:X.def.1": {
        "author": "Euclid (Theaetetus)",
        "work": "Elements, Book X, Definitions 1–4 & Proposition 9 (Commensurability in Length vs. Square)",
        "locus": "X, Defs. 1–4; X.9",
        "notes": "Codifies Theaetetus 147d–148b: squares have commensurable sides iff their areas have the ratio of square numbers.",
    },
    "euclid:XIII.13": {
        "author": "Euclid (Theaetetus)",
        "work": "Elements, Book XIII, Propositions 13–18 (Construction & Exhaustive Comparison of the Five Cosmic Solids)",
        "locus": "XIII.13–18",
        "notes": "Inscribes tetrahedron, octahedron, cube, icosahedron, and dodecahedron in a sphere and proves no sixth regular polyhedron can exist (cf. Timaeus 54d–55c).",
    },
    "proclus:in-euclidem": {
        "author": "Proclus Diadochus",
        "work": "In Primum Euclidis Elementorum Librum Commentarii (ed. Friedlein 1873; trans. Morrow 1970)",
        "locus": "Friedlein pp. 1–436",
        "notes": "Neoplatonic mathematical synthesis linking Philebus, Republic VI–VII, Meno, Parmenides, and Timaeus to Euclid Book I (geometor/proclus).",
    },
    "proclus:in-timaeum": {
        "author": "Proclus Diadochus",
        "work": "In Platonis Timaeum Commentaria, ed. Ernst Diehl, 3 vols. (Leipzig: Teubner, 1903–1906)",
        "locus": "Vol. II, pp. 167–236 (on Tim. 35a–36d)",
        "notes": "Preserves Crantor's base-384 integer table and verifies the 34-pitch Timaeus World-Soul scale.",
    },
    "aristotle:anal-post": {
        "author": "Aristotle",
        "work": "Analytica Posteriora, Book I (Bekker 71a1–89b20)",
        "locus": "71a29, 76b39, 77b30",
        "notes": "Engages Meno's paradox and Republic's doctrine of mathematical hypotheses and diagrams (geometor/aristotle).",
    },
    "aristotle:metaphysics": {
        "author": "Aristotle",
        "work": "Metaphysica, Books A.6, B.2, M.1–3 (ed. Ross 1924)",
        "locus": "987b14–18, 997b, 1076a–1078b",
        "notes": "Primary witness for Plato's doctrine of mathematical intermediates (ta mathēmatika) between Forms and sensibles.",
    },
    "aristotle:de-caelo": {
        "author": "Aristotle",
        "work": "De Caelo, Book III, Chapters 7–8 (Bekker 305b28–307b24)",
        "locus": "306a1–307b18",
        "notes": "Critiques Timaeus 53c–56c on generating three-dimensional bodies from weightless planar triangles.",
    },
    "heath:greek-math:1921": {
        "author": "Heath, Sir Thomas Little",
        "work": "A History of Greek Mathematics, Vol. I: From Thales to Euclid (Oxford: Clarendon Press, 1921)",
        "locus": "Vol. I, Ch. IX ('Plato', pp. 284–315) & pp. 202–212",
        "notes": "Standard reconstruction of Meno's geometric hypothesis, Theodorus's √3..√17 methods, and the Timaeus scale.",
    },
    "heath:euclid:1926": {
        "author": "Heath, Sir Thomas Little",
        "work": "The Thirteen Books of Euclid's Elements, 2nd ed., 3 vols. (Cambridge University Press, 1926)",
        "locus": "Vols. I–III",
        "notes": "Exhaustive commentary reconciling all 21 Plato citations in geometor/euclid and geometor/elements.",
    },
    "taylor:timaeus:1928": {
        "author": "Taylor, A. E.",
        "work": "A Commentary on Plato's Timaeus (Oxford: Clarendon Press, 1928)",
        "locus": "pp. 92–164, 362–388",
        "notes": "Detailed mathematical analysis of the World-Soul harmonic intervals and cosmic polyhedra.",
    },
    "cornford:timaeus:1937": {
        "author": "Cornford, Francis Macdonald",
        "work": "Plato's Cosmology: The Timaeus of Plato Translated with a Running Commentary (London: Routledge, 1937)",
        "locus": "pp. 43–93, 210–230",
        "notes": "Clarifies the band construction of the Circles of the Same and the Different and the planar triangle assemblies.",
    },
    "pacioli:divina:1509": {
        "author": "Pacioli, Fra Luca",
        "work": "De Divina Proportione (Venice: Paganino Paganini, 1509)",
        "locus": "Compendio Caps. V, XXV–LV",
        "notes": "Renaissance synthesis of Timaeus 53c–56c and Euclid Book XIII (geometor/pacioli).",
    },
    "hoenen:noetica:1952": {
        "author": "Hoenen, Petrus H. J., S.J.",
        "work": "De Noetica Geometriae: Origine Theoriae Cognitionis (Rome: Analecta Gregoriana 63, 1954)",
        "locus": "Caps. I, IV, VII",
        "notes": "Scholastic-noetic analysis of Meno 82b–85b, Republic VI–VII, and Laws V 737e (geometor/hoenen).",
    },
    "knorr:evolution:1975": {
        "author": "Knorr, Wilbur Richard",
        "work": "The Evolution of the Euclidean Elements: A Study of the Theory of Incommensurable Magnitudes and Its Significance for Early Greek Geometry (Dordrecht: Reidel, 1975)",
        "locus": "Chs. III–VIII",
        "notes": "Definitive modern study of Theodorus's stopping-point at √17 and Theaetetus's theory of quadratic powers.",
    },
}


def _slug_anchor(prefix: str, key: str) -> str:
    """Convert an apparatus key into a clean RST anchor token."""
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", key).strip("-").lower()
    return f"{prefix}-{cleaned}"


def render_glossary_rst() -> str:
    """Render ``docsrc/loci_mathematici/glossary.rst``."""
    lines = [
        ":order: 93",
        ":layout: book",
        ":type: apparatus",
        ":title: Glossary of Platonic Mathematical & Noetic Terms",
        "",
        ".. _glossary:",
        "",
        "================================================",
        "Glossary of Platonic Mathematical & Noetic Terms",
        "================================================",
        "",
        ".. rubric:: Polytonic Greek, Scholastic Latin & Mathematical Lexicon of *Loci Mathematici et Geometrici*",
        "",
        (
            f"Systematic lexicon of **{len(GLOSSARY_DATA)} foundational Platonic concepts** "
            "governing geometric figure (*schēma*), quadratic powers (*dynameis*), discursive "
            "mathematical thought (*dianoia*), harmonic proportion (*analogia*), elementary "
            "triangles (*stoicheia*), and Limit (*peras*)."
        ),
        "",
    ]
    for key, entry in GLOSSARY_DATA.items():
        head = entry["headword"]
        lines.extend(
            [
                f".. _{_slug_anchor('term', key)}:",
                "",
                head,
                "-" * len(head),
                "",
                f"- **Greek**: *{entry['greek']}*  |  **Latin**: *{entry['latin']}*",
                f"- **Rendering**: {entry['translation']}",
                f"- **Primary Stephanus Loci**: ``{entry['loci']}``",
                "",
                entry["definition"],
                "",
            ]
        )
    return "\n".join(lines)


def render_persons_rst() -> str:
    """Render ``docsrc/loci_mathematici/persons.rst``."""
    lines = [
        ":order: 92",
        ":layout: book",
        ":type: apparatus",
        ":title: Index of Persons, Interlocutors & Commentators",
        "",
        ".. _persons:",
        "",
        "==============================================",
        "Index of Persons, Interlocutors & Commentators",
        "==============================================",
        "",
        ".. rubric:: Academic Geometers, Dramatic Interlocutors, Ancient Exegetes & Modern Editors",
        "",
        (
            f"Biographical register of **{len(PERSONS_DATA)} philosophers, mathematicians, "
            "dialogue interlocutors, commentators, and modern philologists** engaged across "
            "*Loci Mathematici et Geometrici* and the GEOMETOR canon."
        ),
        "",
    ]
    for key, entry in PERSONS_DATA.items():
        heading = f"{entry['name']} ({entry['dates']})"
        lines.extend(
            [
                f".. _{_slug_anchor('person', key)}:",
                "",
                heading,
                "-" * len(heading),
                "",
                f"**{entry['role']}**",
                "",
                entry["bio"],
                "",
            ]
        )
    return "\n".join(lines)


def render_bibliography_rst() -> str:
    """Render ``docsrc/loci_mathematici/bibliography.rst``."""
    lines = [
        ":order: 91",
        ":layout: book",
        ":type: apparatus",
        ":title: Bibliography & Critical Editions",
        "",
        ".. _bibliography:",
        "",
        "================================",
        "Bibliography & Critical Editions",
        "================================",
        "",
        ".. rubric:: Critical Greek Texts, Public-Domain Translations, Euclidean Propositions & Commentaries",
        "",
        (
            f"Authoritative editions, Euclidean propositions, ancient commentaries, and "
            f"modern mathematical histories (**{len(CITATIONS_DATA)} entries**) cited across "
            "*Loci Mathematici et Geometrici*."
        ),
        "",
    ]
    for key, entry in CITATIONS_DATA.items():
        lines.extend(
            [
                f".. _{_slug_anchor('cite', key)}:",
                "",
                f"**{entry['author']} — {entry['work']}**",
                "",
                f"- **Citation Key**: ``{key}``  |  **Locus**: ``{entry['locus']}``",
                f"- **Significance**: {entry['notes']}",
                "",
            ]
        )
    return "\n".join(lines)


def write_apparatus_artifacts(repo_root: str | Path) -> dict[str, Path]:
    """Write ``glossary.json``, ``persons.json``, ``citations.json`` & apparatus ``.rst`` pages."""
    root = Path(repo_root)
    written: dict[str, Path] = {}

    json_payloads = {
        "glossary.json": GLOSSARY_DATA,
        "persons.json": PERSONS_DATA,
        "citations.json": CITATIONS_DATA,
    }

    for filename, payload in json_payloads.items():
        for folder in (root / "resources", root / "resources" / "loci_mathematici"):
            folder.mkdir(parents=True, exist_ok=True)
            target = folder / filename
            target.write_text(
                json.dumps(payload, indent=2, ensure_ascii=False) + "\n",
                encoding="utf-8",
            )
            written[str(target.relative_to(root))] = target

    rst_dir = root / "docsrc" / "loci_mathematici"
    rst_dir.mkdir(parents=True, exist_ok=True)
    for filename, content in (
        ("glossary.rst", render_glossary_rst()),
        ("persons.rst", render_persons_rst()),
        ("bibliography.rst", render_bibliography_rst()),
    ):
        target = rst_dir / filename
        target.write_text(content, encoding="utf-8")
        written[str(target.relative_to(root))] = target

    return written
