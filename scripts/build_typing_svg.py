"""Generate assets/typing.svg, the terminal-style typing line under the hero.

Edit PHRASES and run:

    python scripts/build_typing_svg.py

The animation is plain SMIL (no script, no external service), so it works when
GitHub serves the SVG as an image. If animation is unavailable, the first
phrase is shown in full with a cursor, which is the intended static state.
"""

from __future__ import annotations

from pathlib import Path
from xml.sax.saxutils import escape

PHRASES = [
    "Engineering practical software",
    "Building Windows desktop applications",
    "Automation & developer utilities",
    "Shipping better desktop experiences",
]

OUT = Path(__file__).resolve().parent.parent / "assets" / "typing.svg"

SLOT = 4.0          # seconds each phrase owns
TYPE_STEP = 0.055   # seconds per typed character
HOLD_UNTIL = 3.1    # seconds into the slot when deleting starts
ERASE_STEP = 0.018  # seconds per deleted character
CHAR_W = 12         # px per character (text is forced to this pitch)
TEXT_X = 52
HEIGHT = 52


def timeline(n: int, cycle: float) -> tuple[str, str]:
    """Discrete width values and keyTimes for typing then deleting n characters."""
    times, values = [], []
    for k in range(n + 1):
        times.append(k * TYPE_STEP)
        values.append(k * CHAR_W)
    for k in range(1, n + 1):
        times.append(HOLD_UNTIL + k * ERASE_STEP)
        values.append((n - k) * CHAR_W)
    key_times = ";".join(f"{t / cycle:.5f}" for t in times)
    return ";".join(str(v) for v in values), key_times


def main() -> None:
    cycle = SLOT * len(PHRASES)
    longest = max(len(p) for p in PHRASES)
    width = TEXT_X + longest * CHAR_W + 40
    clips, texts, cursors = [], [], []

    for i, phrase in enumerate(PHRASES):
        n = len(phrase)
        full = n * CHAR_W
        values, key_times = timeline(n, cycle)
        cursor_values = ";".join(str(TEXT_X + int(v) + 2) for v in values.split(";"))
        static_w = full if i == 0 else 0
        begin = f"{i * SLOT:g}s"
        common = f'dur="{cycle:g}s" begin="{begin}" repeatCount="indefinite" calcMode="discrete" keyTimes="{key_times}"'

        clips.append(
            f'<clipPath id="t{i}"><rect x="{TEXT_X}" y="8" height="36" width="{static_w}">'
            f'<animate attributeName="width" values="{values}" {common}/></rect></clipPath>'
        )
        texts.append(
            f'<text x="{TEXT_X}" y="33" textLength="{full}" lengthAdjust="spacingAndGlyphs" '
            f'clip-path="url(#t{i})">{escape(phrase)}</text>'
        )
        visible_until = (SLOT - 0.05) / cycle
        cursors.append(
            f'<rect x="{TEXT_X + static_w + 2}" y="16" width="11" height="21" rx="1.5" '
            f'opacity="{1 if i == 0 else 0}">'
            f'<animate attributeName="x" values="{cursor_values}" {common}/>'
            f'<animate attributeName="opacity" values="1;0" keyTimes="0;{visible_until:.5f}" '
            f'dur="{cycle:g}s" begin="{begin}" repeatCount="indefinite" calcMode="discrete"/></rect>'
        )

    alt = " · ".join(PHRASES)
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{HEIGHT}" viewBox="0 0 {width} {HEIGHT}" role="img" aria-label="{escape(alt)}">
  <title>{escape(alt)}</title>
  <defs>
    {chr(10).join('    ' + c for c in clips).strip()}
  </defs>
  <rect x=".75" y=".75" width="{width - 1.5}" height="{HEIGHT - 1.5}" rx="{(HEIGHT - 1.5) / 2}" fill="#0B1020" stroke="#263451" stroke-width="1.5"/>
  <g font-family="'Cascadia Mono', Consolas, 'SF Mono', Menlo, 'DejaVu Sans Mono', monospace" font-size="20">
    <text x="26" y="33" fill="#65D6E6">›</text>
    <g fill="#F0F4FA">
    {chr(10).join('      ' + t for t in texts).strip()}
    </g>
  </g>
  <g fill="#65D6E6">
    <animate attributeName="opacity" values="1;0.15" keyTimes="0;0.5" dur="1.05s" repeatCount="indefinite" calcMode="discrete"/>
    {chr(10).join('    ' + c for c in cursors).strip()}
  </g>
</svg>
"""
    OUT.write_text(svg, encoding="utf-8")
    print(f"wrote {OUT} ({len(svg)} bytes, {width}x{HEIGHT})")


if __name__ == "__main__":
    main()
