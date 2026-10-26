# 04 — Geo-reporting

Build a geospatial report as a PDF: a title, a framed map area with
five synthetic station dots and labels, and a summary line — then a
second edit pass that adds a footer, using a FRESH fontname, and
verifies the added text by extraction. All stations are synthetic
(a made-up grid), not a real place.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `report.pdf` (pass 1)
and `report_final.pdf` (pass 2) in this directory.

## Expected output

```text
Stations: 5, Values sum: 172, Footer present: True
```

- 5 station dots with labels S1–S5, values 12, 25, 30, 44, 61
  (sum 172).
- The pass-2 footer "APPENDIX NOTE ADDED IN PASS 2" is present in
  `report_final.pdf`, verified by extraction — not assumed from a
  successful insert call.
- The title and all five station labels survive both passes.

## The fontname trap (proven fleet lesson — do not skip this)

When editing a PDF that already carries text inserted under a custom
fontname (an embedded subset), reusing the SAME fontname for a later
insert silently drops the new text: glyphs missing from the old
subset are never embedded, and extraction shows nothing. Rules this
pattern follows:

1. Pass 1 inserts with fontname `helv`; pass 2 inserts with a
   DIFFERENT fontname (`tiro`, Times-Roman).
2. Every inserted text is verified by extraction after the pass that
   added it — an insert call returning normally proves nothing.

## Failure behavior

- `ModuleNotFoundError: pymupdf` — you are not in the wave11 venv;
  use the full venv Python path above.
- Footer missing from extraction — the pass-2 fontname was reused
  from pass 1 (see the trap above), or the pass-2 document was not
  saved before re-opening.
- Station labels missing — the dot/label loop was edited; restore
  the `STATIONS` list from `run.py`, do not adjust the assertions.

## Versions and evidence

- Tool: PyMuPDF 2.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Use `import pymupdf`; `fitz` is deprecated.
- Evidence level: design-only (gate 1 target). The dot count, value
  sum, and footer check were derived during drafting; running them
  against the fleet venv is **to confirm at validation**.
