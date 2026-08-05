from app.utils.text_utils import word_count
import json

# read file
def read_file(file_path: str) -> str:
    try:
        with open(file_path) as f:
            content = f.read()
    except OSError as e:
        print(f'Error reading file: {e}')
        raise
    return content

# create metadata
def create_metadata(content: str, filename: str) -> dict:
    metadata = {
        'filename': filename,
        'word_count': word_count(content)
    }
    return metadata
