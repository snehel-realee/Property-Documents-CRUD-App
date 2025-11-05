from database import db
from model.models import PropertyDetails, Server_Response, Data_Response, UpdateRequestBody
async def create_property_service(details: PropertyDetails)-> Server_Response:
    try:
        res = await db.create_new_property(details)
        return res
    except Exception as e:
        response = Server_Response(status=400, message=str(e))
        return response

async def get_all_properties_service()->Data_Response:
    res = await db.find_properties()
    return res

async def get_property_service(property_id: int)->Data_Response:
    res = await db.find_properties(property_id)
    return res

async def delete_properties_service(property_id: int)->Server_Response:
    res = await db.delete_property(property_id)
    return res

async def update_properties_service(property_id: int, data: UpdateRequestBody)->Server_Response:
    data = data.model_dump(exclude_defaults=True)
    res = await db.update_property(property_id, data)
    return res