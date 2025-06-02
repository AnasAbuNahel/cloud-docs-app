import streamlit as st
from utils.drive import upload_to_drive
from utils.parser import extract_text_title
from utils.search import search_documents
from utils.classifier import classify_documents
import os
import time

st.set_page_config(page_title="Cloud Document Analyzer", layout="wide")

st.title("📁 Cloud-Based Document Analytics")

# Upload Documents
st.header("1. Upload PDF/DOCX Files")
uploaded_files = st.file_uploader("Choose files", type=["pdf", "docx"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Uploading files to Google Drive..."):
        uploaded_info = upload_to_drive(uploaded_files)
    st.success(f"Uploaded {len(uploaded_info)} files.")

# Extract Titles and Sort
st.header("2. Sort Documents by Title")
titles = []
if uploaded_files:
    for file in uploaded_files:
        text, title = extract_text_title(file)
        titles.append((title, file.name))

    sorted_titles = sorted(titles, key=lambda x: x[0])
    st.write("### Sorted Documents:")
    for title, filename in sorted_titles:
        st.write(f"**{title}** - {filename}")

# Search
st.header("3. Search in Documents")
query = st.text_input("Enter search text")
if query and uploaded_files:
    with st.spinner("Searching documents..."):
        results = search_documents(uploaded_files, query)
    st.write("### Search Results:")
    for result in results:
        st.markdown(result, unsafe_allow_html=True)

# Classification
st.header("4. Classify Documents")
if uploaded_files:
    with st.spinner("Classifying documents..."):
        classifications = classify_documents(uploaded_files)
    st.write("### Classification Results:")
    for fname, label in classifications:
        st.write(f"📄 {fname} → 🗂️ {label}")

# Stats
st.header("5. Statistics")
if uploaded_files:
    total_size = sum([file.size for file in uploaded_files]) / 1024
    st.metric("Number of Documents", len(uploaded_files))
    st.metric("Total Size (KB)", f"{total_size:.2f}")