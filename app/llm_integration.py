import openai
from transformers import pipeline
import streamlit as st

def load_hf_model():
    # Using a lightweight model for demonstration.
    return pipeline("text2text-generation", model="google/flan-t5-small")

@st.cache_resource(show_spinner=False)
def get_hf_model():
    return load_hf_model()

def extract_info_openai(text, num_pages, api_key):
    openai.api_key = api_key
    prompt = f"""Extract the following information from the estate document:
- Client Name
- Client Address
- Document Date
- Title of the document
- A brief summary of the document content
- Number of Pages (should be {num_pages})

Document text (truncated for brevity):
{text[:2000]}...
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
        return output
    except Exception as e:
        return f"Error during OpenAI API call: {e}"

def extract_info_hf(text, num_pages, hf_model):
    prompt = f"""Extract the following information from the estate document:
- Client Name
- Client Address
- Document Date
- Title of the document
- A brief summary of the document content
- Number of Pages (should be {num_pages})

Document text (truncated for brevity):
{text[:1000]}...
"""
    try:
        result = hf_model(prompt, max_length=300, truncation=True)
        output = result[0]['generated_text'].strip()
        return output
    except Exception as e:
        return f"Error during Hugging Face model call: {e}"
