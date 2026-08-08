from app.services.get_documents_service import get_all_documents
from fastapi import APIRouter
from pathlib import Path
from app.models.documents_model import ListDocumentsModel

router = APIRouter()

@router.get("/documents", response_model=ListDocumentsModel)
def get_documents():
    try:
        documents = get_all_documents()
    except Exception as e:
        return {"Error getting all documents": str(e)}

    return {"documents": documents}