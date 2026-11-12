"""Exact symbolic demonstration of Republic VI 509d–511e: The Divided Line."""

from __future__ import annotations

import sympy as sp
from geometor.model.invariants import quadrance
from rich.console import Console
from rich.table import Table

from geometor.plato.constructions import (
    construct_divided_line,
    verify_divided_line_identity,
)


def run_demo() -> None:
    """Verify the general symbolic Divided Line law and inspect the Golden Section model."""
    console = Console()
    identity = verify_divided_line_identity()
    model = construct_divided_line(ratio=sp.GoldenRatio)

    pt_a = model.get_element_by_ID("A")
    pt_b = model.get_element_by_ID("B")
    pt_c = model.get_element_by_ID("C")
    pt_d = model.get_element_by_ID("D")
    pt_e = model.get_element_by_ID("E")
    pt_g = model.get_element_by_ID("G")

    table = Table(title="Republic VI 509d–511e — Divided Line Segments (Golden Ratio phi)")
    table.add_column("Cognitive Mode", style="cyan")
    table.add_column("Segment", style="yellow")
    table.add_column("Symbolic Formula (r)", style="magenta")
    table.add_column("Exact Quadrance (r = phi)", style="green")

    rows = [
        ("Eikasia (shadows)", "/ A B /", str(identity["eikasia"]), str(sp.simplify(quadrance(pt_a, pt_b)))),
        ("Pistis (physical objects)", "/ B C /", str(identity["pistis"]), str(sp.simplify(quadrance(pt_b, pt_c)))),
        ("Dianoia (mathematics)", "/ C D /", str(identity["dianoia"]), str(sp.simplify(quadrance(pt_c, pt_d)))),
        ("Noesis (dialectic)", "/ D E /", str(identity["noesis"]), str(sp.simplify(quadrance(pt_d, pt_e)))),
        ("Mean Ordinate", "/ B G /", str(identity["dianoia"]), str(sp.simplify(quadrance(pt_b, pt_g)))),
    ]
    for mode, seg, sym_f, q_str in rows:
        table.add_row(mode, seg, sym_f, q_str)

    console.print(table)
    console.print(
        f"[bold green]Symbolic identity |BC| == |CD| for all r > 0:[/bold green] "
        f"{identity['middle_segments_equal']}"
    )


if __name__ == "__main__":
    run_demo()
