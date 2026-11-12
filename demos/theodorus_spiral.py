"""Exact symbolic demonstration of Theaetetus 147d–148b: Theodorus's Spiral & Powers."""

from __future__ import annotations

import sympy as sp
from rich.console import Console
from rich.table import Table

from geometor.plato.constructions import (
    classify_theaetetus_powers,
    construct_theodorus_spiral,
)


def run_demo() -> None:
    """Construct Theodorus's 1..17 spiral and display Theaetetus's lengths vs. powers."""
    console = Console()
    entries = classify_theaetetus_powers(17)
    model = construct_theodorus_spiral(max_n=17)

    table = Table(title="Theaetetus 147d–148b — Lengths (Meke) vs. Powers (Dynameis)")
    table.add_column("Area n", justify="right", style="cyan")
    table.add_column("Vertex", style="yellow")
    table.add_column("Exact Spoke Quadrance", justify="right", style="green")
    table.add_column("Side Expr", style="magenta")
    table.add_column("Number Class")
    table.add_column("Line Class")

    for entry in entries:
        pt = model.get_element_by_ID(f"P{entry.area_n}")
        q_spoke = sp.expand(pt.x**2 + pt.y**2)
        table.add_row(
            str(entry.area_n),
            f"P{entry.area_n}",
            str(q_spoke),
            str(entry.side_expr),
            entry.number_kind,
            entry.line_kind,
        )

    console.print(table)


if __name__ == "__main__":
    run_demo()
