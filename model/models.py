'''Property (Name, address, city, state, zip)'''
from pydantic import BaseModel, Field
from typing import Optional, Literal
class PropertyDetails(BaseModel):
    name: str = Field(...)
    address: str = Field(...)
    city: str = Field(...)
    state: str = Field(...)
    # zip: int = Field(..., gt=0, lt=1000000)
    zip: str = Field(...)
class UpdateRequestBody(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    # zip: int = Field(..., gt=0, lt=1000000)
    zip: Optional[str]= None

class Server_Response(BaseModel):
    status: int
    message: str

class Data_Response(Server_Response):
    data: Optional[list[PropertyDetails]]

class Docs_Response(Server_Response):
    data: Optional[list[str]]

class DeleteDocumentRequest(BaseModel):
    file_name: str