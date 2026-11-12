"""Interactive `.euclid-graphic` SVG renderer for Plato's geometric constructions.

Produces dark/light theme-adaptive SVGs from exact :class:`~geometor.model.Model`
instances conforming simultaneously to:

1. Standalone SVG display (GitHub ``README.rst``, browsers, ``prefers-color-scheme``), and
2. ``photon-platform/publish`` interactive ``geometor_interactive.js`` figures
   (``svg.euclid-graphic``, ``<defs>`` tick markers, ``#elements``, ``#graphics``,
   ``#highlights``, ``#points``, ``#labels``, 3-vertex midpoint ``<path>`` geometry,
   ``data-ref``, and ``data-aliases``).
"""

from __future__ import annotations

import html
import math
import re
from collections.abc import Sequence
from pathlib import Path

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model
from geometor.model.algebra import fast_line_coeffs
from geometor.model.sections import Section

from geometor.plato.constructions import (
    construct_compass_and_peras,
    construct_divided_line,
    construct_meno_diagonal_doubling,
    construct_theodorus_spiral,
    construct_timaeus_proportion_circles,
    construct_timaeus_triangles,
)

__all__ = [
    "EMBEDDED_SVG_STYLE",
    "render_svg_string",
    "export_svg",
    "export_all_codex_figures",
]

EMBEDDED_SVG_STYLE: str = """
  .euclid-graphic {
    --svg-bg: #fafaf9;
    --ink: #1c1917;
    --label-halo: rgba(250, 250, 249, 0.92);
    --carrier: #334155;
    --conic: #0284c7;
    --cross: #0e7490;
    --quad: #4338ca;
    --pappus-even: #d97706;
    --pappus-odd: #db2777;
    --steiner: #7c3aed;
    --harmonic: #059669;
    --golden: #b45309;
    --pt-given: #0f172a;
    --pt-meet: #d97706;
    --pt-steiner: #7c3aed;
    --pt-harmonic: #059669;
    --tri-square: #d97706;
    --tri-circle: #0284c7;
    --tri-diamond: #db2777;
    font-family: "Inter", "Segoe UI", system-ui, -apple-system, sans-serif;
  }
  @media (prefers-color-scheme: dark) {
    .euclid-graphic {
      --svg-bg: #141417;
      --ink: #f4f4f5;
      --label-halo: rgba(20, 20, 23, 0.92);
      --carrier: #cbd5e1;
      --conic: #38bdf8;
      --cross: #38bdf8;
      --quad: #818cf8;
      --pappus-even: #fbbf24;
      --pappus-odd: #f472b6;
      --steiner: #c084fc;
      --harmonic: #34d399;
      --golden: #facc15;
      --pt-given: #f8fafc;
      --pt-meet: #fbbf24;
      --pt-steiner: #c084fc;
      --pt-harmonic: #34d399;
      --tri-square: #fbbf24;
      --tri-circle: #38bdf8;
      --tri-diamond: #f472b6;
    }
  }
  .euclid-graphic .bg { fill: #fafaf9; fill: var(--svg-bg, #fafaf9); }
  .euclid-graphic .geom-circle.conic-curve { fill: none; stroke: #0284c7; stroke: var(--conic, #0284c7); stroke-width: 1.95; opacity: 0.86; }
  .euclid-graphic .geom-line { fill: none; stroke: #334155; stroke: var(--carrier, #334155); stroke-width: 1.75; stroke-linecap: round; }
  .euclid-graphic .carrier-line { stroke: #334155; stroke: var(--carrier, #334155); stroke-width: 2.15; opacity: 0.94; }
  .euclid-graphic .cross-line { stroke: #0e7490; stroke: var(--cross, #0e7490); stroke-width: 1.35; stroke-opacity: 0.68; }
  .euclid-graphic .quad-line { stroke: #4338ca; stroke: var(--quad, #4338ca); stroke-width: 1.65; stroke-opacity: 0.84; }
  .euclid-graphic .diagonal-line { stroke-dasharray: 5 3.5; }
  .euclid-graphic .pappus-line { stroke-width: 2.65; opacity: 0.96; }
  .euclid-graphic .pappus-even { stroke: #d97706; stroke: var(--pappus-even, #d97706); }
  .euclid-graphic .pappus-odd { stroke: #db2777; stroke: var(--pappus-odd, #db2777); }
  .euclid-graphic .steiner-line { stroke: #7c3aed; stroke: var(--steiner, #7c3aed); stroke-width: 2.45; stroke-dasharray: 6 3.5; }
  .euclid-graphic .harmonic-line { stroke: #059669; stroke: var(--harmonic, #059669); stroke-width: 2.35; }
  .euclid-graphic .geom-segment.golden-segment { fill: none; stroke: #b45309; stroke: var(--golden, #b45309); stroke-width: 3.6; stroke-linecap: round; opacity: 0.85; }
  .euclid-graphic .geom-segment.harmonic-segment { fill: none; stroke: #059669; stroke: var(--harmonic, #059669); stroke-width: 3.2; stroke-linecap: round; opacity: 0.78; }
  .euclid-graphic .geom-polygon.hexagon-poly { fill: #0e7490; fill: var(--cross, #0e7490); fill-opacity: 0.05; stroke: #0e7490; stroke: var(--cross, #0e7490); stroke-width: 1.4; stroke-opacity: 0.42; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-square { fill: #d97706; fill: var(--tri-square, #d97706); fill-opacity: 0.11; stroke: #d97706; stroke: var(--tri-square, #d97706); stroke-width: 1.7; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-circle { fill: #0284c7; fill: var(--tri-circle, #0284c7); fill-opacity: 0.09; stroke: #0284c7; stroke: var(--tri-circle, #0284c7); stroke-width: 1.6; stroke-linejoin: round; }
  .euclid-graphic .geom-polygon.tri-diamond { fill: #db2777; fill: var(--tri-diamond, #db2777); fill-opacity: 0.12; stroke: #db2777; stroke: var(--tri-diamond, #db2777); stroke-width: 1.9; stroke-linejoin: round; }
  .euclid-graphic .geom-point { fill: #0f172a; fill: var(--pt-given, #0f172a); stroke: #fafaf9; stroke: var(--svg-bg, #fafaf9); stroke-width: 1.5; }
  .euclid-graphic .meet-point { fill: #d97706; fill: var(--pt-meet, #d97706); }
  .euclid-graphic .steiner-point { fill: #7c3aed; fill: var(--pt-steiner, #7c3aed); stroke-width: 1.9; }
  .euclid-graphic .harmonic-point { fill: #059669; fill: var(--pt-harmonic, #059669); stroke-width: 1.8; }
  .euclid-graphic .aux-point { opacity: 0.78; }
  .euclid-graphic .geom-label {
    fill: #1c1917;
    fill: var(--ink, #1c1917);
    font-size: 13px;
    font-weight: 600;
    paint-order: stroke fill;
    stroke: #fafaf9;
    stroke: var(--label-halo, rgba(250, 250, 249, 0.92));
    stroke-width: 3.6px;
    stroke-linejoin: round;
    user-select: none;
  }
  .euclid-graphic .geom-label-sub { font-size: 9.8px; font-weight: 600; }
""".strip()

SVG_TICK_DEFS: str = """  <defs>
    <marker id="geom-tick-1" viewBox="-4 -6 8 12" refX="0" refY="0" markerWidth="8" markerHeight="12" orient="auto">
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-2" viewBox="-6 -6 12 12" refX="0" refY="0" markerWidth="12" markerHeight="12" orient="auto">
      <line x1="-2" y1="-4.5" x2="-2" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
      <line x1="2" y1="-4.5" x2="2" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
    </marker>
    <marker id="geom-tick-3" viewBox="-8 -6 16 12" refX="0" refY="0" markerWidth="16" markerHeight="12" orient="auto">
      <line x1="-3.5" y1="-4.5" x2="-3.5" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
      <line x1="0" y1="-4.5" x2="0" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
      <line x1="3.5" y1="-4.5" x2="3.5" y2="4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" />
    </marker>
  </defs>"""


def _fmt(val: float) -> str:
    """Format a pixel coordinate compactly to 2 decimal places."""
    if abs(val - round(val)) < 1e-5:
        return str(int(round(val)))
    return f"{val:.2f}".rstrip("0").rstrip(".")


def _clip_line_to_rect(
    line: spg.Line,
    xmin: float,
    xmax: float,
    ymin: float,
    ymax: float,
) -> tuple[tuple[float, float], tuple[float, float]] | None:
    """Clip an infinite algebraic line to a math bounding box."""
    a_sym, b_sym, c_sym = fast_line_coeffs(line)
    a_f = float(a_sym.evalf())
    b_f = float(b_sym.evalf())
    c_f = float(c_sym.evalf())
    eps = 1e-11
    hits: list[tuple[float, float]] = []

    if abs(b_f) > eps:
        for x_edge in (xmin, xmax):
            y_val = -(a_f * x_edge + c_f) / b_f
            if ymin - 1e-7 <= y_val <= ymax + 1e-7:
                hits.append((x_edge, min(max(y_val, ymin), ymax)))

    if abs(a_f) > eps:
        for y_edge in (ymin, ymax):
            x_val = -(b_f * y_edge + c_f) / a_f
            if xmin - 1e-7 <= x_val <= xmax + 1e-7:
                hits.append((min(max(x_val, xmin), xmax), y_edge))

    unique_hits: list[tuple[float, float]] = []
    for hx, hy in hits:
        if not any(math.hypot(hx - ux, hy - uy) < 1e-5 for ux, uy in unique_hits):
            unique_hits.append((hx, hy))

    if len(unique_hits) < 2:
        return None
    best_pair = (unique_hits[0], unique_hits[1])
    best_dist = -1.0
    for i in range(len(unique_hits)):
        for j in range(i + 1, len(unique_hits)):
            d = math.hypot(
                unique_hits[j][0] - unique_hits[i][0],
                unique_hits[j][1] - unique_hits[i][1],
            )
            if d > best_dist:
                best_dist = d
                best_pair = (unique_hits[i], unique_hits[j])
    return best_pair


def _split_point_label(
    pt_id: str,
    overrides: dict[str, tuple[str, str]] | None = None,
) -> tuple[str, str]:
    """Split an alphanumeric point ID into ``(base, subscript)`` for ``<tspan>`` display."""
    if overrides and pt_id in overrides:
        return overrides[pt_id]
    m = re.match(r"^([A-Za-z]+)(\d+)$", pt_id)
    if m:
        return (m.group(1), m.group(2))
    return (pt_id, "")


def _line_css_classes(classes: dict[str, str] | set[str]) -> str:
    """Map model line classes to semantic CSS classes."""
    out = ["geom-line"]
    if "carrier" in classes:
        out.append("carrier-line")
    if "cross" in classes:
        out.append("cross-line")
    if "quadrilateral" in classes:
        out.append("quad-line")
    if "diagonal" in classes:
        out.append("diagonal-line")
    if "pappus" in classes:
        out.append("pappus-line")
        if "odd" in classes:
            out.append("pappus-odd")
        else:
            out.append("pappus-even")
    if "steiner_line" in classes:
        out.append("steiner-line")
    if "harmonic" in classes:
        out.append("harmonic-line")
    return " ".join(out)


def _polygon_css_classes(classes: dict[str, str] | set[str]) -> str:
    """Map model polygon classes to semantic CSS classes."""
    out = ["geom-polygon"]
    if "hexagon" in classes:
        out.append("hexagon-poly")
    if "square" in classes:
        out.append("tri-square")
    if "circle" in classes:
        out.append("tri-circle")
    if "diamond" in classes:
        out.append("tri-diamond")
    return " ".join(out)


def _point_css_and_radius(classes: dict[str, str] | set[str]) -> tuple[str, float]:
    """Map model point classes to ``(css_class_string, pixel_radius)``."""
    out = ["geom-point"]
    radius = 3.8
    if "given" in classes or "mekos" in classes:
        out.append("given-point")
        radius = 4.3
    if "meet" in classes or "dynamis" in classes or "diagonal_vertex" in classes:
        out.append("meet-point")
        radius = 4.2
    if "steiner" in classes:
        out.append("steiner-point")
        radius = 5.4
    if "fourth_harmonic" in classes or "harmonic" in classes:
        out.append("harmonic-point")
        radius = 4.8
    if "auxiliary" in classes or "trial" in classes:
        out.append("aux-point")
        radius = 3.2
    return (" ".join(out), radius)


def _point_to_segment_dist(
    px: float,
    py: float,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
) -> float:
    """Compute pixel distance from ``(px, py)`` to segment ``(x1, y1)-(x2, y2)``."""
    dx = x2 - x1
    dy = y2 - y1
    len_sq = dx * dx + dy * dy
    if len_sq < 1e-9:
        return math.hypot(px - x1, py - y1)
    t = max(0.0, min(1.0, ((px - x1) * dx + (py - y1) * dy) / len_sq))
    proj_x = x1 + t * dx
    proj_y = y1 + t * dy
    return math.hypot(px - proj_x, py - proj_y)


def render_svg_string(
    model: Model,
    *,
    graphic_id: str = "g1",
    title: str = "Plato Geometric Construction",
    width: int = 680,
    height: int = 460,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    finite_segments: bool = True,
    include_guides: bool = False,
    show_labels: bool = True,
    show_aux_labels: bool = False,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> str:
    """Render an exact :class:`~geometor.model.Model` into an interactive ``.euclid-graphic`` SVG string.

    Args:
        model: Populated :class:`~geometor.model.Model`.
        graphic_id: ``data-graphic-id`` attribute for ``geometor_interactive.js``.
        title: Accessible SVG title.
        width: SVG ``viewBox`` width in pixels.
        height: SVG ``viewBox`` height in pixels.
        margin: Outer pixel margin around the framed scene.
        bbox: Optional explicit math viewport ``(xmin, xmax, ymin, ymax)``.
        focus_points: Optional subset of points for auto-framing.
        finite_segments: When ``True`` (default), draw each line strictly spanning all
            incident visible points (preventing infinite ray clutter on spiral/grid plates).
        include_guides: If ``True``, include elements marked ``guide=True``.
        show_labels: Master toggle for point labels.
        show_aux_labels: If ``True``, label ``X1..Xn`` auto-intersections.
        label_overrides: Optional mapping ``pt_id -> (base, subscript)``.
        highlight_point_ids: Optional point IDs to emphasize with a halo ring.

    Returns:
        Complete UTF-8 SVG document string.
    """
    visible_points = [
        pt for pt in model.points if include_guides or not model[pt].guide
    ]
    visible_lines = [
        ln for ln in model.lines if include_guides or not model[ln].guide
    ]
    visible_polygons = [
        poly
        for poly in model
        if isinstance(poly, spg.Polygon) and (include_guides or not model[poly].guide)
    ]
    visible_sections = [
        sec
        for sec in model
        if isinstance(sec, Section) and (include_guides or not model[sec].guide)
    ]
    visible_conics: list[tuple[spg.Circle, str]] = [
        (curve, model[curve].ID)
        for curve in model
        if isinstance(curve, spg.Circle) and (include_guides or not model[curve].guide)
    ]

    frame_pts = list(focus_points) if focus_points else visible_points
    if bbox is not None:
        xmin_m, xmax_m, ymin_m, ymax_m = bbox
    elif frame_pts or visible_conics:
        xs = [float(p.x.evalf()) for p in frame_pts]
        ys = [float(p.y.evalf()) for p in frame_pts]
        if focus_points is None:
            for curve, _ in visible_conics:
                ccx = float(curve.center.x.evalf())
                ccy = float(curve.center.y.evalf())
                rad = float(curve.radius.evalf())
                xs.extend((ccx - rad, ccx + rad))
                ys.extend((ccy - rad, ccy + rad))
        xmin_m, xmax_m = min(xs), max(xs)
        ymin_m, ymax_m = min(ys), max(ys)
        span_x = max(xmax_m - xmin_m, 1.0)
        span_y = max(ymax_m - ymin_m, 1.0)
        pad_x = 0.12 * span_x
        pad_y = 0.14 * span_y
        xmin_m -= pad_x
        xmax_m += pad_x
        ymin_m -= pad_y
        ymax_m += pad_y
    else:
        xmin_m, xmax_m, ymin_m, ymax_m = -1.0, 5.0, -1.0, 4.0

    span_x = max(xmax_m - xmin_m, 1e-6)
    span_y = max(ymax_m - ymin_m, 1e-6)
    avail_w = max(width - 2.0 * margin, 100.0)
    avail_h = max(height - 2.0 * margin, 100.0)
    scale = min(avail_w / span_x, avail_h / span_y)

    cx_m = 0.5 * (xmin_m + xmax_m)
    cy_m = 0.5 * (ymin_m + ymax_m)
    cx_s = 0.5 * width
    cy_s = 0.5 * height

    def to_svg(mx: float, my: float) -> tuple[float, float]:
        return (cx_s + (mx - cx_m) * scale, cy_s - (my - cy_m) * scale)

    inset_px = 14.0
    clip_xmin = cx_m - (cx_s - inset_px) / scale
    clip_xmax = cx_m + (width - inset_px - cx_s) / scale
    clip_ymin = cy_m - (height - inset_px - cy_s) / scale
    clip_ymax = cy_m + (cy_s - inset_px) / scale

    pt_svg_coords: dict[spg.Point, tuple[float, float]] = {
        pt: to_svg(float(pt.x.evalf()), float(pt.y.evalf())) for pt in visible_points
    }

    conic_elems: list[str] = []
    for curve, primary_c_ref in visible_conics:
        ccx_f = float(curve.center.x.evalf())
        ccy_f = float(curve.center.y.evalf())
        rad_f = float(curve.radius.evalf())
        ccx_s, ccy_s = to_svg(ccx_f, ccy_f)
        on_curve_ids: list[str] = []
        for pt in visible_points:
            pid = model[pt].ID
            if not pid or pid.startswith("X"):
                continue
            px_m = float(pt.x.evalf())
            py_m = float(pt.y.evalf())
            if abs(math.hypot(px_m - ccx_f, py_m - ccy_f) - rad_f) < 1e-7:
                on_curve_ids.append(pid)
        c_aliases: list[str] = []
        if curve.center in model and model[curve.center].ID:
            cid = model[curve.center].ID
            for pid in on_curve_ids:
                cand2 = f"( {cid} {pid} )"
                if cand2 != primary_c_ref:
                    c_aliases.append(cand2)
        c_alias_attr = f' data-aliases="{html.escape(" | ".join(c_aliases))}"' if c_aliases else ""
        c_ref_attr = f' data-ref="{html.escape(primary_c_ref)}"' if primary_c_ref else ""
        eq_c_str = f"(x - ({curve.center.x}))^2 + (y - ({curve.center.y}))^2 - ({curve.radius**2})"
        r_px = rad_f * scale
        conic_elems.append(
            f'      <circle class="geom-circle conic-curve" '
            f'cx="{_fmt(ccx_s)}" cy="{_fmt(ccy_s)}" r="{_fmt(r_px)}"'
            f'{c_ref_attr}{c_alias_attr} fill="none">'
            f"<title>{html.escape(primary_c_ref)}: {html.escape(eq_c_str)} = 0</title></circle>"
        )

    polygon_elems: list[str] = []
    for poly in visible_polygons:
        el = model[poly]
        pts_attr = " ".join(
            f"{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[0])},{_fmt(to_svg(float(v.x.evalf()), float(v.y.evalf()))[1])}"
            for v in poly.vertices
        )
        vert_ids = [model[v].ID for v in poly.vertices if v in model and model[v].ID]
        poly_ref = f"< {' '.join(vert_ids)} >" if vert_ids else el.ID
        css_cls = _polygon_css_classes(el.classes)
        polygon_elems.append(
            f'      <polygon class="{css_cls}" points="{pts_attr}" '
            f'data-ref="{html.escape(poly_ref)}" fill="none" />'
        )

    def _line_z_key(ln: spg.Line) -> int:
        cls = model[ln].classes
        if "steiner_line" in cls:
            return 40
        if "pappus" in cls or "harmonic" in cls:
            return 30
        if "carrier" in cls:
            return 20
        return 10

    sorted_lines = sorted(visible_lines, key=_line_z_key)
    line_elems: list[str] = []
    drawn_segments_px: list[tuple[float, float, float, float]] = []

    for ln in sorted_lines:
        clipped_full = _clip_line_to_rect(ln, clip_xmin, clip_xmax, clip_ymin, clip_ymax)
        if clipped_full is None:
            continue
        (fx1, fy1), (fx2, fy2) = clipped_full
        fsx1, fsy1 = to_svg(fx1, fy1)
        fsx2, fsy2 = to_svg(fx2, fy2)

        incident_pts: list[spg.Point] = []
        incident_ids: list[str] = []
        known_parents = set(model[ln].parents) | set(model[ln].pts.keys())
        for pt in visible_points:
            px, py = pt_svg_coords[pt]
            is_inc = pt in known_parents or _point_to_segment_dist(px, py, fsx1, fsy1, fsx2, fsy2) < 1e-4
            if is_inc:
                incident_pts.append(pt)
                pid = model[pt].ID
                if pid and not pid.startswith("X"):
                    incident_ids.append(pid)

        if finite_segments and len(incident_pts) >= 2:
            # Span strictly from minimum to maximum projection along the line
            dx_l = float((ln.p2.x - ln.p1.x).evalf())
            dy_l = float((ln.p2.y - ln.p1.y).evalf())
            ordered_inc = sorted(
                incident_pts,
                key=lambda p: float(p.x.evalf()) * dx_l + float(p.y.evalf()) * dy_l,
            )
            sx1, sy1 = pt_svg_coords[ordered_inc[0]]
            sx2, sy2 = pt_svg_coords[ordered_inc[-1]]
        else:
            sx1, sy1, sx2, sy2 = fsx1, fsy1, fsx2, fsy2

        smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
        drawn_segments_px.append((sx1, sy1, sx2, sy2))

        el = model[ln]
        css_cls = _line_css_classes(el.classes)
        primary_ref = el.ID if el.ID else (
            f"[ {incident_ids[0]} {incident_ids[-1]} ]" if len(incident_ids) >= 2 else ""
        )
        aliases: list[str] = []
        for i in range(len(incident_ids)):
            for j in range(i + 1, len(incident_ids)):
                for cand in (
                    f"[ {incident_ids[i]} {incident_ids[j]} ]",
                    f"[ {incident_ids[j]} {incident_ids[i]} ]",
                    f"/ {incident_ids[i]} {incident_ids[j]} /",
                ):
                    if cand != primary_ref and cand not in aliases:
                        aliases.append(cand)
        alias_attr = f' data-aliases="{html.escape(" | ".join(aliases))}"' if aliases else ""
        ref_attr = f' data-ref="{html.escape(primary_ref)}"' if primary_ref else ""
        a_sym, b_sym, c_sym = fast_line_coeffs(ln)
        eq_str = f"({a_sym})*x + ({b_sym})*y + ({c_sym})"

        line_elems.append(
            f'      <path class="{css_cls}" '
            f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}"'
            f'{ref_attr}{alias_attr} fill="none">'
            f"<title>{html.escape(primary_ref)}: {html.escape(eq_str)} = 0</title></path>"
        )

    section_elems: list[str] = []
    for sec in visible_sections:
        if isinstance(sec, Section) and len(sec.points) >= 3:
            el = model[sec]
            p_start, p_end = sec.points[0], sec.points[-1]
            sx1, sy1 = to_svg(float(p_start.x.evalf()), float(p_start.y.evalf()))
            sx2, sy2 = to_svg(float(p_end.x.evalf()), float(p_end.y.evalf()))
            smx, smy = 0.5 * (sx1 + sx2), 0.5 * (sy1 + sy2)
            sec_ids = [model[p].ID for p in sec.points if p in model and model[p].ID]
            sec_ref = f"/ {' '.join(sec_ids)} /" if sec_ids else el.ID
            seg_cls = "golden-segment" if "golden" in el.classes else "harmonic-segment"
            section_elems.append(
                f'      <path class="geom-segment {seg_cls}" '
                f'd="M {_fmt(sx1)} {_fmt(sy1)} L {_fmt(smx)} {_fmt(smy)} L {_fmt(sx2)} {_fmt(sy2)}" '
                f'data-ref="{html.escape(sec_ref)}" fill="none" />'
            )

    def _pt_z_key(pt: spg.Point) -> int:
        cls = model[pt].classes
        if "steiner" in cls:
            return 40
        if "fourth_harmonic" in cls or "harmonic" in cls or "meet" in cls:
            return 30
        if "given" in cls or "mekos" in cls:
            return 20
        return 10

    sorted_pts = sorted(visible_points, key=_pt_z_key)
    highlight_ids = set(highlight_point_ids or ())
    point_elems: list[str] = []
    label_elems: list[str] = []
    placed_label_boxes: list[tuple[float, float, float, float]] = []
    all_pt_px = [pt_svg_coords[p] for p in sorted_pts]

    candidate_angles = [
        -0.5 * math.pi,
        0.5 * math.pi,
        -0.25 * math.pi,
        -0.75 * math.pi,
        0.25 * math.pi,
        0.75 * math.pi,
        0.0,
        math.pi,
        -0.12 * math.pi,
        0.12 * math.pi,
        -0.88 * math.pi,
        0.88 * math.pi,
    ]

    for pt in sorted_pts:
        sx, sy = pt_svg_coords[pt]
        if sx < -8 or sx > width + 8 or sy < -8 or sy > height + 8:
            continue

        el = model[pt]
        pid = el.ID
        css_cls, radius = _point_css_and_radius(el.classes)
        x_latex = sp.latex(pt.x)
        y_latex = sp.latex(pt.y)
        tooltip = f"{pid} = ({pt.x}, {pt.y})"

        if pid in highlight_ids:
            point_elems.append(
                f'      <circle class="geom-point-halo" cx="{_fmt(sx)}" cy="{_fmt(sy)}" '
                f'r="{_fmt(radius + 4.4)}" fill="none" stroke="currentColor" stroke-opacity="0.38" stroke-width="1.6" />'
            )

        ref_attr = f' data-ref="{html.escape(pid)}"' if pid else ""
        point_elems.append(
            f'      <circle class="{css_cls}" cx="{_fmt(sx)}" cy="{_fmt(sy)}" r="{_fmt(radius)}"'
            f'{ref_attr} data-latex-x="{html.escape(x_latex)}" data-latex-y="{html.escape(y_latex)}">'
            f"<title>{html.escape(tooltip)}</title></circle>"
        )

        if not show_labels or not pid:
            continue
        if pid.startswith("X") and not show_aux_labels:
            continue

        base_txt, sub_txt = _split_point_label(pid, label_overrides)
        est_w = 8.8 * len(base_txt) + 6.0 * len(sub_txt) + 4.0
        est_h = 14.0
        dist_r = radius + 12.0

        best_pos = (sx + 6.0, sy - 9.0)
        best_box = (sx, sy - est_h, sx + est_w, sy)
        best_score = -1e12
        for ang in candidate_angles:
            cand_cx = sx + math.cos(ang) * (dist_r + 0.35 * est_w)
            cand_cy = sy + math.sin(ang) * (dist_r + 0.25 * est_h)
            box = (
                cand_cx - 0.5 * est_w,
                cand_cy - 0.5 * est_h,
                cand_cx + 0.5 * est_w,
                cand_cy + 0.5 * est_h,
            )

            score = 0.0
            if box[0] < 6 or box[2] > width - 6 or box[1] < 6 or box[3] > height - 6:
                score -= 500.0

            for lx1, ly1, lx2, ly2 in drawn_segments_px:
                d_line = _point_to_segment_dist(cand_cx, cand_cy, lx1, ly1, lx2, ly2)
                if d_line < 12.0:
                    score -= (12.0 - d_line) * 16.0

            for opx, opy in all_pt_px:
                d_pt = math.hypot(cand_cx - opx, cand_cy - opy)
                if d_pt < 15.0:
                    score -= (15.0 - d_pt) * 20.0

            for bx1, by1, bx2, by2 in placed_label_boxes:
                ox = max(0.0, min(box[2], bx2) - max(box[0], bx1))
                oy = max(0.0, min(box[3], by2) - max(box[1], by1))
                if ox > 0 and oy > 0:
                    score -= ox * oy * 6.0

            if score > best_score:
                best_score = score
                best_pos = (cand_cx - 0.45 * est_w, cand_cy + 0.34 * est_h)
                best_box = box

        placed_label_boxes.append(best_box)
        lx, ly = best_pos
        if sub_txt:
            inner_txt = (
                f"{html.escape(base_txt)}"
                f'<tspan class="geom-label-sub" dy="3">{html.escape(sub_txt)}</tspan>'
            )
        else:
            inner_txt = html.escape(base_txt)

        label_elems.append(
            f'      <text class="geom-label" x="{_fmt(lx)}" y="{_fmt(ly)}"'
            f"{ref_attr}>{inner_txt}</text>"
        )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic" '
        f'viewBox="0 0 {width} {height}" data-graphic-id="{html.escape(graphic_id)}" '
        f'role="img" aria-label="{html.escape(title)}">',
        f"  <title>{html.escape(title)}</title>",
        SVG_TICK_DEFS,
        "  <style>",
        EMBEDDED_SVG_STYLE,
        "  </style>",
        f'  <rect class="bg" x="0" y="0" width="{width}" height="{height}" rx="6" />',
        '  <g id="elements">',
        '    <g id="graphics">',
        *conic_elems,
        *polygon_elems,
        *line_elems,
        *section_elems,
        "    </g>",
        '    <g id="highlights"></g>',
        '    <g id="points">',
        *point_elems,
        "    </g>",
        '    <g id="labels">',
        *label_elems,
        "    </g>",
        "  </g>",
        "</svg>",
        "",
    ]
    return "\n".join(parts)


def export_svg(
    model: Model,
    output_path: str | Path,
    *,
    graphic_id: str = "g1",
    title: str = "Plato Geometric Construction",
    width: int = 680,
    height: int = 460,
    margin: float = 44.0,
    bbox: tuple[float, float, float, float] | None = None,
    focus_points: Sequence[spg.Point] | None = None,
    finite_segments: bool = True,
    include_guides: bool = False,
    show_labels: bool = True,
    show_aux_labels: bool = False,
    label_overrides: dict[str, tuple[str, str]] | None = None,
    highlight_point_ids: Sequence[str] | None = None,
) -> Path:
    """Export an interactive ``.euclid-graphic`` SVG file to ``output_path``."""
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    svg_text = render_svg_string(
        model,
        graphic_id=graphic_id,
        title=title,
        width=width,
        height=height,
        margin=margin,
        bbox=bbox,
        focus_points=focus_points,
        finite_segments=finite_segments,
        include_guides=include_guides,
        show_labels=show_labels,
        show_aux_labels=show_aux_labels,
        label_overrides=label_overrides,
        highlight_point_ids=highlight_point_ids,
    )
    target.write_text(svg_text, encoding="utf-8")
    return target.resolve()


def export_all_codex_figures(figures_dir: str | Path) -> dict[str, Path]:
    """Generate and write all 6 interactive ``.euclid-graphic`` SVG figures for the Codex.

    Args:
        figures_dir: Target directory (e.g., ``docsrc/_static/figures``).

    Returns:
        Mapping from figure filename stem to resolved :class:`~pathlib.Path`.
    """
    out_dir = Path(figures_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    written: dict[str, Path] = {}

    written["meno_diagonal_doubling"] = export_svg(
        construct_meno_diagonal_doubling(),
        out_dir / "meno_diagonal_doubling.svg",
        graphic_id="meno-diag",
        title="Meno 82b-85b: Doubling the Square by the Diagonal (Q = 4 + 4 = 8)",
        width=620,
        height=520,
        highlight_point_ids=["B", "H", "K", "D", "C"],
    )

    written["theodorus_spiral"] = export_svg(
        construct_theodorus_spiral(max_n=17),
        out_dir / "theodorus_spiral.svg",
        graphic_id="theodorus-spiral",
        title="Theaetetus 147d-148b: Theodorus's Spiral of Square-Root Powers up to 17",
        width=680,
        height=560,
        highlight_point_ids=["P1", "P4", "P9", "P16", "P17"],
    )

    written["republic_divided_line"] = export_svg(
        construct_divided_line(),
        out_dir / "republic_divided_line.svg",
        graphic_id="divided-line",
        title="Republic VI 509d-511e: The Divided Line and Equality of Pistis and Dianoia",
        width=700,
        height=440,
        bbox=(-0.6, 7.4, -0.7, 3.0),
        highlight_point_ids=["B", "C", "D", "G"],
    )

    written["timaeus_world_soul"] = export_svg(
        construct_timaeus_proportion_circles(),
        out_dir / "timaeus_world_soul.svg",
        graphic_id="timaeus-means",
        title="Timaeus 31c-36d: Arithmetic, Geometric, and Harmonic Means & Circles of the World-Soul",
        width=660,
        height=520,
        highlight_point_ids=["O", "J", "G", "H"],
    )

    written["timaeus_triangles"] = export_svg(
        construct_timaeus_triangles(),
        out_dir / "timaeus_triangles.svg",
        graphic_id="timaeus-triangles",
        title="Timaeus 54d-55a: Six Elementary 1:sqrt(3):2 Scalene Right Triangles Forming the Cosmic Face",
        width=640,
        height=540,
        highlight_point_ids=["G", "A", "B", "C", "M1", "M2", "M3"],
    )

    written["foundations_peras_compass"] = export_svg(
        construct_compass_and_peras(),
        out_dir / "foundations_peras_compass.svg",
        graphic_id="foundations-peras",
        title="Parmenides 137e, Philebus 51c & Laws VII 819d: Compass, Straight Ray & 1-sqrt(2)-sqrt(3) Triad",
        width=640,
        height=500,
        highlight_point_ids=["O", "C", "D", "E"],
    )

    return written
