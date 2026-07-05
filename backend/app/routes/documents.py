from fastapi import APIRouter
from pathlib import Path
from app.models.documents_model import ListDocumentsModel

router = APIRouter()

documents_path = Path("uploads/")

@router.get("/documents")
async def get_documents() -> ListDocumentsModel:
    try:
        documents = [x.name for x in documents_path.iterdir()]
    except Exception as e:
        return {"Error": f"Failed to get documents: {e}"}
    else:
        return ListDocumentsModel(documents=documents)