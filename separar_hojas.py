from PyPDF2 import PdfReader, PdfWriter

pdf_reader = PdfReader("archivo1.pdf")

#Iterar en cada hoja
for index, page in enumerate(pdf_reader.pages):
    #Creamos pdf vacío
    pdf_writer = PdfWriter()
    #Añadimos la página al pdf
    pdf_writer.add_page(page)
    #GUardar el pdf con un nombre con el index de cada página.
    with open(f"page_{index + 1}.pdf", "wb") as out:
        pdf_writer.write(out)
