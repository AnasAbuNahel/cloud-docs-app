from utils.parser import extract_text_title

def highlight_text(text, query):
    highlighted = text.replace(query, f"<mark>{query}</mark>")
    return highlighted

def search_documents(files, query):
    results = []
    for file in files:
        text, title = extract_text_title(file)
        if query.lower() in text.lower():
            highlighted = highlight_text(text, query)
            results.append(f"<h5>{file.name}</h5><div style='border:1px solid #ccc;padding:10px'>{highlighted[:500]}...</div><hr>")
    return results