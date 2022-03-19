# 20CE146
# Practical 10: Generate PDF file of your 3rd Semester Mark-sheet
from fpdf import FPDF
pdf = FPDF()    # save FPDF() class into a variable pdf
pdf.add_page()  # Add a page
pdf.set_font("Arial", size=10)  # set style and size of font
f = open("result.txt", "r")  # open the text file in read mode
for x in f:
    pdf.cell(200, 10, txt=x, ln=1, align='J')    # insert the texts in pdf
pdf.output("RESULT.pdf")   # save the pdf with name .pdf