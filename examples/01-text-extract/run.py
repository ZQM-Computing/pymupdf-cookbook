# 01-text-extract (pymupdf) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic document ONLY. Writes fixture.pdf, then re-opens it for extraction.
import pymupdf

doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
page.insert_text((72, 72), "SYNTHETIC REPORT", fontsize=18, fontname="helv")
page.insert_text((72, 110), "Alpha station reading", fontsize=11, fontname="helv")
page.insert_text((72, 130), "Bravo station reading", fontsize=11, fontname="helv")
page.insert_text((72, 760), "Footer note", fontsize=9, fontname="helv")
doc.save("fixture.pdf")

doc2 = pymupdf.open("fixture.pdf")
p = doc2[0]
blocks = [b for b in p.get_text("blocks") if b[4].strip()]
words = p.get_text("words")
ordered = sorted(blocks, key=lambda b: (b[1], b[0]))
assert len(blocks) == 4, blocks
assert len(words) == 10, words
assert ordered[0][4].strip().startswith("SYNTHETIC REPORT"), ordered[0][4]
print(f"Blocks: {len(blocks)}, Words: {len(words)}")
print(f"First block: {ordered[0][4].strip()}")
