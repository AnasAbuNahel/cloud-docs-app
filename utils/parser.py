import PyPDF2
import docx

def extract_text_title(file):
    text = ""
    title = "Untitled"
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        if reader.pages:
            page = reader.pages[0]
            text = page.extract_text()
            title = text.strip().split('\n')[0] if text else "Untitled PDF"
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        text = '\n'.join([p.text for p in doc.paragraphs])
        title = text.strip().split('\n')[0] if text else "Untitled DOCX"
    return text, title