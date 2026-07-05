from fastapi import APIRouter, UploadFile
from app.models.upload_models import UploadResponseModel
from app.services.file_service import create_metadata

router = APIRouter()

# HTTPExceptions will be added later

@router.post("/upload")
async def upload(upload_file: UploadFile) -> UploadResponseModel | dict:
    # accept .txt files
    if not upload_file.filename.endswith(".txt"):
        return {"Error": "Only .txt files are allowed"}
    
    # save the file to uploads/
    try:
        upload_file_content = await upload_file.read()
    except Exception as e:
        return {'Error': f"Failed to read file: {e}"}
    else:
        upload_file_destination = f"uploads/{upload_file.filename}" 

    try:
        with open(upload_file_destination, "w", encoding="utf-8") as f:
            f.write(upload_file_content.decode())
    except Exception as e:
        print({"Error": f"Failed to save file: {e}"})
        raise
    # return metadata
    else:
        metadata = create_metadata(upload_file_content, upload_file.filename)
        return UploadResponseModel(**metadata)
