# PyMuPDF Cookbook

<!-- ZQM-START -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <strong>ZQM Computing — Geospatial Engineering & Scientific Computing</strong><br>
  <a href="https://github.com/ZQM-Computing">ZQM Computing</a>
</p>
<!-- markdownlint-enable MD033 -->
<!-- ZQM-END -->

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

A **PyMuPDF cookbook** — PDF text, layout, and redaction from Python. Installed in wave-11 (Node-1 wave11-venv, Wally spot-checked 2026-10-25). First pattern pass written below (design-only, gate 1 target). Note for the redaction pass: redaction deletes any line whose box intersects the redact rect, so keep rects clear of neighboring lines. It is intended for Developers who extract and edit PDF documents programmatically. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public. First pattern pass written (design-only, gate 1 target — none runtime-validated on the fleet yet).

**What this repository is:** PyMuPDF patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Developers who extract and edit PDF documents programmatically.

## Prerequisites

- PyMuPDF 2.0 in Node-1's wave11-venv (`C:\geo-tools\wave11-venv`, Python 3.12.10) — invoke the venv Python by full path, never bare `python` (hermes venv); use `import pymupdf` (`fitz` is deprecated)
- Fixtures are generated at runtime by each pattern (no external PDF needed)

## Patterns

| # | Example | What it demonstrates | Status |
|---|---------|----------------------|--------|
| 01 | [examples/01-text-extract](examples/01-text-extract) | Extracting text with layout awareness | Written (design-only) |
| 02 | [examples/02-page-ops](examples/02-page-ops) | Splitting, merging, and rotating pages | Written (design-only) |
| 03 | [examples/03-redaction](examples/03-redaction) | Redacting text safely, with neighbor-line checks | Written (design-only) |
| 04 | [examples/04-geo-reporting](examples/04-geo-reporting) | Building geospatial reports as PDFs | Written (design-only) |

## Repository layout

```text
pymupdf-cookbook/
├── examples/
│   ├── 01-text-extract/
│   ├── 02-page-ops/
│   ├── 03-redaction/
│   └── 04-geo-reporting/
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: all four table rows (design-only, gate 1 target)
- Validation pass: run each pattern against the fleet environment and promote to gate 3

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [pdfplumber-cookbook](https://github.com/ZQM-Computing/pdfplumber-cookbook) — Table and text extraction from PDFs
- [rasterio-cookbook](https://github.com/ZQM-Computing/rasterio-cookbook) — Raster reads, windows, reprojection, and COG pairing in Python
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
