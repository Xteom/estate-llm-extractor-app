import streamlit as st
from app.pdf_processor import extract_pdf_text
from app.llm_integration import extract_info_openai, extract_info_hf, get_hf_model

def run_app():
    st.title("Estate Document Analyzer")
    st.write(
        "Upload a PDF document related to estate planning (e.g., Will, Trust, "
        "Healthcare Directive, or Power of Attorney) for analysis."
    )
    
    # PDF file uploader widget.
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract text and number of pages from the PDF.
        text, num_pages = extract_pdf_text(uploaded_file)
        st.write(f"Extracted {num_pages} pages from the document.")

        if text:
            st.subheader("Select LLM Option")
            model_option = st.radio("Choose LLM backend for extraction:", 
                                    ("Local Hugging Face Model", "OpenAI API"))
            
            if model_option == "OpenAI API":
                api_key = st.text_input("Enter your OpenAI API key", type="password")
                if st.button("Analyze Document") and api_key:
                    with st.spinner("Analyzing document using OpenAI API..."):
                        result = extract_info_openai(text, num_pages, api_key)
                        st.subheader("Extraction Results")
                        st.text(result)
            else:
                if st.button("Analyze Document with Local Model"):
                    with st.spinner("Analyzing document using local Hugging Face model..."):
                        hf_model = get_hf_model()
                        result = extract_info_hf(text, num_pages, hf_model)
                        st.subheader("Extraction Results")
                        st.text(result)
        else:
            st.error("No text could be extracted from the PDF.")
