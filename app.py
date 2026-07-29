from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from planner import create_plan
from gemini_service import generate_document
from document_generator import create_word_document

app = FastAPI(title="Autonomous AI Agent")


class AgentRequest(BaseModel):
    request: str


@app.get("/")
def home():
    return {
        "message": "Autonomous AI Agent is Running!"
    }


# Existing API - Returns JSON
@app.post("/agent")
def run_agent(data: AgentRequest):

    # Error Handling
    if not data.request.strip():
        raise HTTPException(
            status_code=400,
            detail="Request cannot be empty."
        )

    # Step 1: Planning
    tasks = create_plan(data.request)

    # Step 2: Generate Content
    ai_content = generate_document(data.request)

    # Step 3: Generate Word Document
    document_path = create_word_document(ai_content)

    # Step 4: Return JSON Response
    return {
        "status": "success",
        "user_request": data.request,
        "execution_plan": tasks,
        "generated_document": document_path,
        "generated_content": ai_content
    }


# New API - Downloads the Word Document
@app.post("/download-document")
def download_document(data: AgentRequest):

    # Error Handling
    if not data.request.strip():
        raise HTTPException(
            status_code=400,
            detail="Request cannot be empty."
        )

    # Generate Content
    ai_content = generate_document(data.request)

    # Generate Word Document
    document_path = create_word_document(ai_content)

    # Return the generated Word document as a download
    return FileResponse(
        path=document_path,
        filename="Generated_Document.docx",
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )