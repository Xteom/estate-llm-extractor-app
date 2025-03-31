from pydantic import BaseModel, Field
from typing import Optional

class DocumentExtraction(BaseModel):
    client_name: Optional[str] = Field(None, description="Client's name")
    client_address: Optional[str] = Field(None, description="Client's address")
    document_date: Optional[str] = Field(
        None, description="Document date in YYYY-MM-DD format"
    )
    title: Optional[str] = Field(None, description="Title of the document")
    summary: Optional[str] = Field(None, description="Brief summary of the document content")
    number_of_pages: int = Field(..., description="Number of pages in the document")
