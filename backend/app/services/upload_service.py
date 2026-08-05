from app.database import engine
from sqlalchemy import select, Row
from sqlalchemy.orm import Session
from app.models.db.document_model import Document
from datetime import datetime, timezone

async def upload_service(metadata: dict) -> Row:
    documentMetadata = Document(filename=metadata['filename'], word_count=metadata['word_count'], upload_time=datetime.now(timezone.utc))
    stmt = select(Document).where(Document.filename == metadata['filename'])

    with Session(engine) as session, session.begin():
        session.expire_on_commit = False
        session.add(documentMetadata)
        session.execute(stmt)
        session.refresh(documentMetadata)
    return documentMetadata
