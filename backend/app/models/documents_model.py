from datetime import datetime

from pydantic import BaseModel, ConfigDict
from app.models.upload_models import UploadDocumentResponse

class ListDocumentsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    documents: list[UploadDocumentResponse]

class DocumentModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    word_count: int
    upload_time: datetime