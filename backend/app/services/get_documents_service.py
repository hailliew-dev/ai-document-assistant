# Service to retrieve all documents from the database

from app.database import engine
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.documents_model import ListDocumentsModel, DocumentModel
from app.models.db.document_model import Document

def get_all_documents() -> ListDocumentsModel:
    stmt = select(Document)
    with Session(engine, expire_on_commit=False) as session, session.begin():
        documents = session.execute(stmt).scalars().all()

    print(f"Retrieved {len(documents)} documents from the database.")
    return documents

def get_document_by_id(id: int) -> DocumentModel:
    stmt = select(Document).where(Document.id == id)
    with Session(engine, expire_on_commit=False) as session, session.begin():
        document = session.execute(stmt).scalars().first()

    print(f"Retrieved document with id {id} from the database")
    return document
