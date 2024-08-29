from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False)

topics = pd.read_csv("topics.csv")

for index, item in topics.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=18)
    pdf.set_text_color(0,0,0)
    pdf.cell(w=0, h=12, txt=item['Topic'], ln=1)

    for y in range(25, 270, 8):
        pdf.line(10, y, 200, y)

    pdf.ln(260)
    pdf.set_font("Arial", size=8)
    pdf.set_text_color(150,150,150)
    pdf.cell(w=0, h=12, align="R", txt=item['Topic'], ln=1)

    for i in range(1, item["Pages"]):
        pdf.add_page()

        for y in range(25, 270, 8):
            pdf.line(10, y, 200, y)

        pdf.ln(270)

        pdf.set_font("Arial", size=8)
        pdf.set_text_color(150, 150, 150)
        pdf.cell(w=0, h=12, align="R", txt=item['Topic'], ln=1)


pdf.output('output.pdf')
