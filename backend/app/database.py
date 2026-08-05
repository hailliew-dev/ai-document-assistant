import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from app.models.db.document_model import Base

load_dotenv()

engine = create_engine(
    os.getenv("SQLALCHEMY_DATABASE_URL"), 
    echo=False)

Base.metadata.create_all(engine)
