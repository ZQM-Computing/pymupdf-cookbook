# 04-geo-reporting (pymupdf) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic stations ONLY (a made-up grid, not a real place).
# Fontname trap (proven fleet lesson): NEVER reuse the pass-1 fontname
# for a later insert pass on a PDF that already carries text under it
# — glyphs missing from the old subset silently drop. Pass 2 uses a
# FRESH fontname, and every insert is verified by extraction.
import pymupdf

STATIONS = [
    ("S1", 150, 180, 12),
    ("S2", 250, 220, 25),
    ("S3", 350, 180, 30),
    ("S4", 450, 300, 44),
    ("S5", 200, 330, 61),
]

# Pass 1: build the report.
doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
page.insert_text((72, 72), "SYNTHETIC STATION REPORT", fontsize=18, fontname="helv")
page.draw_rect(pymupdf.Rect(72, 110, 540, 400), color=(0, 0, 0), width=1)
for name, x, y, _value in STATIONS:
    page.draw_circle((x, y), 5, color=(1, 0, 0), fill=(1, 0, 0), width=1)
    page.insert_text((x + 10, y + 4), name, fontsize=10, fontname="helv")
total = sum(v for _n, _x, _y, v in STATIONS)
page.insert_text((72, 430), f"Stations: {len(STATIONS)}  Values sum: {total}", fontsize=11, fontname="helv")
doc.save("report.pdf")

# Pass 2: reopen and add a footer with a FRESH fontname (tiro, not helv).
d = pymupdf.open("report.pdf")
d[0].insert_text((72, 760), "APPENDIX NOTE ADDED IN PASS 2", fontsize=9, fontname="tiro")
d.save("report_final.pdf")

text = pymupdf.open("report_final.pdf")[0].get_text()
assert "SYNTHETIC STATION REPORT" in text
assert all(name in text for name, _x, _y, _v in STATIONS)
assert "APPENDIX NOTE ADDED IN PASS 2" in text
assert total == 172
print(f"Stations: {len(STATIONS)}, Values sum: {total}, Footer present: True")
