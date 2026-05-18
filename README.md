# AI Document Assistant
Full-stack, AI-powered document assistant. Supports document upload, summary-generation, and question answering via LLM integration.
## What this will do
- Upload and store documents
- Generate AI-powered summaries
- Ask questions about uploaded content
- Use retrieval-based AI (RAG architecture)
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
`python -m venv ./venv` or `python3 -m venv venv`
### Activate virtual environment
#### macOS/Linux:
`source venv/bin/activate`
#### Windows:
`venv\Scripts\activate`
### Install dependencies
`pip install -r requirements.txt`
### Run development server
From `/backend`: 
`uvicorn main:app --reload`

The API should now be available locally at:

http://127.0.0.1:8000/health

Interactive API docs:

http://127.0.0.1:8000/docs

## Goals

This project is being built to:

- Learn production AI engineering workflows
- Explore LLM integrations and retrieval systems
