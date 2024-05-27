import pdfkit

def html_to_pdf(input_html_path, output_pdf_path):
    try:
        # Convert HTML file to PDF
        pdfkit.from_file(input_html_path, output_pdf_path)
        print(f"Successfully converted {input_html_path} to {output_pdf_path}")
    except Exception as e:
        print(f"Failed to convert {input_html_path} to PDF: {e}")

if __name__ == "__main__":
    # Replace 'input.html' and 'output.pdf' with your file paths
    input_html_path = 'Contact_Aaima_Tahir.html'
    output_pdf_path = 'output.pdf'

    html_to_pdf(input_html_path, output_pdf_path)
