# Estate Document Analyzer

This project is a Streamlit application that analyzes estate planning documents (e.g., Wills, Trusts, Healthcare Directives, Powers of Attorney) by extracting key information using a Language Model (LLM).

## Features

- **PDF Selection:** Upload a PDF document for analysis.
- **PDF Processing:** Extract text and count pages using `pdfplumber`.
- **LLM Integration:** 
  - Use a local Hugging Face model (`google/flan-t5-small`) for testing.
  - Alternatively, use the OpenAI API (e.g., `text-davinci-003`) for extraction.
- **Display Results:** Extraction results are shown directly in the app.

## Project Structure

