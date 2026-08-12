# AI Document Assistant
Full-stack, AI-powered document assistant. Supports document upload, summary-generation, and question answering via LLM integration.
## 🥅 Goals
This project is being built to:
- Learn production AI engineering workflows
- Explore LLM integrations and retrieval systems
## ✅ Current Capabilities
- Accept  `.txt` files uploads
- Read uploaded `.txt` files
- Calculate word counts
- Save uploaded file metadata (currently, not file contents) to database
- Return file metadata to client
- Retrieve all uploaded documents (metadata)
- Retrieve one uploaded document (metadata)
## 💡 Planned Capabilities
✅ ~~- Upload and store documents~~
- Generate AI-powered summaries
- Ask questions about uploaded content
- Use retrieval-based AI (RAG architecture)
## ⚙️ Tech Stack
Backend:
- Python
- FastAPI
- OpenAI API
- PostgreSQL (+ SQLAlchemy, psycopg)
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
`uvicorn app.main:app --reload`

## ♣️ Running with Docker
*NOTE: Updated Dockerfile is pending database persistence changes*
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

http://localhost:8000

## 🔻 API Endpoints 
### GET `/health`
Returns service status.

### POST `/upload`
Accepts `.txt` files.
Returns document metadata.

### GET `/docs`
Interactive API docs.
Use this to test `/upload` endpoint.

### GET `/documents`
Returns all documents.

### GET `/document{id}`
Returns one document's metadata by ID.

## 🏛️ Project Structure
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

### 🔙 Backend Structure
```
backend/
│
├── app/
│   ├── main.py
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── database.py
├── requirements.txt
└── .env.example
```
#### Structure Overview
- main.py - backend application entry point
- routes/ - API route handlers and endpoints
- services/ - business logic and AI workflows
- models/ - application data models and schemas
- utils/ - shared helper utilities
- database.py - PostgreSQL database connection file
- requirements.txt - installed dependencies
- .env.example - backend environment variable example

### 📊 Database Setup
#### Database Stack
- PostgreSQL - relational database that stores document records
- SQLAlchemy - maps Python models to database tables and manages database sessions and transactions
- psycopg - provides the PostgreSQL driver used by SQLAlchemy
#### Document Table
Column - Description
- id - Unique identifier for the document record
- filename - Original uploaded filename
- word_count - Calculated number of words in the document
- upload_time - Time the record was created
The current implementation stores document metadata rather than the uploaded file contents.
#### Environment Configuration
Create a `.env` file and provide a PostgreSQL connection URL:
`SQLALCHEMY_DATABASE_URL=postgresql+psycopg://USERNAME:PASSWORD@localhost:5432/DATABASE_NAME`
#### Persistence Flow
When a document is uploaded, the application:
- reads and processes the document;
- calculates its metadata;
- creates a SQLAlchemy document record;
- commits the record to PostgreSQL; and
- returns the stored document information in the API response.

#### Verifying Persistence
After uploading documents, connect to PostgreSQL and run:

`SELECT * FROM documents;`

The records should remain present after the FastAPI server is stopped and restarted.

### ➡️ Frontend Structure
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

## Current utilities & services
`utils/text_utils.py`
Functions:
- `clean_text()` - Cleans text of extra spaces, preserving capitalization, puncutation, and newlines
- `word_count()` - Returns word count

`services/file_service.py`
Functions:
- `read_file()` - Reads file contents
- `create_metadata()` - Creates metadata dictionary for filename and word count

`services/upload_service.py`
Functions:
- `upload_service()` - Saves document metadata to database

`services/get_documets_service`
Functions:
- `get_documents()` - Returns all document metadata
- `get_one_document()` - Returns one document's metadata by ID
