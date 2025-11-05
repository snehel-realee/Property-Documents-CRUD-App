from database import db
from typing import List
from model.models import Server_Response, UpdateRequestBody, Docs_Response
from fastapi import UploadFile
from utils import utils

upload_folder = 'uploaded_docs'
async def add_docs_service(id: int, files: List[UploadFile])->Server_Response:
    file_paths = []
    for file in files:
        file_path = utils.save_file(file)
        file_paths.append(file_path)
    res = await db.create_documents(id, file_paths)
    return res
async def get_docs_service(id: int)->Docs_Response:
    res = await db.find_documents(id)
    return res

async def delete_docs_service(property_id: int, file_name:str)->Server_Response:
    file_path = utils.append_file(file_name)
    res = await db.delete_document(property_id, file_path)
    if(res.status==200):
        utils.remove_file(file_path)
    return res