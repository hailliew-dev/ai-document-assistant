from pydantic import BaseModel

class ListDocumentsModel(BaseModel):
    documents: list[str]
