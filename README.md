# AI Document Assistant
Full-stack, AI-powered document assistant. Supports document upload, summary-generation, and question answering via LLM integration.
## What this will do
- Upload and store documents
- Generate AI-powered summaries
- Ask questions about uploaded content
- Use retrieval-based AI (RAG architecture)
## Goals
This project is being built to:
- Learn production AI engineering workflows
- Explore LLM integrations and retrieval systems
## Tech Stack
Backend:
- Python
- FastAPI
- OpenAI API
Frontend:
- React
- TypeScript

## Running locally
### Create virtual environment
`cd backend`
`python -m venv venv` or `python3 -m venv venv`
### Activate virtual environment
#### macOS/Linux:
`source venv/bin/activate`
#### Windows:
`venv\Scripts\activate`
### Install dependencies
`pip install -r requirements.txt`
### Run development server
`cd backend`
`uvicorn main:app --reload`

The API should now be available locally at:

http://127.0.0.1:8000/health

Interactive API docs:

http://127.0.0.1:8000/docs

## Backend Structure
```
backend/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   └── utils/
│
├── requirements.txt
└── .env
```
### Structure Overview
- routes/ — API route handlers and endpoints
- services/ — business logic and AI workflows
- models/ — application data models and schemas
- utils/ — shared helper utilities
- main.py — backend application entrypoint
- .env — backend environment variables
