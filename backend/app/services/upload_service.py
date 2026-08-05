from app.database import engine
from sqlalchemy.orm import Session
from app.models.db.document_model import Document

def upload_service(metadata: dict) -> Document:
    document_metadata = Document(
        filename=metadata['filename'], 
        word_count=metadata['word_count'],
    )
    with Session(
        engine, 
        expire_on_commit = False
    ) as session:
        with session.begin():
            session.add(document_metadata)
            session.flush()
            session.refresh(document_metadata)

    return document_metadata
