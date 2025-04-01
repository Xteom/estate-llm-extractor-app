import json
import openai
from transformers import pipeline
import streamlit as st
from app.models import DocumentExtraction
from pydantic import ValidationError

def load_hf_model():
    # Using a lightweight model for demonstration.
    return pipeline("text2text-generation", model="google/flan-t5-small")

@st.cache_resource(show_spinner=False)
def get_hf_model():
    return load_hf_model()

def parse_extraction_output(output: str) -> DocumentExtraction:
    """
    Parse the LLM output (expected to be valid JSON) and return a DocumentExtraction object.
    """
    try:
        data = json.loads(output)
        extraction = DocumentExtraction(**data)
        return extraction
    except (json.JSONDecodeError, ValidationError) as e:
        raise ValueError(f"Failed to parse LLM output as JSON: {e}\nRaw output: {output}")

def extract_info_openai(text, num_pages, api_key) -> DocumentExtraction:
    """
    Use the OpenAI API to extract key information from the estate document.
    The LLM is instructed to return the result as valid JSON.
    """
    openai.api_key = api_key
    prompt = f"""Extract the following information from the estate document and output the result as valid JSON:
{{
  "client_name": "The client's name",
  "client_address": "The client's address",
  "document_date": "Document date in YYYY-MM-DD format",
  "title": "Title of the document",
  "summary": "Brief summary of the document content",
  "number_of_pages": {num_pages}
}}

Document text (truncated for brevity):
{text[:2000]}...
Please ensure the output is valid JSON.
"""
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=300,
            temperature=0.2,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        output = response.choices[0].text.strip()
        extraction = parse_extraction_output(output)
        return extraction
    except Exception as e:
        raise ValueError(f"Error during OpenAI API call: {e}")

def extract_info_hf(text, num_pages, hf_model) -> DocumentExtraction:
    """
    Use the local Hugging Face model to extract key information from the estate document.
    The LLM is instructed to output valid JSON.
    """
    prompt = f"""Extract the following information from the estate document and output the result as valid JSON:
{{
  "client_name": "The client's name",
  "client_address": "The client's address",
  "document_date": "Document date in YYYY-MM-DD format",
  "title": "Title of the document",
  "summary": "Brief summary of the document content",
  "number_of_pages": {num_pages}
}}

Document text (truncated for brevity):
{text[:1000]}...
Please ensure the output is valid JSON.
"""
    try:
        result = hf_model(prompt, max_length=300, truncation=True)
        output = result[0]['generated_text'].strip()
        extraction = parse_extraction_output(output)
        return extraction
    except Exception as e:
        raise ValueError(f"Error during Hugging Face model call: {e}")
