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

# save metadata to json file
def save_metadata(metadata: dict, file_path: str) -> None:
    try:
        with open(file_path, 'w') as f:
            json.dump(metadata, f)
    except OSError as e:
        print(f'Error saving metadata: {e}')

input_file = 'example.txt'
output_file = 'example.json'
content = read_file(f'uploads/{input_file}')
metadata = create_metadata(content, input_file)
save_metadata(metadata, f'metadata/{output_file}')