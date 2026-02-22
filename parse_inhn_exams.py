from pypdf import PdfReader
reader = PdfReader("/Users/ziway/Downloads/CNS/exams.pdf")
with open("/Users/ziway/Downloads/CNS/inhn_exams_dump.txt", "w") as f:
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            f.write(f"--- PAGE {i+1} ---\n")
            f.write(text + "\n\n")
