from app.services.get_documents_service import get_all_documents, get_document_by_id
from fastapi import APIRouter
from app.models.documents_model import ListDocumentsModel, DocumentModel

router = APIRouter()

@router.get("/documents", response_model=ListDocumentsModel)
def get_documents():
    try:
        documents = get_all_documents()
    except Exception as e:
        return {"Error getting all documents": str(e)}

    return {"documents": documents}

@router.get("/documents/{id}", response_model=DocumentModel)
def get_document(id: int) -> DocumentModel:
    try: 
        document = get_document_by_id(id)
    except Exception as e:
        return {"Error getting document by id": str(e)}

    return document