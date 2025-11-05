import os
import shutil
upload_folder='uploaded_docs'
def save_file(file) -> str:
    os.makedirs(upload_folder, exist_ok=True)
    file_path=os.path.join(upload_folder, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        return file_path
    
def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)

def append_file(file_name: str):
    return os.path.join(upload_folder, file_name)