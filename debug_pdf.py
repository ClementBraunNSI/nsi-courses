import pypdf

def extract_text_from_pdf(pdf_path):
    try:
        reader = pypdf.PdfReader(pdf_path)
        print(f"Number of pages: {len(reader.pages)}")
        for i, page in enumerate(reader.pages[:5]):
            text = page.extract_text()
            print(f"--- Page {i+1} ---")
            print(f"Text length: {len(text) if text else 0}")
            if text:
                print(text[:200]) # Print start of text
            else:
                print("<No text extracted>")
    except Exception as e:
        print(f"Error extracting text: {e}")

if __name__ == "__main__":
    extract_text_from_pdf('downloaded_bloc3.pdf')
