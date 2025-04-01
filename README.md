# Estate Document Analyzer

```
currently abandoned

links I may need when I continue this proyect
* https://www.perplexity.ai/search/i-need-to-build-this-applicati-gw1_FbOsRn.42ezyY_J3Vg
* https://www.buchalter.com/wp-content/uploads/2024/03/Estate-Planning-Guide-and-Questionnaire-for-2024-fillable.pdfv2_.pdf
* https://www.rocketlawyer.com/family-and-personal/estate-planning/make-a-will/legal-guide/sample-will
```


This project is a Streamlit application that analyzes estate planning documents (e.g., Wills, Trusts, Healthcare Directives, Powers of Attorney) by extracting key information using a Language Model (LLM). It leverages Pydantic to validate and structure the extracted information.

## Features

- **PDF Selection:** Upload a PDF document for analysis.
- **PDF Processing:** Extract text and count pages using `pdfplumber`.
- **LLM Integration:** 
  - Use a local Hugging Face model (`google/flan-t5-small`) for testing.
  - Alternatively, use the OpenAI API for extraction.
- **Structured Output:** The extraction result is parsed into a Pydantic model (`DocumentExtraction`), ensuring data consistency.
- **Display Results:** Extraction results are shown in the app as structured JSON.

## Project Structure

```
estate-document-analyzer/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── llm_integration.py
│   ├── pdf_processor.py
│   └── ui.py
├── Dockerfile
├── docker-compose.yml
├── main.py
├── requirements.txt
└── README.md
```

## Setup

### Prerequisites

- Python 3.8 or later
- Git
- Docker (if you want to containerize the app)

### Local Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/estate-document-analyzer.git
   cd estate-document-analyzer
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**

   ```bash
   streamlit run main.py
   ```

### Docker Setup

1. **Build and run with Docker:**

   ```bash
   docker build -t estate-document-analyzer .
   docker run -p 8501:8501 estate-document-analyzer
   ```

   Alternatively, use Docker Compose:

   ```bash
   docker-compose up --build
   ```

The app will be available at http://localhost:8501.
