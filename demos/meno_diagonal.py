"""Exact symbolic demonstration of Meno 82b–85b: Doubling the Square by the Diagonal."""

from __future__ import annotations

from geometor.model.invariants import quadrance
from rich.console import Console
from rich.table import Table

from geometor.plato.constructions import construct_meno_diagonal_doubling


def run_demo() -> None:
    """Construct Socrates' diagonal square diagram and display exact quadrances."""
    console = Console()
    model = construct_meno_diagonal_doubling()

    pt_a = model.get_element_by_ID("A")
    pt_b = model.get_element_by_ID("B")
    pt_d = model.get_element_by_ID("D")
    pt_e = model.get_element_by_ID("E")
    pt_m = model.get_element_by_ID("M")

    table = Table(title="Meno 82b–85b — Exact Square Quadrance Progression")
    table.add_column("Stage", style="cyan")
    table.add_column("Segment", style="yellow")
    table.add_column("Exact Quadrance Q (= Area)", justify="right", style="green")
    table.add_column("Linear Side", style="magenta")

    for stage, p1, p2, seg_lbl in (
        ("Given 2-foot square (82c)", pt_a, pt_b, "/ A B /"),
        ("First error: double side (82e–83c)", pt_a, pt_e, "/ A E /"),
        ("Second error: 3-foot trial (83d–e)", pt_a, pt_m, "/ A M /"),
        ("Diagonal resolution (84d–85b)", pt_b, pt_d, "/ B D /"),
    ):
        q_val = quadrance(p1, p2)
        table.add_row(stage, seg_lbl, str(q_val), f"sqrt({q_val})")

    console.print(table)
    console.print(f"[bold green]Recorded deductive steps:[/bold green] {len(model.steps)}")


if __name__ == "__main__":
    run_demo()
