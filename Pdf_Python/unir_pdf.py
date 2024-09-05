import PyPDF2

archivos = ["archivo1.pdf", "archivo2.pdf", "archivo3.pdf"]
pdf_resultado = "resultado_pdf.pdf"

pdf_final = PyPDF2.PdfFileMerger

for nombre_archivo in archivos:
    pdf_resultado.append(nombre_archivo)

pdf_resultado.write()