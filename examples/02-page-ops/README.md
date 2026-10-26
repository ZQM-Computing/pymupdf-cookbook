# 02 — Page ops

Split, merge, and rotate pages: build a synthetic four-page PDF, split
it into two two-page PDFs, merge it back to four pages, and rotate one
page — verifying page counts, text survival, and the rotation value
at each step.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `four.pdf`,
`split_a.pdf`, `split_b.pdf`, `merged.pdf`, and `merged_rot.pdf` in
this directory.

## Expected output

```text
Split: 2 + 2, Merged: 4, Rotated page 2: 90
```

- `split_a.pdf` holds PAGE 1 and PAGE 2; `split_b.pdf` holds PAGE 3
  and PAGE 4.
- `merged.pdf` holds all four pages in order; page 3 still reads
  "PAGE 3 SYNTHETIC".
- `merged_rot.pdf` page 2 has rotation 90 and still reads
  "PAGE 2 SYNTHETIC" — rotation changes orientation, not content.

## Failure behavior

- `ModuleNotFoundError: pymupdf` — you are not in the wave11 venv;
  use the full venv Python path above.
- Page counts differ — the source fixture was edited; restore the
  four-page build loop from `run.py`, do not adjust the assertions.
- Rotation reads 0 after save — the rotated document was not saved
  before re-opening, or the wrong page index was rotated; page
  indexes are 0-based, so page 2 is index 1.

## Versions and evidence

- Tool: PyMuPDF 2.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Use `import pymupdf`; `fitz` is deprecated.
- Evidence level: design-only (gate 1 target). Page counts and the
  rotation value were derived during drafting; running them against
  the fleet venv is **to confirm at validation**.
