import pdfplumber

def analyze_resume(resume_file):
    with pdfplumber.open(resume_file) as pdf:
        text = " ".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    feedback = "✅ Resume is ATS-friendly" if "skills" in text.lower() else "❌ Add more skills to optimize resume"
    return feedback
