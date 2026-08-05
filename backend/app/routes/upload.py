from fastapi import APIRouter, UploadFile
from app.services.upload_service import upload_service
from app.models.upload_models import UploadDocumentResponse
from app.services.file_service import create_metadata

router = APIRouter()

# HTTPExceptions will be added later

@router.post("/upload", response_model=UploadDocumentResponse)
def upload(upload_file: UploadFile) -> UploadDocumentResponse | dict:
    # accept .txt files
    if not upload_file.filename.endswith(".txt"):
        return {"Error": "Only .txt files are allowed"}
    # read the file
    try:
        upload_file_content = upload_file.file.read()
    except Exception as e:
        return {'Error': f"Failed to read file: {e}"}
    # return metadata
    else:
        metadata = create_metadata(upload_file_content, upload_file.filename)
        try:
            metadataResponse = upload_service(metadata)
        except Exception as e:
            print({"Error": f"Failed to save metadata to database: {e}"})
            raise
        return metadataResponse
