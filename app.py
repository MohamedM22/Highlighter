import fitz

# Open the PDF file
pdf_document = "example.pdf"
doc = fitz.open(pdf_document)

# Define the sentence to be highlighted
sentence = "Franklin "

# Define the highlight color
highlight_color = (1, 1, 0)  # Yellow color in RGB format

# Create a new PDF document for the highlights
highlighted_doc = fitz.open()

# Loop through the pages of the PDF document
for page in doc:

    # Search for the sentence in the page
    search_results = page.search_for(sentence)

    # Highlight the sentence in the page
    for result in search_results:
        highlight = page.add_highlight_annot(result, color=highlight_color)
        highlighted_page = highlighted_doc.new_page()
        highlighted_page.show_pdf_page(highlight.page_number, highlight.rect)

# Save the modified PDF document
highlighted_doc.save("highlighted.pdf")

# Close the PDF documents
doc.close()
highlighted_doc.close()
