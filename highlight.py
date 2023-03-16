from pdf2image import convert_from_path
from IPython.display import display

from txtmarker.factory import Factory

# Renders first page of pdf file as image
def render(path):
  images = convert_from_path(path, size=(800, None), single_file=True)
  display(images[0])

# Define highlights
highlights = [
  ("Basic", "sex work*"),
#   ("Multi-line", "Hashes are used to secure. Hashes can be deterministic or non-deterministic. Hashes can be significantly different with small changes to data or very similar."),
#   ("Regex", "This article.*Python"),
#   ("Regex Multi-line", "The above(.|\n)+is deterministic"),
#   (None, "Python provides the built-in .hash()"),
]

highlighter = Factory.create("pdf")
highlighter.highlight("/Users/moh/Developper/Thesis-Files-Total_output.pdf", "out2.pdf", highlights)

render("out2.pdf")

["sex work*",
 "sex work",
 "sex worker",
 "sex workers",
 "prostitut*",
 "prostitute",
 "prostitution",
 "prostitutes",
 "prostituted",
 "prostituting",
 "sex traffic*",
 "sex traffic",
 "sex traffickers",
 "sex trafficking",
"sex slave*",
"sex slave",
"sex slavery",
"sex slaves"]



# https://pymupdf.readthedocs.io/en/latest/recipes-annotations.html#how-to-add-and-modify-annotations
# https://www.thepythoncode.com/code/redact-and-highlight-text-in-pdf-with-python
# https://www.nobledesktop.com/learn/git/undo-changes