import sys
import os
import glob
from pypdf import PdfReader

dir_path = "/Users/ziway/Downloads/CNS/cns.net.in.tum.de"
pdf_files = glob.glob(os.path.join(dir_path, "*.pdf"))

for pdf_file in pdf_files:
    try:
        reader = PdfReader(pdf_file)
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            if text and ("circuit switching" in text.lower() or "circuit-switching" in text.lower()):
                print(f"[{os.path.basename(pdf_file)}] Page {i+1}")
    except Exception as e:
        print(f"Error reading {pdf_file}: {e}")
