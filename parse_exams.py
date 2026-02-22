from pypdf import PdfReader
reader = PdfReader("/Users/ziway/Downloads/CNS/exams.pdf")
print(f"Checking {len(reader.pages)} pages...")
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    if text:
        lines = text.split("\n")
        exam_info = []
        for line in lines[:30]:
            lower_line = line.lower()
            if "exam:" in lower_line or "midterm" in lower_line or "endterm" in lower_line or "retake" in lower_line:
                exam_info.append(line.strip())
            elif "date:" in lower_line:
                exam_info.append(line.strip())
        if exam_info:
            print(f"Page {i+1}: " + " | ".join(exam_info))
