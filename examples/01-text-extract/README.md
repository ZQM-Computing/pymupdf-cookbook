# 01 — Text extract

Extract text with layout awareness: build a synthetic one-page PDF,
then read it back as blocks and as words, in reading order. All text
is synthetic (a made-up report), not a real document.

## Run

```bash
C:\geo-tools\wave11-venv\Scripts\python.exe run.py
```

Use the fleet wave11 Python by full path. Never Node-1's bare
`python` (the hermes venv). The script writes `fixture.pdf` in this
directory, then re-opens it for extraction.

## Expected output

```text
Blocks: 4, Words: 10
First block: SYNTHETIC REPORT
```

- 4 non-empty blocks: title, two body lines, footer.
- 10 words: title 2, body lines 3 + 3, footer 2.
- Blocks sorted by (top, left) start with the title — that sort is
  the layout-aware reading order, not raw document order.

## Failure behavior

- `ModuleNotFoundError: pymupdf` — you are not in the wave11 venv;
  use the full venv Python path above.
- `ImportError` on `import fitz` — the old name is deprecated in
  PyMuPDF 2.0 (it raises a FutureWarning, not an error, but do not
  use it); this pattern uses `import pymupdf`.
- Block count differs — the fixture was edited; restore the four
  `insert_text` calls from `run.py`, do not adjust the assertions.

## Versions and evidence

- Tool: PyMuPDF 2.0 in Node-1's wave11-venv (wave-11A, Wally
  spot-checked). Use `import pymupdf`; `fitz` is deprecated.
- Evidence level: design-only (gate 1 target). Block/word counts
  were derived during drafting; running them against the fleet
  venv is **to confirm at validation**.
