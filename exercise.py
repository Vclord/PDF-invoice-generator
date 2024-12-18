import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path


filepaths = glob.glob("text/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()
    filename = Path(filepath).stem
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=0, h=8, txt=filename.capitalize(), ln=1)

pdf.output("Animal.pdf")