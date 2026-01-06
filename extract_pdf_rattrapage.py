import pypdf

pdf_path = "/Users/clementbraun/nsi-courses/interro_2025_2026/B3/B3 - Braun (2025-2027)-rattrapage ufa théorique-4866/Rattrapage_DS_B3_cybersecurite.pdf"
output_path = "/Users/clementbraun/nsi-courses/interro_2025_2026/B3/B3 - Braun (2025-2027)-rattrapage ufa théorique-4866/Rattrapage_DS_B3_cybersecurite.txt"

try:
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    with open(output_path, "w") as f:
        f.write(text)
    print("PDF extracted successfully")
except Exception as e:
    print(f"Error extracting PDF: {e}")
