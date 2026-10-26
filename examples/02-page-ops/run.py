# 02-page-ops (pymupdf) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic document ONLY. Page indexes are 0-based throughout.
import pymupdf

doc = pymupdf.open()
for i in range(4):
    page = doc.new_page(width=612, height=792)
    page.insert_text((72, 72), f"PAGE {i + 1} SYNTHETIC", fontsize=14, fontname="helv")
doc.save("four.pdf")

src = pymupdf.open("four.pdf")
a = pymupdf.open()
a.insert_pdf(src, from_page=0, to_page=1)
a.save("split_a.pdf")
b = pymupdf.open()
b.insert_pdf(src, from_page=2, to_page=3)
b.save("split_b.pdf")
m = pymupdf.open()
m.insert_pdf(src)
m.save("merged.pdf")
mm = pymupdf.open("merged.pdf")
mm[1].set_rotation(90)
mm.save("merged_rot.pdf")

assert len(pymupdf.open("split_a.pdf")) == 2
assert len(pymupdf.open("split_b.pdf")) == 2
assert "PAGE 1 SYNTHETIC" in pymupdf.open("split_a.pdf")[0].get_text()
assert "PAGE 4 SYNTHETIC" in pymupdf.open("split_b.pdf")[1].get_text()
assert len(pymupdf.open("merged.pdf")) == 4
assert "PAGE 3 SYNTHETIC" in pymupdf.open("merged.pdf")[2].get_text()
rot = pymupdf.open("merged_rot.pdf")
assert rot[1].rotation == 90
assert "PAGE 2 SYNTHETIC" in rot[1].get_text()
print("Split: 2 + 2, Merged: 4, Rotated page 2: 90")
