
import pypdf

def extract_text_from_pdf(pdf_path, output_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Successfully extracted text to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    extract_text_from_pdf("/Users/clementbraun/nsi-courses/interro_2025_2026/B3/Ds_intro/DS B3 willoquet allan.pdf", "/Users/clementbraun/nsi-courses/interro_2025_2026/B3/Ds_intro/DS_B3_willoquet_allan.txt")
