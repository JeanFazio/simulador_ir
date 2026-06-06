from datetime import datetime
from reportlab.pdfgen import canvas



def exportar_txt(texto, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)


def exportar_pdf(texto, caminho):
    pdf = canvas.Canvas(caminho)

    pdf.setTitle("Relatório do Simulador de IR")

    y = 800

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(50, y, "Relatório - Simulador de Imposto de Renda")
    y -= 30

    pdf.setFont("Helvetica", 10)
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    pdf.drawString(50, y, f"Gerado em: {data_atual}")
    y -= 30

    pdf.line(50, y, 550, y)
    y -= 30

    pdf.setFont("Helvetica", 11)

    for linha in texto.split("\n"):
        pdf.drawString(50, y, linha)
        y -= 18

        if y < 50:
            pdf.showPage()
            y = 800
            pdf.setFont("Helvetica", 11)

    pdf.save()