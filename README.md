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

A **PyMuPDF cookbook** — PDF text, layout, and redaction from Python. Queued in wave-11 (per-node adds). Patterns are planned from the design, not yet from fleet runs. Note for the redaction pass: redaction deletes any line whose box intersects the redact rect, so keep rects clear of neighboring lines. It is intended for Developers who extract and edit PDF documents programmatically. Validate each pattern against your own data, software versions, and operating environment before adopting it.

## Repository role and status

**Status:** Active, public — seeding. Pattern passes land in follow-up work from fleet-verified setups; the tables below list what is planned, not what is already written.

**What this repository is:** PyMuPDF patterns — see the table below.

**What it contributes:** Part of the ZQM Computing geospatial portfolio. The umbrella index for the series is [geospatial-cookbooks](https://github.com/ZQM-Computing/geospatial-cookbooks).

**Standing:** This repository is maintained independently. Automated checks cover only the paths and environments configured in its workflows; they do not establish production readiness or operational certification.

## Who this is for

Developers who extract and edit PDF documents programmatically.

## Prerequisites

- PyMuPDF in the fleet Python environment
- Python 3.11+
- A sample PDF

## Patterns (planned)

| # | Example | What it will demonstrate |
|---|---------|--------------------------|
| 01 | `01-text-extract` | Extracting text with layout awareness |
| 02 | `02-page-ops` | Splitting, merging, and rotating pages |
| 03 | `03-redaction` | Redacting text safely, with neighbor-line checks |
| 04 | `04-geo-reporting` | Building geospatial reports as PDFs |

## Repository layout

```text
pymupdf-cookbook/
├── examples/          # pattern passes, landing in follow-up work
├── README.md
└── LICENSE
```

## Roadmap

- First pattern pass: the first two table rows
- Second pass: the remaining rows, from fleet-verified setups

## Contributing

A contributing guide lands with the first pattern pass. Report security issues to <zqmcomputing@gmail.com> — please do not open a public issue for those.

## More from this series

- [pdfplumber-cookbook](https://github.com/ZQM-Computing/pdfplumber-cookbook) — Table and text extraction from PDFs
- [rasterio-cookbook](https://github.com/ZQM-Computing/rasterio-cookbook) — Raster reads, windows, reprojection, and COG pairing in Python
- [geopandas-cookbook](https://github.com/ZQM-Computing/geopandas-cookbook) — GeoDataFrame patterns: joins, overlays, and spatial analysis
