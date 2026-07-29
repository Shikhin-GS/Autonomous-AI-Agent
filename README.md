# 🤖 Autonomous AI Agent

An AI-powered Autonomous Agent built using **Python**, **FastAPI**, and **Google Gemini AI** that understands user requests, creates an execution plan, generates business documents, and exports them as Microsoft Word (.docx) files.

---

## Project Overview

This project was developed as part of the **Python AI Engineer – Autonomous Agents Assignment**.

The application accepts a natural language request, plans the required tasks, generates AI-powered content using Google Gemini, and creates a professional Word document automatically.

---

## Features

- Accepts natural language requests
- Autonomous task planning
- AI-powered content generation
- Generates Microsoft Word (.docx) documents
- FastAPI REST API
- Error handling and recovery
- Environment variable support using `.env`

---

## Tech Stack

- Python
- FastAPI
- Google Gemini AI
- python-docx
- python-dotenv

---

## Project Structure

```text
AI_AGENT_PROJECT/
│
├── app.py
├── planner.py
├── gemini_service.py
├── document_generator.py
├── requirements.txt
├── .env.example
├── README.md
└── .gitignore
```
## Project Screenshots

### Home Page

![Home](images/home.png)

### Swagger UI

![Swagger UI](images/swagger.png)

### API Response

![API Response](images/api_response.png)

### Generated Word Document

![Generated Document](images/generated_document.png)


---

## Installation

Clone the repository

```bash
git clone https://github.com/Shikhin-GS/Autonomous-AI-Agent.git
```

Move into the project

```bash
cd Autonomous-AI-Agent
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application

```bash
uvicorn app:app --reload
```

---

## API Endpoint

### POST `/agent`

Example Request

```json
{
  "request": "Create a business proposal for an AI Hospital Management System."
}
```

---

## Workflow

User Request

⬇

FastAPI API

⬇

Task Planner

⬇

Google Gemini AI

⬇

Word Document Generator

⬇

Response with Generated Document

---

## Engineering Improvement

Implemented **Error Handling & Recovery** to ensure the application handles API failures gracefully without crashing.

---

## Author

**Shikhin G S**

GitHub:
https://github.com/Shikhin-GS