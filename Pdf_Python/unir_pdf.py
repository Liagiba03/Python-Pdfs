import PyPDF2
#Nombre de los archivos
archivos = ["archivo1.pdf", "archivo2.pdf", "archivo3.pdf"]

#Nombre del pdf final
nom_resultado = "resultado_pdf.pdf"

#Unir pdf
pdf_final = PyPDF2.PdfFileMerger


for nombre_archivo in archivos:
    pdf_final.append(nombre_archivo)

pdf_final.write(nom_resultado)
