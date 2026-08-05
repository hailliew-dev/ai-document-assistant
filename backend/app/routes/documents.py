from fastapi import APIRouter
from pathlib import Path
# from app.models.documents_model import ListDocumentsModel

router = APIRouter()

documents_path = Path("uploads/")

@router.get("/documents")
async def get_documents():
    return {'status': 'ok'}