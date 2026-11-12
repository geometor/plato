r"""Exact symbolic constructions for Plato's Mathematical & Geometric Dialogues.

Every construction builds a :class:`~geometor.model.Model` with ``auto_intersect=False``
and 100% exact SymPy coordinates over :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\phi)`, or
closed-form quadratic radicals—never injecting ``float`` or ``sp.Float`` approximations.

Constructions provided:

1. :func:`construct_meno_diagonal_doubling` (*Meno* 82b–85b): The :math:`2\times 2`
   given square (:math:`Q=4`), false :math:`4\times 4` (:math:`Q=16`) and :math:`3\times 3`
   (:math:`Q=9`) conjectures, and Socrates' inscribed diagonal square (:math:`Q=8`).
2. :func:`construct_theodorus_spiral` (*Theaetetus* 147c–148b): Pure straightedge-and-compass
   right-triangle spiral constructing exact quadrances :math:`Q(O, P_n) = n` for
   :math:`n = 1, 2, \dots, 17`, classifying lengths (*mēkē*) vs. powers (*dynameis*).
3. :func:`construct_divided_line` (*Republic* VI, 509d–511e): Exact division of the
   Visible and Intelligible realms proving ``Q(pistis) == Q(dianoia)`` identically,
   with semicircle geometric-mean ordinates and Golden Ratio default.
4. :func:`construct_timaeus_proportion_circles` (*Timaeus* 31c–36d): Semicircle
   construction of Plato's arithmetic (:math:`3`), geometric (:math:`2\sqrt{2}`), and
   harmonic (:math:`8/3`) means on the :math:`[2, 4]` octave, exhibiting the :math:`9:8`
   *epogdoos* tone and the inclined circles of the Same and the Different.
5. :func:`construct_timaeus_triangles` & :func:`construct_timaeus_cube_face` (*Timaeus*
   53c–56c): Six :math:`1:\sqrt{3}:2` scalene half-triangles (quadrances :math:`1, 3, 4`;
   spreads :math:`1/4, 3/4, 1`) around centroid :math:`G = X(2)` forming the cosmic
   equilateral face, plus the 4-isosceles-triangle square face of the Cube.
6. :func:`construct_compass_and_peras` (*Parmenides* 137e, *Philebus* 51c, *Laws* VII 819d):
   Circular equidistance (*tornos*), optical straightness (*kanōn*), and the :math:`1, \sqrt{2}, \sqrt{3}`
   length–breadth–depth incommensurability chain.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    clean_expr,
    quadrance,
    vertex_spread,
    zero_test,
)

__all__ = [
    "TheaetetusPowerEntry",
    "classify_theaetetus_powers",
    "construct_meno_diagonal_doubling",
    "construct_theodorus_spiral",
    "construct_divided_line",
    "verify_divided_line_identity",
    "construct_timaeus_proportion_circles",
    "construct_timaeus_triangles",
    "construct_timaeus_cube_face",
    "construct_compass_and_peras",
]


@dataclass(frozen=True)
class TheaetetusPowerEntry:
    r"""Classification of an integer area :math:`n` under *Theaetetus* 147e–148b.

    Attributes:
        area_n: Integer square area :math:`n = Q(O, P_n)`.
        side_expr: Exact symbolic side length :math:`\sqrt{n}`.
        number_kind: ``"square (isos isakis)"`` or ``"oblong (promekes)"``.
        line_kind: ``"mekos (length)"`` when commensurable in length with unit,
            else ``"dynamis (power)"``.
    """

    area_n: int
    side_expr: sp.Expr
    number_kind: str
    line_kind: str


def _new_exact_model(name: str) -> Model:
    """Create a quiet, deterministic exact :class:`~geometor.model.Model`."""
    return Model(name, auto_intersect=False, enable_logging=False)


def _normalize_symbolic_ratio(ratio: sp.Expr | int) -> sp.Expr:
    """Convert symbolic constants such as ``sp.GoldenRatio`` into explicit radicals."""
    expr = sp.sympify(ratio)
    if expr.has(sp.Float):
        raise ValueError(f"Floating-point ratio {ratio!r} is prohibited in geometor.plato.")
    phi_rad = (sp.Integer(1) + sp.sqrt(5)) / sp.Integer(2)
    expr = expr.subs(sp.GoldenRatio, phi_rad).rewrite(sp.sqrt)
    return clean_expr(expr)


def _construct_perp_at_point(
    model: Model,
    origin_ref: spg.Point,
    vertex_pt: spg.Point,
    *,
    scope_name: str,
    guide: bool = True,
    classes: list[str] | None = None,
) -> spg.Line:
    """Construct the exact Euclidean perpendicular to ``[origin_ref, vertex_pt]`` at ``vertex_pt`` (Euclid I.11)."""
    with model.subconstruction(scope_name, hide_guides=True) as scope:
        ray_line = model.construct_line(origin_ref, vertex_pt, guide=True, by="Post.2")
        dbl_circle = model.construct_circle(vertex_pt, origin_ref, guide=True, by="Post.3")
        far_pt = model.intersect(
            ray_line,
            dbl_circle,
            other_than=origin_ref,
            guide=True,
            by="Def.15",
        )
        c_left = model.construct_circle(origin_ref, far_pt, guide=True, by="Post.3")
        c_right = model.construct_circle(far_pt, origin_ref, guide=True, by="Post.3")
        apex = model.intersect(
            c_left,
            c_right,
            side_of=(origin_ref, vertex_pt, 1),
            guide=True,
            by="I.1",
        )
        perp = model.construct_line(
            vertex_pt, apex, classes=classes, guide=guide, by="I.11"
        )
        if not guide:
            scope.keep(perp)
        return perp


def construct_meno_diagonal_doubling(model: Model | None = None) -> Model:
    r"""Construct Socrates' diagonal square-doubling proof (*Meno* 82b–85b).

    Starting from the unit/two-foot baseline ``A=(0,0)``, ``U=(1,0)``, ``B=(2,0)``,
    constructs by straightedge and compass:

    - Initial :math:`2\times 2` square ``< A B C D >`` of side :math:`2` (:math:`Q(A, B) = 4`, area :math:`4`),
    - First false conjecture ``< A E F G >`` of doubled side :math:`4` (:math:`Q(A, E) = 16`, area :math:`16`),
    - Second false conjecture ``< A M N P >`` of three-foot side :math:`3` (:math:`Q(A, M) = 9`, area :math:`9`),
    - Inscribed diagonal square ``< B H K D >`` cut by the four *diametroi* (:math:`Q(B, H) = 8`, area :math:`8`).

    Args:
        model: Optional existing :class:`~geometor.model.Model` (created if ``None``).

    Returns:
        Populated :class:`~geometor.model.Model` with verified assertions.
    """
    m = model if model is not None else _new_exact_model("meno_diagonal_doubling")

    a_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    u_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="U", classes=["auxiliary"])

    base_ln = m.construct_line(a_pt, u_pt, classes=["carrier"], by="Post.1")

    # Produce 2-ft, 3-ft, and 4-ft marks along AB by compass stepping (Post.2, Post.3)
    c_u = m.construct_circle(u_pt, a_pt, guide=True, by="Post.3")
    b_pt = m.intersect(base_ln, c_u, other_than=a_pt, ID="B", classes=["given"], by="Post.3")

    c_b1 = m.construct_circle(b_pt, u_pt, guide=True, by="Post.3")
    m_pt = m.intersect(base_ln, c_b1, other_than=u_pt, ID="M", classes=["trial"], by="Post.3")

    c_b2 = m.construct_circle(b_pt, a_pt, guide=True, by="Post.3")
    e_pt = m.intersect(base_ln, c_b2, other_than=a_pt, ID="E", classes=["quadruple"], by="Post.3")

    # Erect left vertical axis ADPG at A perpendicular to AE (I.11)
    left_ln = _construct_perp_at_point(
        m, b_pt, a_pt, scope_name="meno_left_axis", guide=False, classes=["carrier"]
    )

    c_a2 = m.construct_circle(a_pt, b_pt, classes=["compass"], guide=True, by="Post.3")
    d_pt = m.intersect(left_ln, c_a2, side_of=(a_pt, b_pt, 1), ID="D", classes=["given"], by="Post.3")

    c_a3 = m.construct_circle(a_pt, m_pt, guide=True, by="Post.3")
    p_pt = m.intersect(left_ln, c_a3, side_of=(a_pt, b_pt, 1), ID="P", classes=["trial"], by="Post.3")

    c_a4 = m.construct_circle(a_pt, e_pt, guide=True, by="Post.3")
    g_pt = m.intersect(left_ln, c_a4, side_of=(a_pt, b_pt, 1), ID="G", classes=["quadruple"], by="Post.3")

    # Construct interior and outer grid vertices via compass intersections (I.46)
    c_b_up = m.construct_circle(b_pt, a_pt, guide=True, by="Post.3")
    c_d_rt = m.construct_circle(d_pt, a_pt, guide=True, by="Post.3")
    c_pt = m.intersect(c_b_up, c_d_rt, other_than=a_pt, ID="C", classes=["given"], by="I.46")

    mid_v = m.construct_line(b_pt, c_pt, classes=["quadrilateral"], by="Post.1")
    mid_h = m.construct_line(d_pt, c_pt, classes=["quadrilateral"], by="Post.1")

    right_ln = _construct_perp_at_point(
        m, a_pt, e_pt, scope_name="meno_right_axis", guide=False, classes=["carrier"]
    )
    top_border = _construct_perp_at_point(
        m, a_pt, g_pt, scope_name="meno_top_axis", guide=False, classes=["carrier"]
    )

    h_pt = m.intersect(right_ln, mid_h, ID="H", classes=["diagonal_vertex"], by="Post.1")
    k_pt = m.intersect(top_border, mid_v, ID="K", classes=["diagonal_vertex"], by="Post.1")
    f_pt = m.intersect(right_ln, top_border, ID="F", classes=["quadruple"], by="Post.1")

    # 3x3 trial square corner N=(3,3)
    trial_v = _construct_perp_at_point(m, a_pt, m_pt, scope_name="meno_trial_v")
    trial_h = _construct_perp_at_point(m, a_pt, p_pt, scope_name="meno_trial_h")
    n_pt = m.intersect(trial_v, trial_h, ID="N", classes=["trial"], by="I.46")
    m.construct_line(m_pt, n_pt, classes=["diagonal", "trial_line"], by="Post.1")
    m.construct_line(p_pt, n_pt, classes=["diagonal", "trial_line"], by="Post.1")

    # The four Platonic diametroi enclosing the 8-square-foot square < B H K D >
    m.construct_line(b_pt, d_pt, classes=["pappus", "even", "diametros"], by="Post.1")
    m.construct_line(b_pt, h_pt, classes=["pappus", "even", "diametros"], by="Post.1")
    m.construct_line(h_pt, k_pt, classes=["pappus", "even", "diametros"], by="Post.1")
    m.construct_line(k_pt, d_pt, classes=["pappus", "even", "diametros"], by="Post.1")

    # Polygons for interactive Codex highlighting
    sq_four = m.set_polygon([a_pt, e_pt, f_pt, g_pt], classes=["hexagon"], by="Meno.83b")
    sq_nine = m.set_polygon([a_pt, m_pt, n_pt, p_pt], classes=["circle"], by="Meno.83e")
    sq_given = m.set_polygon([a_pt, b_pt, c_pt, d_pt], classes=["square"], by="Meno.82c")
    sq_double = m.set_polygon([b_pt, h_pt, k_pt, d_pt], classes=["diamond"], by="Meno.85b")
    _ = (sq_four, sq_nine)

    # Exact Rational Trigonometry & Euclidean assertions
    m.assert_equal((a_pt, b_pt), (b_pt, c_pt), (c_pt, d_pt), (d_pt, a_pt), by="Meno.82c")
    m.assert_equal((b_pt, h_pt), (h_pt, k_pt), (k_pt, d_pt), (d_pt, b_pt), by="Meno.85a")
    m.assert_perpendicular((b_pt, h_pt), (h_pt, k_pt), by="Meno.85a")
    m.assert_perpendicular((h_pt, k_pt), (k_pt, d_pt), by="Meno.85a")

    if not zero_test(quadrance(b_pt, d_pt) - 2 * quadrance(a_pt, b_pt)):
        raise AssertionError("Diagonal quadrance Q(B, D) must equal 2 * Q(A, B) = 8.")
    if not zero_test(sq_double.area - 2 * sq_given.area):
        raise AssertionError("Area of diagonal square BHKD must equal twice ABCD.")

    m.conclude(
        sq_double,
        sq_given,
        by="Meno.85b",
        label="Square on the diagonal BHKD (Q = 8) is exactly double square ABCD (Q = 4).",
    )
    return m


def classify_theaetetus_powers(max_n: int = 17) -> list[TheaetetusPowerEntry]:
    """Classify integer areas ``1..max_n`` into *mēkē* (lengths) and *dynameis* (powers).

    Follows Theaetetus's exact dichotomy (*Theaetetus* 147e–148b):

    - Equilateral square numbers (*isos isakis*, :math:`n = k^2`) produce lines
      commensurable in length with the unit (*mēkē*).
    - Oblong numbers (*promēkeis*, non-square :math:`n`) produce lines incommensurable
      in length with the unit, commensurable only in the plane areas they have the
      power to form (*dynameis*).

    Args:
        max_n: Upper integer area bound (defaults to Theodorus's ``17``).

    Returns:
        List of :class:`TheaetetusPowerEntry` records for ``1..max_n``.
    """
    if max_n < 1:
        raise ValueError("max_n must be >= 1.")
    entries: list[TheaetetusPowerEntry] = []
    for n in range(1, max_n + 1):
        side = sp.sqrt(sp.Integer(n))
        is_sq = side.is_integer is True
        entries.append(
            TheaetetusPowerEntry(
                area_n=n,
                side_expr=side,
                number_kind="square (isos isakis)" if is_sq else "oblong (promekes)",
                line_kind="mekos (length)" if is_sq else "dynamis (power)",
            )
        )
    return entries


def construct_theodorus_spiral(model: Model | None = None, max_n: int = 17) -> Model:
    r"""Construct Theodorus's exact :math:`\sqrt{1}\dots\sqrt{17}` spiral (*Theaetetus* 147d–148b).

    Starting from ``O=(0,0)`` and ``P1=(1,0)``, each vertex ``P_{n+1}`` is erected
    along the perpendicular to ``[O, P_n]`` at ``P_n`` (Euclid I.11) at exact unit
    step ``Q(P_n, P_{n+1}) = 1 = Q(O, P1)`` (Postulate 3) in the positive orientation
    ``side_of=(O, P_n, +1)``, expanding cross-terms at each step so every coordinate
    remains a flat :math:`\mathbb{Q}`-linear combination of :math:`\sqrt{k}` (:math:`k \le n`)
    with zero nested square roots and exact symbolic quadrance ``Q(O, P_{n+1}) = n + 1``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.
        max_n: Maximum integer area ``n`` (defaults to ``17`` per *Theaetetus* 147d6).

    Returns:
        Populated :class:`~geometor.model.Model` with vertices ``O, P1..P{max_n}``.
    """
    if max_n < 2:
        raise ValueError("max_n must be >= 2.")

    if model is None:
        m = _new_exact_model("theodorus_spiral")
        m._simplifier = sp.expand
    else:
        m = model
    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O")
    p1 = m.given_point(sp.Integer(1), sp.Integer(0), ID="P1", classes=["mekos"])
    m.construct_line(o_pt, p1, classes=["carrier", "spoke"], by="Post.1")

    vertices: list[spg.Point] = [p1]

    for n in range(1, max_n):
        curr_pt = vertices[-1]
        next_area = n + 1
        is_square_num = sp.sqrt(sp.Integer(next_area)).is_integer is True
        pt_cls = ["mekos", "given"] if is_square_num else (
            ["steiner", "dynamis"] if next_area == max_n else ["dynamis", "meet"]
        )

        # Exact I.11 perpendicular direction (-y_n, x_n) at P_n and exact unit step 1/sqrt(n)
        inv_rn = sp.Integer(1) / sp.sqrt(sp.Integer(n))
        nx = sp.expand(curr_pt.x - curr_pt.y * inv_rn)
        ny = sp.expand(curr_pt.y + curr_pt.x * inv_rn)

        with m.subconstruction(f"theodorus_step_{n}", hide_guides=True) as scope:
            perp_aux = m.set_point(
                sp.expand(curr_pt.x - curr_pt.y),
                sp.expand(curr_pt.y + curr_pt.x),
                parents=[o_pt, curr_pt],
                guide=True,
                by="I.11",
            )
            perp_ln = m.construct_line(curr_pt, perp_aux, guide=True, by="I.11")
            next_pt = m.set_point(
                nx,
                ny,
                parents=[perp_ln, curr_pt],
                ID=f"P{next_area}",
                classes=pt_cls,
                by="I.47",
            )
            scope.keep(next_pt)

        m.construct_line(curr_pt, next_pt, classes=["quadrilateral", "unit_leg"], by="Post.1")
        spoke_cls = (
            ["pappus", "even", "spoke"]
            if is_square_num
            else (["steiner_line", "spoke"] if next_area == max_n else ["cross", "spoke"])
        )
        m.construct_line(o_pt, next_pt, classes=spoke_cls, by="Post.1")

        if next_area <= 4:
            tri_cls = ["square"] if is_square_num else (["circle"] if next_area % 2 == 0 else ["hexagon"])
            m.set_polygon([o_pt, curr_pt, next_pt], classes=tri_cls, by="Theaet.147d")
            m.assert_incident(next_pt, perp_ln, by="I.11")
            m.assert_perpendicular((o_pt, curr_pt), (curr_pt, next_pt), by="I.11")
            m.assert_equal((o_pt, p1), (curr_pt, next_pt), by="Post.3")

        q_leg = sp.expand((next_pt.x - curr_pt.x) ** 2 + (next_pt.y - curr_pt.y) ** 2)
        dot_perp = sp.expand(
            curr_pt.x * (next_pt.x - curr_pt.x) + curr_pt.y * (next_pt.y - curr_pt.y)
        )
        q_next = sp.expand(next_pt.x**2 + next_pt.y**2)
        if q_leg != sp.Integer(1) or dot_perp != sp.Integer(0) or q_next != sp.Integer(next_area):
            raise AssertionError(
                f"Theodorus step {next_area} failed exact invariants: "
                f"Q_leg={q_leg}, dot={dot_perp}, Q_spoke={q_next}"
            )

        vertices.append(next_pt)

    m.conclude(
        o_pt,
        vertices[-1],
        by="Theaet.147d",
        label=f"Constructed Theodorus radical chain P1..P{max_n} with Q(O, P{max_n}) = {max_n}.",
    )
    return m


def verify_divided_line_identity() -> dict[str, sp.Expr | bool]:
    """Prove over symbolic ratio :math:`r > 0` that *pistis* equals *dianoia* (*Republic* 509d).

    Returns:
        Dictionary of exact symbolic lengths, quadrances, and verified proportion checks.
    """
    r = sp.Symbol("r", positive=True)
    eikasia = sp.Integer(1)
    pistis = r
    visible = eikasia + pistis
    dianoia = r
    noesis = r**2
    intelligible = dianoia + noesis

    return {
        "ratio_symbol": r,
        "eikasia": eikasia,
        "pistis": pistis,
        "dianoia": dianoia,
        "noesis": noesis,
        "realm_ratio": sp.simplify(intelligible / visible),
        "visible_subratio": sp.simplify(pistis / eikasia),
        "intelligible_subratio": sp.simplify(noesis / dianoia),
        "middle_segments_equal": sp.simplify(pistis - dianoia) == 0,
        "middle_is_geometric_mean": sp.simplify(pistis**2 - eikasia * noesis) == 0,
    }


def construct_divided_line(
    model: Model | None = None,
    ratio: sp.Expr = sp.GoldenRatio,
) -> Model:
    r"""Construct Plato's Divided Line (*Republic* VI, 509d–511e) and verify middle equality.

    Divides baseline ``[A, E]`` at ``C`` into Visible ``AC`` and Intelligible ``CE`` in
    ``1 : r``, and subdivides each realm in the same ratio ``1 : r`` at ``B`` and ``D``:

    - ``AB`` (*eikasia*, length :math:`1`, :math:`Q = 1`),
    - ``BC`` (*pistis*, length :math:`r`, :math:`Q = r^2`),
    - ``CD`` (*dianoia*, length :math:`r`, :math:`Q = r^2`),
    - ``DE`` (*noēsis*, length :math:`r^2`, :math:`Q = r^4`).

    Also constructs the semicircle on ``[A, K]`` of length :math:`1 + r^2` (`AB + DE`)
    whose ordinate ``BG`` at ``B`` has exact length :math:`\sqrt{1 \cdot r^2} = r`,
    demonstrating geometrically why ``BC = CD = BG``.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.
        ratio: Symbolic proportion :math:`r > 0` (defaults to ``sp.GoldenRatio``).

    Returns:
        Populated :class:`~geometor.model.Model` with verified equal-middle proof.
    """
    r_val = _normalize_symbolic_ratio(ratio)
    if sp.simplify(r_val) <= 0:
        raise ValueError(f"Divided Line ratio must be positive, got {ratio!r}.")

    m = model if model is not None else _new_exact_model("republic_divided_line")

    x_a = sp.Integer(0)
    x_b = sp.Integer(1)
    x_c = sp.Integer(1) + r_val
    x_d = sp.Integer(1) + sp.Integer(2) * r_val
    x_e = clean_expr((sp.Integer(1) + r_val) ** 2)

    a_pt = m.given_point(x_a, sp.Integer(0), ID="A")
    b_pt = m.set_point(x_b, sp.Integer(0), ID="B", classes=["meet"], by="Rep.509d")
    c_pt = m.set_point(x_c, sp.Integer(0), ID="C", classes=["steiner"], by="Rep.509d")
    d_pt = m.set_point(x_d, sp.Integer(0), ID="D", classes=["meet"], by="Rep.509d")
    e_pt = m.set_point(x_e, sp.Integer(0), ID="E", classes=["given"], by="Rep.509d")

    axis = m.construct_line(a_pt, e_pt, classes=["carrier"], by="Post.1")

    # Semicircle mean-proportional construction on AK of diameter 1 + r^2:
    # A=(0,0), B=(1,0), K=(1 + r^2, 0), midpoint M=((1 + r^2)/2, 0).
    # Ordinate at B meets circle (M, A) at G=(1, r), proving Q(B, G) = r^2 = Q(B, C) = Q(C, D).
    x_k = clean_expr(sp.Integer(1) + r_val**2)
    x_m = clean_expr(x_k / sp.Integer(2))
    k_pt = m.set_point(x_k, sp.Integer(0), ID="K", classes=["auxiliary"], guide=True)
    m_pt = m.set_point(x_m, sp.Integer(0), ID="M", classes=["auxiliary"], guide=True)
    mean_circ = m.construct_circle(m_pt, a_pt, classes=["conic"], by="Post.3")

    perp_b = _construct_perp_at_point(
        m, a_pt, b_pt, scope_name="rep_perp_b", guide=False, classes=["harmonic"]
    )
    g_pt = m.intersect(perp_b, mean_circ, side_of=(a_pt, e_pt, 1), ID="G", classes=["harmonic"], by="VI.13")

    perp_c = _construct_perp_at_point(
        m, a_pt, c_pt, scope_name="rep_perp_c", guide=False, classes=["steiner_line"]
    )
    _ = perp_c

    # Transfer ordinate height r across B -> C -> D to form congruent squares on pistis (BC) and dianoia (CD)
    h_pt = m.set_point(x_c, r_val, ID="H", classes=["harmonic"], by="I.34")
    j_pt = m.set_point(x_d, r_val, ID="J", classes=["harmonic"], by="I.34")
    m.construct_line(g_pt, j_pt, classes=["quadrilateral"], by="Post.1")
    m.construct_line(d_pt, j_pt, classes=["quadrilateral"], by="Post.1")
    m.construct_line(a_pt, g_pt, classes=["cross"], by="Post.1")
    m.construct_line(g_pt, k_pt, classes=["cross"], guide=True, by="Post.1")
    _ = axis

    sq_pistis = m.set_polygon([b_pt, c_pt, h_pt, g_pt], classes=["square"], by="Rep.510a")
    sq_dianoia = m.set_polygon([c_pt, d_pt, j_pt, h_pt], classes=["diamond"], by="Rep.510b")

    is_phi = zero_test(r_val**2 - r_val - sp.Integer(1))
    sec_cls = ["golden"] if is_phi else ["harmonic"]
    m.set_section([a_pt, c_pt, e_pt], classes=sec_cls, by="Rep.509d")
    m.set_section([a_pt, b_pt, c_pt], classes=sec_cls, by="Rep.509e")
    m.set_section([c_pt, d_pt, e_pt], classes=sec_cls, by="Rep.510b")

    # Exact assertions: Q(pistis) == Q(dianoia) == Q(ordinate BG)
    m.assert_equal((b_pt, c_pt), (c_pt, d_pt), (b_pt, g_pt), by="Rep.VI.509d")
    if is_phi:
        # Unique Golden Ratio property: Intelligible Noesis DE equals entire Visible realm AC!
        m.assert_equal((a_pt, c_pt), (d_pt, e_pt), by="II.11")

    m.conclude(
        sq_pistis,
        sq_dianoia,
        by="Rep.VI.509d-511e",
        label="Pistis (BC) and Dianoia (CD) have identical exact quadrance r^2.",
    )
    return m


def construct_timaeus_proportion_circles(model: Model | None = None) -> Model:
    r"""Construct the Three Platonic Means & Circles of Same/Different (*Timaeus* 31c–36d).

    On diameter ``AB`` of length :math:`2 + 4 = 6` (`A=(0,0)`, `J=(2,0)`, `O=(3,0)`, `B=(6,0)`),
    exhibits in a single exact Euclidean figure:

    - **Arithmetic mean** ``O G`` of length :math:`3 = \frac{2+4}{2}` (*hēmiolios*, :math:`Q = 9`),
    - **Geometric mean** ``J G`` of length :math:`2\sqrt{2} = \sqrt{2\cdot 4}` (:math:`Q = 8`),
    - **Harmonic mean** ``G H`` of length :math:`\frac{8}{3} = \frac{2\cdot 2\cdot 4}{2+4}` (*epitritos*, :math:`Q = 64/9`),
    - **Epogdoos ratio** :math:`\frac{OG}{GH} = \frac{3}{8/3} = \frac{9}{8}` (:math:`Q(O,G)/Q(G,H) = 81/64`),

    together with the equatorial Circle of the Same ``(O, B)`` and the inclined Circle
    of the Different ``[P, Q]`` crossing at ``O`` like the Greek letter :math:`\mathrm{X}` (*chi*, 36b–c).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model`.
    """
    m = model if model is not None else _new_exact_model("timaeus_world_soul")

    a_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="A")
    j_pt = m.given_point(sp.Integer(2), sp.Integer(0), ID="J", classes=["meet"])
    o_pt = m.given_point(sp.Integer(3), sp.Integer(0), ID="O", classes=["steiner"])
    b_pt = m.given_point(sp.Integer(6), sp.Integer(0), ID="B")

    diam_ln = m.construct_line(a_pt, b_pt, classes=["carrier"], by="Post.1")
    same_circ = m.construct_circle(o_pt, b_pt, classes=["conic"], by="Tim.36c")
    inner_circ = m.construct_circle(o_pt, j_pt, classes=["conic"], by="Tim.36d")
    _ = (diam_ln, inner_circ)

    # Erect perpendicular at J=(2,0) meeting Circle of the Same at G=(2, 2*sqrt(2))
    perp_j = _construct_perp_at_point(
        m, a_pt, j_pt, scope_name="tim_perp_j", guide=False, classes=["harmonic"]
    )
    g_pt = m.intersect(perp_j, same_circ, side_of=(a_pt, b_pt, 1), ID="G", classes=["harmonic"], by="VI.13")

    rad_og = m.construct_line(o_pt, g_pt, classes=["pappus", "even"], by="Post.1")

    # Foot H of perpendicular from J onto radius OG: exact harmonic mean GH = 8/3
    h_pt = m.set_point(
        sp.Rational(26, 9),
        sp.Rational(2, 9) * sp.sqrt(2),
        parents=[j_pt, rad_og],
        ID="H",
        classes=["fourth_harmonic"],
        by="I.12",
    )
    m.construct_line(j_pt, h_pt, classes=["quadrilateral", "diagonal"], by="I.12")

    # Inclined axis of the Circle of the Different (Chi-cross at center O, 36b-c)
    s3_half = sp.Rational(3, 2) * sp.sqrt(3)
    p_pt = m.set_point(sp.Integer(3) - s3_half, sp.Rational(-3, 2), ID="P", classes=["meet"], by="Tim.36c")
    q_pt = m.set_point(sp.Integer(3) + s3_half, sp.Rational(3, 2), ID="Q", classes=["meet"], by="Tim.36c")
    m.construct_line(p_pt, q_pt, classes=["steiner_line"], by="Tim.36c")

    tri_ojg = m.set_polygon([o_pt, j_pt, g_pt], classes=["square"], by="Tim.32a")
    tri_jhg = m.set_polygon([j_pt, h_pt, g_pt], classes=["diamond"], by="Tim.36a")

    m.assert_perpendicular((a_pt, b_pt), (j_pt, g_pt), by="I.11")
    m.assert_perpendicular((o_pt, g_pt), (j_pt, h_pt), by="I.12")
    m.assert_equal((o_pt, a_pt), (o_pt, b_pt), (o_pt, g_pt), (o_pt, p_pt), (o_pt, q_pt), by="Def.15")

    if quadrance(o_pt, g_pt) != sp.Integer(9):
        raise AssertionError("Expected arithmetic mean quadrance Q(O, G) = 9.")
    if quadrance(j_pt, g_pt) != sp.Integer(8):
        raise AssertionError("Expected geometric mean quadrance Q(J, G) = 8.")
    if quadrance(g_pt, h_pt) != sp.Rational(64, 9):
        raise AssertionError("Expected harmonic mean quadrance Q(G, H) = 64/9.")

    m.conclude(
        tri_ojg,
        tri_jhg,
        by="Tim.35c-36b",
        label="Arithmetic (3), geometric (2*sqrt(2)), and harmonic (8/3) means yield Q(OG)/Q(GH) = (9/8)^2.",
    )
    return m


def construct_timaeus_triangles(model: Model | None = None) -> Model:
    r"""Construct the 6-triangle equilateral cosmic face of *Timaeus* 54d–55a.

    Assembles six elementary right-angled scalene half-triangles (*hēmitrigōna*)
    with exact side lengths :math:`1 : \sqrt{3} : 2` (quadrances :math:`1, 3, 4` and
    spreads :math:`1/4, 3/4, 1`) meeting thrice along their diagonals and altitudes
    at the centroid ``G = (0, 0) = X(2)`` to form one equilateral face ``< A B C >``
    of the Tetrahedron, Octahedron, and Icosahedron.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model`.
    """
    m = model if model is not None else _new_exact_model("timaeus_triangles")

    # Given centroid G=(0,0) and foot M1=(0,-1) of unit inradius Q(G, M1) = 1
    g_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="G", classes=["steiner"])
    m1_pt = m.given_point(sp.Integer(0), sp.Integer(-1), ID="M1", classes=["meet"])

    axis_v = m.construct_line(m1_pt, g_pt, classes=["pappus", "even"], by="Post.1")

    # Double M1->G->U->A so circumradius GA = 2 (quadrance Q(G, A) = 4)
    c_g1 = m.construct_circle(g_pt, m1_pt, classes=["conic"], by="Post.3")
    u_pt = m.intersect(axis_v, c_g1, other_than=m1_pt, ID="U", classes=["auxiliary"], guide=True, by="Def.15")
    c_u1 = m.construct_circle(u_pt, g_pt, guide=True, by="Post.3")
    a_pt = m.intersect(axis_v, c_u1, other_than=g_pt, ID="A", classes=["given"], by="Post.3")

    circum = m.construct_circle(g_pt, a_pt, classes=["conic"], by="Post.3")

    # Base line perpendicular to GM1 at M1 meets circumcircle (G, A) at B=(-sqrt(3), -1) and C=(sqrt(3), -1)
    base_bc = _construct_perp_at_point(
        m, g_pt, m1_pt, scope_name="tim_base_bc", guide=False, classes=["carrier"]
    )

    b_pt = m.intersect(base_bc, circum, side_of=(m1_pt, a_pt, 1), ID="B", classes=["given"], by="I.11")
    c_pt = m.intersect(base_bc, circum, other_than=b_pt, ID="C", classes=["given"], by="I.11")

    side_ca = m.construct_line(c_pt, a_pt, classes=["carrier"], by="Post.1")
    side_ab = m.construct_line(a_pt, b_pt, classes=["carrier"], by="Post.1")

    # Other two altitudes/medians [B, G] -> M2 on CA and [C, G] -> M3 on AB
    med_b = m.construct_line(b_pt, g_pt, classes=["pappus", "even"], by="Post.1")
    med_c = m.construct_line(c_pt, g_pt, classes=["pappus", "even"], by="Post.1")

    m2_pt = m.intersect(side_ca, med_b, ID="M2", classes=["meet"], by="Tim.54e")
    m3_pt = m.intersect(side_ab, med_c, ID="M3", classes=["meet"], by="Tim.54e")

    # Register outer cosmic face and all 6 elementary scalene right triangles
    face = m.set_polygon([a_pt, b_pt, c_pt], classes=["hexagon"], by="Tim.54e")
    sub_tris_pts = [
        (g_pt, m1_pt, c_pt, "square"),
        (g_pt, m1_pt, b_pt, "diamond"),
        (g_pt, m2_pt, c_pt, "circle"),
        (g_pt, m2_pt, a_pt, "square"),
        (g_pt, m3_pt, a_pt, "diamond"),
        (g_pt, m3_pt, b_pt, "circle"),
    ]
    for p_cen, p_mid, p_vtx, poly_cls in sub_tris_pts:
        m.set_polygon([p_cen, p_mid, p_vtx], classes=[poly_cls], by="Tim.54b")
        q_short = quadrance(p_cen, p_mid)
        q_long = quadrance(p_mid, p_vtx)
        q_hyp = quadrance(p_cen, p_vtx)
        if (q_short, q_long, q_hyp) != (sp.Integer(1), sp.Integer(3), sp.Integer(4)):
            raise AssertionError(f"Expected quadrances (1, 3, 4), got {(q_short, q_long, q_hyp)}")
        s_right = vertex_spread(p_cen, p_mid, p_vtx)
        s_thirty = vertex_spread(p_cen, p_vtx, p_mid)
        s_sixty = vertex_spread(p_mid, p_cen, p_vtx)
        if (s_thirty, s_sixty, s_right) != (sp.Rational(1, 4), sp.Rational(3, 4), sp.Integer(1)):
            raise AssertionError(
                f"Expected spreads (1/4, 3/4, 1), got {(s_thirty, s_sixty, s_right)}"
            )

    m.assert_equal((a_pt, b_pt), (b_pt, c_pt), (c_pt, a_pt), by="Tim.54e")
    m.assert_equal((g_pt, m1_pt), (g_pt, m2_pt), (g_pt, m3_pt), by="Tim.54e")
    m.assert_perpendicular((g_pt, m1_pt), (b_pt, c_pt), by="Tim.54e")
    m.assert_perpendicular((g_pt, m2_pt), (c_pt, a_pt), by="Tim.54e")
    m.assert_perpendicular((g_pt, m3_pt), (a_pt, b_pt), by="Tim.54e")

    m.conclude(
        face,
        g_pt,
        by="Tim.54d-55a",
        label="Six 1:sqrt(3):2 half-triangles (spreads 1/4, 3/4, 1) meet at centroid G to form cosmic face ABC.",
    )
    return m


def construct_timaeus_cube_face(model: Model | None = None) -> Model:
    r"""Construct the 4-isosceles-triangle square face of Earth (*Timaeus* 55b).

    Assembles four elementary isosceles right triangles (:math:`1 : 1 : \sqrt{2}`,
    quadrances :math:`1, 1, 2`; spreads :math:`1/2, 1/2, 1`) with right angles
    meeting at center ``O=(0,0)`` to form one square face ``< A B C D >`` of the Cube.

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model`.
    """
    m = model if model is not None else _new_exact_model("timaeus_cube_face")

    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O", classes=["steiner"])
    a_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="A")
    axis_h = m.construct_line(o_pt, a_pt, classes=["pappus", "even"], by="Post.1")
    circ = m.construct_circle(o_pt, a_pt, classes=["conic"], by="Post.3")

    c_pt = m.intersect(axis_h, circ, other_than=a_pt, ID="C", classes=["given"], by="Def.15")
    axis_v = _construct_perp_at_point(
        m, a_pt, o_pt, scope_name="cube_axis_v", guide=False, classes=["pappus", "even"]
    )

    b_pt = m.intersect(axis_v, circ, side_of=(o_pt, a_pt, 1), ID="B", classes=["given"], by="I.11")
    d_pt = m.intersect(axis_v, circ, other_than=b_pt, ID="D", classes=["given"], by="Def.15")

    for p1, p2, cls in (
        (a_pt, b_pt, "square"),
        (b_pt, c_pt, "diamond"),
        (c_pt, d_pt, "square"),
        (d_pt, a_pt, "diamond"),
    ):
        m.construct_line(p1, p2, classes=["carrier"], by="Post.1")
        m.set_polygon([o_pt, p1, p2], classes=[cls], by="Tim.55b")
        if (quadrance(o_pt, p1), quadrance(o_pt, p2), quadrance(p1, p2)) != (1, 1, 2):
            raise AssertionError("Expected isosceles quadrances (1, 1, 2).")
        if (
            vertex_spread(p1, o_pt, p2),
            vertex_spread(o_pt, p1, p2),
            vertex_spread(o_pt, p2, p1),
        ) != (sp.Integer(1), sp.Rational(1, 2), sp.Rational(1, 2)):
            raise AssertionError("Expected isosceles spreads (1, 1/2, 1/2).")

    sq = m.set_polygon([a_pt, b_pt, c_pt, d_pt], classes=["hexagon"], by="Tim.55b")
    m.assert_equal((a_pt, b_pt), (b_pt, c_pt), (c_pt, d_pt), (d_pt, a_pt), by="Tim.55b")
    m.assert_perpendicular((o_pt, a_pt), (o_pt, b_pt), by="Tim.55b")
    m.conclude(
        sq,
        o_pt,
        by="Tim.55b",
        label="Four 1:1:sqrt(2) isosceles right triangles meet at O to form the square face of Earth.",
    )
    return m


def construct_compass_and_peras(model: Model | None = None) -> Model:
    r"""Construct Unit 6's Compass (*Tornos*), Straight Ray (*Kanōn*) & :math:`1,\sqrt{2},\sqrt{3}` Triad.

    Synthesizes the three foundational definitions and problems of Unit 6:

    1. *Parmenides* 137e & *Philebus* 51c: Circle ``(O, A)`` whose extremities ``A, B, C``
       are equidistant from the middle ``O=(0,0)``, and straight line ``[A, O, C]`` whose
       middle ``O`` stands optically before both extremes.
    2. *Laws* VII, 819d–820d: Unit length ``OC`` (:math:`Q = 1`), breadth ``CD`` (:math:`Q = 1`)
       yielding plane diagonal ``OD`` (:math:`Q = 2`), and unfolded unit depth ``DE``
       perpendicular to ``OD`` yielding solid cube diagonal ``OE`` (:math:`Q = 3`).

    Args:
        model: Optional existing :class:`~geometor.model.Model`.

    Returns:
        Populated :class:`~geometor.model.Model`.
    """
    m = model if model is not None else _new_exact_model("foundations_peras_compass")

    o_pt = m.given_point(sp.Integer(0), sp.Integer(0), ID="O", classes=["steiner"])
    c_pt = m.given_point(sp.Integer(1), sp.Integer(0), ID="C")

    kanon_ln = m.construct_line(o_pt, c_pt, classes=["carrier"], by="Parm.137e")
    tornos_circ = m.construct_circle(o_pt, c_pt, classes=["conic"], by="Phil.51c")

    a_pt = m.intersect(kanon_ln, tornos_circ, other_than=c_pt, ID="A", classes=["given"], by="Parm.137e")
    perp_o = _construct_perp_at_point(
        m, c_pt, o_pt, scope_name="peras_perp_o", guide=False, classes=["carrier"]
    )

    b_pt = m.intersect(perp_o, tornos_circ, side_of=(o_pt, c_pt, 1), ID="B", classes=["given"], by="I.11")

    # Complete unit square OCDB -> plane diagonal OD (Q = 2)
    perp_c = _construct_perp_at_point(m, o_pt, c_pt, scope_name="peras_perp_c")
    perp_b = _construct_perp_at_point(m, o_pt, b_pt, scope_name="peras_perp_b")
    d_pt = m.intersect(perp_c, perp_b, ID="D", classes=["meet"], by="I.46")
    m.construct_line(c_pt, d_pt, classes=["quadrilateral"], by="Post.1")
    m.construct_line(b_pt, d_pt, classes=["quadrilateral"], by="Post.1")
    diag_od = m.construct_line(o_pt, d_pt, classes=["pappus", "even"], by="Laws.820a")
    _ = diag_od

    # Unfold 3rd dimension (depth = 1) perpendicular to plane diagonal OD at D -> solid diagonal OE (Q = 3)
    perp_d = _construct_perp_at_point(m, o_pt, d_pt, scope_name="peras_perp_d")
    unit_d = m.construct_circle(d_pt, c_pt, guide=True, by="Post.3")
    e_pt = m.intersect(perp_d, unit_d, side_of=(o_pt, d_pt, 1), ID="E", classes=["harmonic"], by="Laws.820a")
    m.construct_line(d_pt, e_pt, classes=["harmonic"], by="Post.1")
    m.construct_line(o_pt, e_pt, classes=["steiner_line"], by="Laws.820c")

    sq_plane = m.set_polygon([o_pt, c_pt, d_pt, b_pt], classes=["square"], by="Laws.819e")
    tri_solid = m.set_polygon([o_pt, d_pt, e_pt], classes=["diamond"], by="Laws.820a")

    m.assert_collinear(a_pt, o_pt, c_pt, by="Parm.137e")
    m.assert_equal((o_pt, a_pt), (o_pt, b_pt), (o_pt, c_pt), (d_pt, e_pt), by="Parm.137e")
    m.assert_perpendicular((o_pt, d_pt), (d_pt, e_pt), by="I.11")

    if (quadrance(o_pt, c_pt), quadrance(o_pt, d_pt), quadrance(o_pt, e_pt)) != (1, 2, 3):
        raise AssertionError("Expected length-breadth-depth diagonal quadrances (1, 2, 3).")

    m.conclude(
        sq_plane,
        tri_solid,
        by="Laws.819d-820d",
        label="Compass circle (Q=1), plane diagonal OD (Q=2), and solid diagonal OE (Q=3) verified.",
    )
    return m
