from pydantic import BaseModel

# Models for the upload endpoint

# Output model
class UploadResponseModel(BaseModel):
    filename: str
    word_count: int
