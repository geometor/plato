r"""Exact rational harmonics of the World-Soul in Plato's *Timaeus* (35b–36b).

Implements the Demiurge's three-stage proportional division of the World-Soul:

1. **Seven Primordial Portions (*Moirai*, 35b4–c2)**:
   Double intervals :math:`1, 2, 4, 8` and triple intervals :math:`1, 3, 9, 27`.
2. **Harmonic and Arithmetic Means (35c2–36a5)**:
   Into every double and triple interval :math:`[a, b]`, insert the harmonic mean
   :math:`h = \frac{2ab}{a+b}` (exceeding and exceeded by the same fraction of the
   extremes) and the arithmetic mean :math:`m = \frac{a+b}{2}` (exceeding and
   exceeded by an equal number), generating fourths (:math:`4:3`, *epitritos*),
   fifths (:math:`3:2`, *hēmiolios*), and tones (:math:`9:8`, *epogdoos*).
3. **Diatonic Tetrachord Completion & the *Leimma* (36a6–b5)**:
   Fill every :math:`4:3` fourth with two :math:`9:8` whole tones, leaving in each
   fourth the exact minor-semitone remnant (*leimma*):

   .. math::

      \frac{4/3}{(9/8)^2} = \frac{4/3}{81/64} = \frac{256}{243}.

Across the full gamut from :math:`1` to :math:`27` (four octaves plus a major sixth),
the canonical 34-term Crantor–Proclus diatonic scale contains exactly 24 tones of
:math:`9/8` and 9 *leimmata* of :math:`256/243`:

.. math::

   \left(\frac{9}{8}\right)^{24} \cdot \left(\frac{256}{243}\right)^{9}
   = \frac{3^{48}}{2^{72}} \cdot \frac{2^{72}}{3^{45}} = 3^3 = 27.
"""

from __future__ import annotations

from dataclasses import dataclass

import sympy as sp

__all__ = [
    "CRANTOR_INTEGER_MULTIPLIER",
    "EPITRITOS",
    "EPOGDOOS",
    "HEMIOLIOS",
    "LEIMMA",
    "APOTOME",
    "COMMA_PYTHAGOREAN",
    "TimaeusPitch",
    "arithmetic_mean",
    "harmonic_mean",
    "geometric_mean_squared",
    "build_timaeus_skeleton",
    "build_timaeus_scale",
    "verify_timaeus_gamut",
]

EPOGDOOS: sp.Rational = sp.Rational(9, 8)
EPITRITOS: sp.Rational = sp.Rational(4, 3)
HEMIOLIOS: sp.Rational = sp.Rational(3, 2)
LEIMMA: sp.Rational = sp.Rational(256, 243)
APOTOME: sp.Rational = sp.Rational(2187, 2048)
COMMA_PYTHAGOREAN: sp.Rational = sp.Rational(531441, 524288)
CRANTOR_INTEGER_MULTIPLIER: int = 384


@dataclass(frozen=True)
class TimaeusPitch:
    """Single exact rational pitch in Plato's *Timaeus* World-Soul scale (35b–36b).

    Attributes:
        index: 1-based ordinal index in the ascending scale (``1..34``).
        ratio: Exact :class:`sympy.Rational` value in :math:`[1, 27]`.
        crantor_integer: Exact integer value under Crantor's multiplier :math:`384`.
        provenance: Generation stage (``"primordial"``, ``"mean"``, or ``"epogdoos"``).
        step_from_prev: Exact adjacent ratio :math:`r_k / r_{k-1}` (``None`` for ``index=1``).
        step_name: Greek interval name (``"arche"``, ``"epogdoos (9:8)"``, or ``"leimma (256:243)"``).
    """

    index: int
    ratio: sp.Rational
    crantor_integer: int
    provenance: str
    step_from_prev: sp.Rational | None
    step_name: str


def arithmetic_mean(a: sp.Rational | int, b: sp.Rational | int) -> sp.Rational:
    r"""Compute Plato's arithmetic mean :math:`\frac{a + b}{2}` (*Timaeus* 36a1–2)."""
    ra = sp.Rational(a)
    rb = sp.Rational(b)
    return (ra + rb) / sp.Integer(2)


def harmonic_mean(a: sp.Rational | int, b: sp.Rational | int) -> sp.Rational:
    r"""Compute Plato's harmonic mean :math:`\frac{2ab}{a + b}` (*Timaeus* 35c2–36a1)."""
    ra = sp.Rational(a)
    rb = sp.Rational(b)
    return (sp.Integer(2) * ra * rb) / (ra + rb)


def geometric_mean_squared(a: sp.Rational | int, b: sp.Rational | int) -> sp.Rational:
    r"""Return the exact squared geometric mean :math:`ab = m \cdot h` linking the three means."""
    ra = sp.Rational(a)
    rb = sp.Rational(b)
    return ra * rb


def build_timaeus_skeleton() -> list[sp.Rational]:
    """Build the 15-term skeleton of primordial portions and their means (*Timaeus* 35b–36a).

    Combines ``{1, 2, 4, 8}`` and ``{1, 3, 9, 27}`` with the harmonic and arithmetic
    means inserted into every double interval ``[1,2], [2,4], [4,8]`` and every triple
    interval ``[1,3], [3,9], [9,27]``.

    Returns:
        Sorted list of 15 exact :class:`sympy.Rational` values from ``1`` to ``27``.
    """
    doubles = (sp.Integer(1), sp.Integer(2), sp.Integer(4), sp.Integer(8))
    triples = (sp.Integer(1), sp.Integer(3), sp.Integer(9), sp.Integer(27))

    terms: set[sp.Rational] = {sp.Rational(x) for x in (*doubles, *triples)}
    for seq in (doubles, triples):
        for left, right in zip(seq[:-1], seq[1:], strict=True):
            terms.add(harmonic_mean(left, right))
            terms.add(arithmetic_mean(left, right))

    return sorted(terms)


def build_timaeus_scale() -> list[TimaeusPitch]:
    """Construct the complete 34-term exact rational World-Soul scale (*Timaeus* 35b–36b).

    Follows Plato's three-stage algorithm:

    1. Establish the 7 primordial portions ``{1, 2, 3, 4, 8, 9, 27}``.
    2. Insert harmonic and arithmetic means in all double and triple intervals, and
       decompose the remaining :math:`3:2` *hēmiolios* fifths ``[9, 27/2]`` and
       ``[18, 27]`` into :math:`4:3` (*epitritos*) plus :math:`9:8` (*epogdoos*)
       via ``12`` and ``24`` (Crantor & Proclus, *In Timaeum* II.168–192).
    3. Fill every :math:`4:3` fourth with two ascending :math:`9:8` tones, leaving
       the exact :math:`256:243` *leimma* at the top of each tetrachord.

    Returns:
        Ascending list of 34 :class:`TimaeusPitch` records spanning ``1`` to ``27``.
    """
    primordial_set: set[sp.Rational] = {
        sp.Rational(x) for x in (1, 2, 3, 4, 8, 9, 27)
    }
    skeleton = set(build_timaeus_skeleton())
    mean_set = skeleton - primordial_set

    # Including 12 and 24 decomposes the upper triple fifths [9, 27/2] and [18, 27]
    # into 4:3 + 9:8 exactly parallel to [4, 16/3, 6] in the third octave.
    tetrachord_skeleton = sorted(skeleton | {sp.Rational(12), sp.Rational(24)})

    all_terms: set[sp.Rational] = set(tetrachord_skeleton)
    for lo, hi in zip(tetrachord_skeleton[:-1], tetrachord_skeleton[1:], strict=True):
        ratio = hi / lo
        if ratio == EPITRITOS:
            t1 = lo * EPOGDOOS
            t2 = t1 * EPOGDOOS
            if hi / t2 != LEIMMA:
                raise ValueError(f"Expected 256/243 leimma in [{lo}, {hi}], got {hi / t2}")
            all_terms.add(t1)
            all_terms.add(t2)
        elif ratio != EPOGDOOS:
            # Note: in [4, 16/3], 9/2 is already present in skeleton, leaving 16/27 = (9/8)*(256/243)
            if lo == sp.Rational(9, 2) and hi == sp.Rational(16, 3):
                t2 = lo * EPOGDOOS
                if hi / t2 != LEIMMA:
                    raise ValueError(f"Expected 256/243 leimma in [{lo}, {hi}], got {hi / t2}")
                all_terms.add(t2)
            else:
                raise ValueError(f"Unexpected skeleton interval {ratio} on [{lo}, {hi}]")

    sorted_ratios = sorted(all_terms)
    pitches: list[TimaeusPitch] = []
    for idx, val in enumerate(sorted_ratios, start=1):
        if val in primordial_set:
            prov = "primordial"
        elif val in mean_set:
            prov = "mean"
        else:
            prov = "epogdoos"

        if idx == 1:
            step_prev = None
            step_label = "arche"
        else:
            step_prev = val / sorted_ratios[idx - 2]
            if step_prev == EPOGDOOS:
                step_label = "epogdoos (9:8)"
            elif step_prev == LEIMMA:
                step_label = "leimma (256:243)"
            else:
                step_label = str(step_prev)

        scaled_int_expr = val * CRANTOR_INTEGER_MULTIPLIER
        if not scaled_int_expr.is_integer:
            raise ValueError(f"Crantor multiplier 384 failed to clear denominator of {val}")

        pitches.append(
            TimaeusPitch(
                index=idx,
                ratio=val,
                crantor_integer=int(scaled_int_expr),
                provenance=prov,
                step_from_prev=step_prev,
                step_name=step_label,
            )
        )
    return pitches


def verify_timaeus_gamut(pitches: list[TimaeusPitch] | None = None) -> dict[str, sp.Rational | int | bool]:
    """Verify exact algebraic identities across the *Timaeus* World-Soul scale.

    Args:
        pitches: Optional precomputed scale from :func:`build_timaeus_scale`.

    Returns:
        Dictionary of verified counts and exact rational invariants.
    """
    scale = pitches if pitches is not None else build_timaeus_scale()
    steps = [p.step_from_prev for p in scale[1:] if p.step_from_prev is not None]
    tone_count = sum(1 for s in steps if s == EPOGDOOS)
    leimma_count = sum(1 for s in steps if s == LEIMMA)
    product = sp.prod(steps, start=sp.Integer(1))
    apotome = EPOGDOOS / LEIMMA
    comma = apotome / LEIMMA

    return {
        "pitch_count": len(scale),
        "tone_count": tone_count,
        "leimma_count": leimma_count,
        "total_span": product,
        "all_steps_diatonic": all(s in {EPOGDOOS, LEIMMA} for s in steps),
        "leimma": LEIMMA,
        "apotome": apotome,
        "pythagorean_comma": comma,
        "crantor_base": scale[0].crantor_integer,
        "crantor_top": scale[-1].crantor_integer,
    }
