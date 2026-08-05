import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.models.db.document_model import Base

load_dotenv()

database_url = os.getenv("SQLALCHEMY_DATABASE_URL")

if not database_url:
    raise RuntimeError(
        "SQLALCHEMY_DATABASE_URL environment variable is not configured"
    )

engine = create_engine(
    database_url, 
    echo=False
)

Base.metadata.create_all(engine)
