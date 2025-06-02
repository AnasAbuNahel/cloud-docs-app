from utils.parser import extract_text_title

# تصنيف بسيط حسب كلمات مفتاحية
CLASS_TREE = {
    'Finance': ['invoice', 'receipt', 'budget', 'payment'],
    'Legal': ['contract', 'law', 'agreement'],
    'Education': ['university', 'assignment', 'exam', 'course'],
    'Medical': ['diagnosis', 'treatment', 'patient']
}

def classify_documents(files):
    results = []
    for file in files:
        text, _ = extract_text_title(file)
        category = 'Uncategorized'
        for label, keywords in CLASS_TREE.items():
            if any(word.lower() in text.lower() for word in keywords):
                category = label
                break
        results.append((file.name, category))
    return results