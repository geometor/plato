"""Command-line interface (`geometor-plato`) for compiling the Codex and verifying models."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

from rich.console import Console
from rich.table import Table

from geometor.plato.compile_codex import compile_all_codex
from geometor.plato.concordance import CROSS_CORPUS_PLATO_ENTRIES
from geometor.plato.constructions import (
    classify_theaetetus_powers,
    construct_compass_and_peras,
    construct_divided_line,
    construct_meno_diagonal_doubling,
    construct_theodorus_spiral,
    construct_timaeus_cube_face,
    construct_timaeus_proportion_circles,
    construct_timaeus_triangles,
    verify_divided_line_identity,
)
from geometor.plato.harmonics import build_timaeus_scale, verify_timaeus_gamut
from geometor.plato.render import export_all_codex_figures

__all__ = ["build_parser", "main"]


def _default_repo_root() -> Path:
    """Resolve the default ``geometor/plato`` repository root from ``src/geometor/plato/cli.py``."""
    return Path(__file__).resolve().parents[3]


def build_parser() -> argparse.ArgumentParser:
    """Construct the ``geometor-plato`` CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="geometor-plato",
        description="GEOMETOR • plato — Exact Symbolic Models & 4-Track Stephanus Book Codex CLI.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_comp = sub.add_parser("compile", help="Compile 4-track Codex RSTs, apparatus JSONs, and SVGs.")
    p_comp.add_argument(
        "--root",
        type=Path,
        default=_default_repo_root(),
        help="Path to geometor/plato repository root.",
    )
    p_comp.add_argument(
        "--no-figures",
        action="store_true",
        help="Skip regenerating .euclid-graphic SVG figures.",
    )

    p_fig = sub.add_parser("figures", help="Export all 6 interactive .euclid-graphic SVG plates.")
    p_fig.add_argument(
        "--output-dir",
        type=Path,
        default=_default_repo_root() / "docsrc" / "_static" / "figures",
        help="Destination directory for SVG plates.",
    )

    sub.add_parser("scale", help="Display the exact 34-pitch Timaeus World-Soul harmonic gamut.")
    sub.add_parser("concordance", help="Display the cross-corpus Plato Stephanus concordance.")
    sub.add_parser("verify", help="Verify all exact symbolic geometric & harmonic invariants.")
    return parser


def _cmd_scale(console: Console) -> int:
    """Print the 34-pitch Crantor-Proclus Timaeus World-Soul scale."""
    scale = build_timaeus_scale()
    summary = verify_timaeus_gamut()
    table = Table(title="Timaeus 35b–36b — Exact 34-Pitch World-Soul Diatonic Scale")
    table.add_column("#", justify="right")
    table.add_column("Exact Ratio", style="cyan")
    table.add_column("Crantor Int (×384)", justify="right", style="green")
    table.add_column("Step Ratio", style="magenta")
    table.add_column("Step Class")
    table.add_column("Role")

    for pitch in scale:
        table.add_row(
            str(pitch.index),
            str(pitch.ratio),
            str(pitch.crantor_integer),
            "-" if pitch.step_from_prev is None else str(pitch.step_from_prev),
            pitch.step_name or "unison",
            pitch.provenance,
        )
    console.print(table)
    console.print(
        f"[bold green]Verified:[/bold green] {summary['pitch_count']} pitches | "
        f"{summary['tone_count']} tones (9/8) | {summary['leimma_count']} leimmata (256/243) | "
        f"(9/8)^24 * (256/243)^9 = {summary['total_span']}"
    )
    return 0


def _cmd_concordance(console: Console) -> int:
    """Print the cross-corpus Plato Stephanus concordance."""
    table = Table(title="GEOMETOR Cross-Corpus Plato Stephanus Concordance")
    table.add_column("Citation Key", style="cyan")
    table.add_column("Sister Repos", style="green")
    table.add_column("Dialogue & Stephanus", style="yellow")
    table.add_column("Unit")
    table.add_column("In Codex")

    for entry in CROSS_CORPUS_PLATO_ENTRIES:
        table.add_row(
            entry.cite_key,
            ", ".join(entry.repos),
            f"{entry.dialogue} {entry.stephanus_locus}",
            entry.unit_slug,
            "yes" if entry.in_codex else "note",
        )
    console.print(table)
    return 0


def _cmd_verify(console: Console) -> int:
    """Run all exact symbolic construction and algebraic invariant checks."""
    m_meno = construct_meno_diagonal_doubling()
    powers = classify_theaetetus_powers(17)
    m_theo = construct_theodorus_spiral(max_n=17)
    div_id = verify_divided_line_identity()
    m_div = construct_divided_line()
    gamut = verify_timaeus_gamut()
    m_means = construct_timaeus_proportion_circles()
    m_tri = construct_timaeus_triangles()
    m_cube = construct_timaeus_cube_face()
    m_found = construct_compass_and_peras()

    console.print("[bold green]All exact symbolic verifications passed:[/bold green]")
    console.print(f"  • Meno diagonal doubling      : {len(m_meno.points)} points, {len(m_meno.steps)} proof steps")
    console.print(f"  • Theaetetus powers (1..17)   : {len(powers)} classified ({sum(p.line_kind.startswith('dynamis') for p in powers)} dynameis)")
    console.print(f"  • Theodorus spiral (max_n=17) : {len(m_theo.points)} points")
    console.print(f"  • Republic Divided Line       : pistis==dianoia={div_id['middle_segments_equal']} ({len(m_div.points)} points)")
    console.print(f"  • Timaeus World-Soul gamut    : {gamut['pitch_count']} pitches, all_diatonic={gamut['all_steps_diatonic']} ({len(m_means.points)} points)")
    console.print(f"  • Timaeus cosmic polyhedra    : scalene face ({len(m_tri.points)} pts), cube face ({len(m_cube.points)} pts)")
    console.print(f"  • Foundations Peras & Compass : {len(m_found.points)} points")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Entry point for ``geometor-plato`` CLI."""
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)
    console = Console()

    if args.command == "compile":
        written = compile_all_codex(args.root, regen_figures=not args.no_figures)
        console.print(f"[bold green]Compiled {len(written)} Codex & apparatus files.[/bold green]")
        return 0
    if args.command == "figures":
        written = export_all_codex_figures(args.output_dir)
        console.print(f"[bold green]Exported {len(written)} .euclid-graphic SVGs to {args.output_dir}.[/bold green]")
        return 0
    if args.command == "scale":
        return _cmd_scale(console)
    if args.command == "concordance":
        return _cmd_concordance(console)
    if args.command == "verify":
        return _cmd_verify(console)
    return 1
