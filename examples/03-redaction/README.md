# 03 — Redaction

Redact text safely, with neighbor-line checks: build a synthetic
three-line page, redact only the middle line, and prove the two
neighbor lines survive byte-for-byte. This pattern exists because of
a proven fleet trap — read the trap note before changing any rect.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `before.pdf` and
`after.pdf` in this directory.

## Expected output

```text
Secret gone: True, Neighbors intact: True
```

- `SECRET VALUE 12345` and every trace of it are absent from
  `after.pdf`.
- `KEEPER LINE ONE` and `KEEPER LINE THREE` are both present in
  `after.pdf`.

## The trap (proven fleet lesson — do not skip this)

`apply_redactions` deletes ANY line whose bounding box intersects the
redact rect. A rect 1.25 pt into the line above once silently deleted
a certification line on a real résumé while the target-line check
passed. Rules this pattern follows:

1. Take the rect from `search_for` on the target text — a tight box,
   not a hand-drawn estimate.
2. Keep the rect clear of neighboring line boxes: cap-top to
   descender-bottom of the TARGET line only. Here the lines sit 30 pt
   apart with an 11 pt font, so the tight rect stays ~17 pt clear of
   each neighbor.
3. Assert the neighboring lines' text immediately after redaction
   (this script does), and pixel-check the neighbor band against the
   backup before deploying any redaction to a real document.

## Failure behavior

- `ModuleNotFoundError: pymupdf` — you are not in the wave11 venv;
  use the full venv Python path above.
- Secret still present — the redact annotation was added but
  `apply_redactions` was not called, or the document was not saved
  after applying; both steps are required.
- A neighbor line missing — the rect intersected its box. Shrink
  the rect to the `search_for` box (no manual expansion) and widen
  the line spacing in the fixture before retrying.

## Versions and evidence

- Tool: PyMuPDF 2.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Use `import pymupdf`; `fitz` is deprecated.
- Evidence level: design-only (gate 1 target). The redaction and
  neighbor assertions were derived during drafting; running them
  against the fleet venv is **to confirm at validation**.
