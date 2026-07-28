# Autonomous AI Agent

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
## 📸 Project Screenshots

### Swagger UI

<img width="1488" height="662" alt="swagger-ui png" src="https://github.com/user-attachments/assets/4fef7268-1cfc-4bdf-bd13-db75f7af926c" />
---

### API Request

<img width="1463" height="622" alt="api-request png" src="https://github.com/user-attachments/assets/063bfa18-c90d-49dd-825a-f65a1a5ba544" />

---

### Generated Word Document

<img width="1341" height="688" alt="generated-document png" src="https://github.com/user-attachments/assets/fe536282-051f-4d22-a838-1886708735fa" />


## Engineering Improvement

Implemented **Error Handling & Recovery** to ensure the application handles API failures gracefully without crashing.

---

## Author

**Shikhin G S**

GitHub:
https://github.com/Shikhin-GS
