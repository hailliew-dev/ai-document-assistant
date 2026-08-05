from datetime import datetime
from pydantic import BaseModel, ConfigDict

# Models for the upload endpoint

# Output model
class UploadDocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    filename: str
    word_count: int
    upload_time: datetime
