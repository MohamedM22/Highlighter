import fitz




print(fitz.__doc__)
print(fitz.__annotations__)


pdf_doc = fitz.open("/Users/moh/Developper/Thesis-Files-Total_output.pdf")
pages_num = pdf_doc.page_count
for i in range(pages_num):
    page = pdf_doc[i]
    full_text = page.get_text('text')
    keyword = page.search_for("sex worker", quads = True)
    annot = page.add_highlight_annot(keyword[0])
    pdf_doc.save(__file__.replace(".py", "-%i.pdf" % page.rotation), deflate=True)
    print(f"{full_text}")
pdf_doc.close()