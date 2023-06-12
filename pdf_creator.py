import pdfkit

def convert_html_to_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file)
        print("La conversión de HTML a PDF se ha completado exitosamente.")
    except Exception as e:
        print(f"Ocurrió un error al convertir HTML a PDF: {str(e)}")

# Ruta del archivo HTML
html_file = "Roman Garcia CV.html"

# Ruta y nombre del archivo PDF resultante
pdf_file = "Roman Garcia CV.pdf"

# Llamar a la función para convertir HTML a PDF
convert_html_to_pdf(html_file, pdf_file)
