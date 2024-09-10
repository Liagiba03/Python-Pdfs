import PyPDF2

pdf_path = "archivo3.pdf"
text = ''

# Context manager, enviamos ruta,  lectura en binario, 
with open(pdf_path, "rb") as file:
    lector_pdf = PyPDF2.PdfReader(pdf_path)
    for num in range(len(lector_pdf.pages)):

        # Almacenar página actual
        page = lector_pdf.pages[num]
        #Almacenar texto de esa página
        text += page.extract_text()

print(text)
