from fastapi import FastAPI, UploadFile, Form, Body
from typing import List
# from db.db import upload_data, read_data, delete_data, update_data, update_docs, delete_docs
from model.models import PropertyDetails, Server_Response, Data_Response, UpdateRequestBody, Docs_Response, DeleteDocumentRequest
from services import property_services, document_services

#Constants
app = FastAPI()
upload_folder = 'uploaded_docs'

def root():
    return {"Property CRUD app"}

#Create
@app.post("/property/create")
async def create_property(details: PropertyDetails) -> Server_Response:
    return await property_services.create_property_service(details)

#Read all
@app.get("/properties/all")
async def get_all_properties()->Data_Response:
    return await property_services.get_all_properties_service()

#Read Individual
@app.get("/properties/{property_id}")
async def get_property(property_id: int)->Data_Response:
    return await property_services.get_property_service(property_id)
    
#Delete individual data
@app.delete("/properties/delete/{property_id}")
async def delete_properties(property_id: int)->Server_Response:
    return await property_services.delete_properties_service(property_id)

#Update data
@app.put("/properties/update/{property_id}")
async def update_properties(property_id: int, data: UpdateRequestBody)->Server_Response:
    return await property_services.update_properties_service(property_id, data)
#add a document
@app.post("/property/{property_id}/add_documents")
async def add_documents(property_id: int, files: List[UploadFile] = Form(...))->Server_Response:
    return await document_services.add_docs_service(property_id, files)

@app.get("/property/{property_id}/documents")
async def add_documents(property_id: int)->Docs_Response:
    return await document_services.get_docs_service(property_id)

@app.delete("/property/{property_id}/delete_documents")
async def add_documents(body: DeleteDocumentRequest, property_id: int)->Server_Response:
    return await document_services.delete_docs_service(property_id, body.file_name)