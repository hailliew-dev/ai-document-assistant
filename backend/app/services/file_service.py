from app.utils.text_utils import word_count
import json

# read file
def read_file(file_path: str) -> str:
    try:
        with open(file_path) as f:
            content = f.read()
    except OSError as e:
        print(e)
    return content

# create metadata
def create_metadata(content: str) -> dict:
    metadata = {
        'filename': 'example.txt',
        'word_count': word_count(content)
    }
    return metadata

# save metadata to json file
def save_metadata(metadata: dict, file_path: str) -> None:
    try:
        with open(file_path, 'w') as f:
            json.dump(metadata, f)
    except OSError as e:
        print(e)

input_file = 'uploads/example.txt'
output_file = 'metadata/example.json'
content = read_file(input_file)
metadata = create_metadata(content)
save_metadata(metadata, output_file)