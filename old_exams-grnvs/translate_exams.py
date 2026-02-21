import os
import glob
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import pdfplumber
from openai import OpenAI

client = OpenAI()

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def translate_to_markdown(german_text, max_retries=3):
    if not german_text.strip():
        return ""
    
    prompt = (
        "You are an expert translator. The following text contains a German computer science exam or solution. "
        "Your task is to translate it entirely to English, while keeping any code snippets, formulas, or numbers intact. "
        "Format the result nicely using Markdown. Output ONLY the translated Markdown. "
        "Do not include any original German text, just the English translation. "
        "Do not wrap your result with Markdown codeblocks like ```markdown."
    )
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": prompt},
                    {"role": "user", "content": f"German Text to translate:\n\n{german_text[:100000]}"} # Avoid exceeding max length just in case
                ],
                temperature=0.3
            )
            content = response.choices[0].message.content.strip()
            # Clean up markdown code blocks if the model still adds them
            if content.startswith("```markdown"):
                content = content[11:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            return content.strip()
        except Exception as e:
            print(f"Attempt {attempt+1} failed during translation: {e}")
            time.sleep(2)
            
    return None

def process_file(pdf_path):
    folder_path = os.path.dirname(pdf_path)
    base_name = os.path.basename(pdf_path)
    md_file_name = os.path.splitext(base_name)[0] + "_en.md"
    md_path = os.path.join(folder_path, md_file_name)
    
    if os.path.exists(md_path):
        return f"Skipped {base_name} (already exists)"
        
    print(f"Extracting {base_name}...")
    german_text = extract_text_from_pdf(pdf_path)
    if not german_text:
        return f"Failed {base_name} (No text extracted)"
        
    print(f"Translating {base_name} ({len(german_text)} chars)...")
    english_markdown = translate_to_markdown(german_text)
    
    if not english_markdown:
        return f"Failed {base_name} (Translation error)"
        
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(english_markdown)
        
    return f"Success {base_name}"

def main():
    folder_path = "/Users/ziway/Downloads/old_exams-grnvs"
    pdf_files = glob.glob(os.path.join(folder_path, "*.pdf"))
    
    # Exclude cheatsheets as they are not exams/solutions
    exams_and_solutions = [f for f in pdf_files if "cheatsheet" not in os.path.basename(f).lower()]
    
    print(f"Found {len(exams_and_solutions)} exams and solutions to translate.")
    
    # Process them concurrently
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_file, pdf): pdf for pdf in exams_and_solutions}
        for future in as_completed(futures):
            print(future.result())

if __name__ == "__main__":
    main()
