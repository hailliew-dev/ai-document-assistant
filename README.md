# AI Document Assistant
Full-stack, AI-powered document assistant. Supports document upload, summary-generation, and question answering via LLM integration.
## 💡 What this will do
- Upload and store documents
- Generate AI-powered summaries
- Ask questions about uploaded content
- Use retrieval-based AI (RAG architecture)
## 🥅 Goals
This project is being built to:
- Learn production AI engineering workflows
- Explore LLM integrations and retrieval systems
## ⚙️ Tech Stack
Backend:
- Python
- FastAPI
- OpenAI API
Frontend:
- React
- TypeScript

## ♠️ Running locally
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
`uvicorn app.main:app --reload`

## ♣️ Running with Docker
This project includes a Dockerfile for running the backend in a reproducible containerized environment.
#### Build command
```
docker build -t ai-doc-assist:initial .
```
#### Run command
```
docker run -d -p 127.0.0.1:8000:8000 ai-doc-assist:initial
```

The API should now be available locally at:

http://localhost:8000/health

Interactive API docs:

http://localhost:8000/docs

## Project Structure
```
ai-document-assistant/
│
├── backend/
├── frontend/
├── .gitignore
└── README.md
```
#### Structure Overview
- backend/ - backend system for app functionality
- frontend/ - frontend system for user interface
- .gitignore - specifies files to remain untracked
- README.md - main application documentation

### Backend Structure
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
#### Structure Overview
- routes/ - API route handlers and endpoints
- services/ - business logic and AI workflows
- models/ - application data models and schemas
- utils/ - shared helper utilities
- main.py - backend application entrypoint
- .env - backend environment variables

### Frontend Structure
```
frontend/
│
├── src/
│   ├── app/
│       ├── globals.css
│       ├── layout.tsx
│       ├── page.tsx
```
#### Structure Overview
- src/app/ - entry point for frontend source code
- globals.css - styles to go across all pages
- layout.tsx - UI layout to go across all pages
- page.tsx - homepage of application
