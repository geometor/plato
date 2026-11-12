"""Exact symbolic demonstration of Timaeus 53c–56c: Elementary Cosmic Right Triangles."""

from __future__ import annotations

from geometor.model.invariants import quadrance, vertex_spread
from rich.console import Console
from rich.table import Table

from geometor.plato.constructions import (
    construct_timaeus_cube_face,
    construct_timaeus_triangles,
)


def run_demo() -> None:
    """Verify exact quadrances and spreads of Plato's scalene and isosceles cosmic faces."""
    console = Console()
    m_scalene = construct_timaeus_triangles()
    m_cube = construct_timaeus_cube_face()

    pt_a = m_scalene.get_element_by_ID("A")
    pt_g = m_scalene.get_element_by_ID("G")
    pt_m3 = m_scalene.get_element_by_ID("M3")

    sq_a = m_cube.get_element_by_ID("A")
    sq_b = m_cube.get_element_by_ID("B")
    sq_o = m_cube.get_element_by_ID("O")

    table = Table(title="Timaeus 53c–55c — Rational Trigonometry Invariants of Elementary Triangles")
    table.add_column("Elementary Triangle", style="cyan")
    table.add_column("Quadrances (Q1, Q2, Q3)", style="green")
    table.add_column("Spreads (s1, s2, s3)", style="magenta")
    table.add_column("Cosmic Polyhedra")

    q_sc = (quadrance(pt_g, pt_m3), quadrance(pt_a, pt_m3), quadrance(pt_g, pt_a))
    s_sc = (
        vertex_spread(pt_g, pt_a, pt_m3),
        vertex_spread(pt_a, pt_g, pt_m3),
        vertex_spread(pt_a, pt_m3, pt_g),
    )
    table.add_row(
        "Scalene Half-Triangle (1 : sqrt(3) : 2)",
        f"{q_sc[0]}, {q_sc[1]}, {q_sc[2]}",
        f"{s_sc[0]}, {s_sc[1]}, {s_sc[2]}",
        "Fire (24), Air (48), Water (120)",
    )

    q_is = (quadrance(sq_o, sq_a), quadrance(sq_o, sq_b), quadrance(sq_a, sq_b))
    s_is = (
        vertex_spread(sq_o, sq_a, sq_b),
        vertex_spread(sq_o, sq_b, sq_a),
        vertex_spread(sq_a, sq_o, sq_b),
    )
    table.add_row(
        "Isosceles Right Triangle (1 : 1 : sqrt(2))",
        f"{q_is[0]}, {q_is[1]}, {q_is[2]}",
        f"{s_is[0]}, {s_is[1]}, {s_is[2]}",
        "Earth Cube (6 faces × 4 = 24)",
    )

    console.print(table)


if __name__ == "__main__":
    run_demo()
