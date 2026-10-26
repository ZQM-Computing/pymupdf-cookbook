# 03-redaction (pymupdf) — design-only, gate 1 target.
# Fleet invocation (Node-1): C:\geo-tools\wave11-venv\Scripts\python.exe run.py
# Synthetic document ONLY. The trap this pattern guards:
# apply_redactions deletes ANY line whose bbox intersects the redact
# rect — so the rect is the tight search_for box of the TARGET line
# only, and neighbor lines are asserted immediately after redaction.
import pymupdf

doc = pymupdf.open()
page = doc.new_page(width=612, height=792)
page.insert_text((72, 100), "KEEPER LINE ONE", fontsize=11, fontname="helv")
page.insert_text((72, 130), "SECRET VALUE 12345", fontsize=11, fontname="helv")
page.insert_text((72, 160), "KEEPER LINE THREE", fontsize=11, fontname="helv")
doc.save("before.pdf")

d = pymupdf.open("before.pdf")
p = d[0]
hits = p.search_for("SECRET VALUE 12345")
assert len(hits) == 1, hits
rect = hits[0]
# Prove the rect stays clear of both neighbor lines' boxes.
for neighbor in ("KEEPER LINE ONE", "KEEPER LINE THREE"):
    for nrect in p.search_for(neighbor):
        assert not rect.intersects(nrect), (rect, nrect)
p.add_redact_annot(rect)
p.apply_redactions()
d.save("after.pdf")

text = pymupdf.open("after.pdf")[0].get_text()
secret_gone = "SECRET" not in text and "12345" not in text
neighbors_ok = "KEEPER LINE ONE" in text and "KEEPER LINE THREE" in text
assert secret_gone and neighbors_ok, text
print(f"Secret gone: {secret_gone}, Neighbors intact: {neighbors_ok}")
