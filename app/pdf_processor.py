import pdfplumber
import streamlit as st

def extract_pdf_text(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            num_pages = len(pdf.pages)
            full_text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
        return full_text, num_pages
    except Exception as e:
        st.error(f"Error processing PDF: {e}")
        return "", 0
