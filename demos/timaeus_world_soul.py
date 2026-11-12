"""Exact symbolic demonstration of Timaeus 31b–36d: World-Soul Harmonics & Three Means."""

from __future__ import annotations

from rich.console import Console
from rich.table import Table

from geometor.plato.constructions import construct_timaeus_proportion_circles
from geometor.plato.harmonics import build_timaeus_scale, verify_timaeus_gamut


def run_demo() -> None:
    """Display the 34-pitch World-Soul scale and construct the Pappus semicircle means."""
    console = Console()
    scale = build_timaeus_scale()
    summary = verify_timaeus_gamut()
    model = construct_timaeus_proportion_circles()

    table = Table(title="Timaeus 35b–36b — World-Soul 34-Pitch Diatonic Scale (First 12 & Final 4)")
    table.add_column("#", justify="right", style="cyan")
    table.add_column("Ratio", style="yellow")
    table.add_column("Crantor ×384", justify="right", style="green")
    table.add_column("Adjacent Interval", style="magenta")
    table.add_column("Provenance")

    selected = scale[:12] + scale[-4:]
    for pitch in selected:
        table.add_row(
            str(pitch.index),
            str(pitch.ratio),
            str(pitch.crantor_integer),
            pitch.step_name,
            pitch.provenance,
        )

    console.print(table)
    console.print(
        f"[bold green]Total pitches:[/bold green] {summary['pitch_count']} | "
        f"Tones (9/8): {summary['tone_count']} | Leimmata (256/243): {summary['leimma_count']} | "
        f"Circle model points: {len(model.points)}"
    )


if __name__ == "__main__":
    run_demo()
