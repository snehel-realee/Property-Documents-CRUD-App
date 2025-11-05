from fastapi import FastAPI
from model.models import PropertyDetails
from database import db
#Constants
app = FastAPI()
upload_folder = 'uploaded_docs'

def root():
    return {"Property CRUD app"}

@app.post("/property/details")
async def create_property(details: PropertyDetails):
    try:
        res = await db.create_new_property(details)
    except Exception as e:
        return {"error": str(e),"from": "main.py"}