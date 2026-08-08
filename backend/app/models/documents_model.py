from pydantic import BaseModel, ConfigDict
from app.models.upload_models import UploadDocumentResponse

class ListDocumentsModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    documents: list[UploadDocumentResponse]