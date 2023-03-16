# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------
Demo script showing how annotations can be added to a PDF using PyMuPDF.

It contains the following annotation types:
Caret, Text, FreeText, text markers (underline, strike-out, highlight,
squiggle), Circle, Square, Line, PolyLine, Polygon, FileAttachment, Stamp
and Redaction.
There is some effort to vary appearances by adding colors, line ends,
opacity, rotation, dashed lines, etc.

Dependencies
------------
PyMuPDF v1.17.0
-------------------------------------------------------------------------------
"""
from __future__ import print_function

import gc
import sys

import fitz

print(fitz.__doc__)
if fitz.VersionBind.split(".") < ["1", "17", "0"]:
    sys.exit("PyMuPDF v1.17.0+ is needed.")

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)

highlight = "this text is highlighted"
underline = "this text is underlined"
strikeout = "this text is striked out"
squiggled = "this text is zigzag-underlined"
red = (1, 0, 0)
blue = (0, 0, 1)
gold = (1, 1, 0)
green = (0, 1, 0)

displ = fitz.Rect(0, 50, 0, 50)
r = fitz.Rect(72, 72, 220, 100)
t1 = u"têxt üsès Lätiñ charß,\nEUR: €, mu: µ, super scripts: ²³!"


def print_descr(annot):
    """Print a short description to the right of each annot rect."""
    annot.parent.insert_text(
        annot.rect.br + (10, -5), "%s annotation" % annot.type[1], color=red
    )


doc = fitz.open()
page = doc.new_page()

page.set_rotation(0)



r = r + displ
annot = page.add_freetext_annot(
    r,
    t1,
    fontsize=10,
    rotate=90,
    text_color=blue,
    fill_color=gold,
    align=fitz.TEXT_ALIGN_CENTER,
)


# Adding text marker annotations:
# first insert a unique text, then search for it, then mark it
pos = annot.rect.tl + displ.tl
page.insert_text(
    pos,  # insertion point
    highlight,  # inserted text
    morph=(pos, fitz.Matrix(-5)),  # rotate around insertion point
)
rl = page.search_for(highlight, quads=True)  # need a quad b/o tilted text
annot = page.add_highlight_annot(rl[0])
print_descr(annot)


doc.save(__file__.replace(".py", "-%i.pdf" % page.rotation), deflate=True)