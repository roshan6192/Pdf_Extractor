import streamlit as st
import PyPDF2

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# Streamlit App
st.set_page_config(page_title="PDF Text Extractor", layout="wide")

st.title("📄 PDF Text Extractor")
st.write("Upload a PDF file and extract its text content.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Extracting text..."):
        try:
            extracted_text = extract_text_from_pdf(uploaded_file)
            st.success("Text extracted successfully!")
            st.text_area("Extracted Text", extracted_text, height=400)
        except Exception as e:
            st.error(f"Failed to extract text: {e}")
