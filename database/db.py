from database.client import client
from database.models import Property, Documents
from model.models import Server_Response, Data_Response, PropertyDetails, Docs_Response
async def create_new_property(details) -> Server_Response:
    try:
        new_property = Property(name=details.name, address=details.address, city=details.city, state=details.state, zip=details.zip)
        client.add(new_property)
        client.commit()
        response = Server_Response(status=200, message="Data added successfully")
        return response
    except Exception as e:
        response = Server_Response(status=400, message=str(e))
        return response


async def find_properties(id: int=None)-> Data_Response:
    try:
        if(not id):
            properties = client.query(Property).all()
            property_list = []
            for p in properties:
                property_detail = PropertyDetails(
                    name=p.name,
                    address=p.address,
                    city=p.city,
                    state=p.state,
                    zip=p.zip
                )
                property_list.append(property_detail)
            response = Data_Response(status=200, message="Success", data=property_list)
            return response
        else:
            print("ID", id)
            property = client.query(Property).where(Property.id == id).all()
            data = PropertyDetails(name=property[0].name, address=property[0].address, city=property[0].city, state=property[0].state, zip=property[0].zip)
            response = Data_Response(status=200, message="Success", data=[data])
            return response

    except Exception as e:
        response = Data_Response(status=400, message=str(e), data=None)
        return response

async def delete_property(id: int)->Server_Response:
    try:
        client.query(Property).filter(Property.id == id).delete()
        client.commit()
        return Server_Response(status=200, message="Data deleted successfully")
    except Exception as e:
        return Server_Response(status=400, message=str(e))


async def update_property(property_id, data)->Server_Response:
    try:
        print(data)
        client.query(Property).filter(Property.id == property_id).update(data)
        client.commit()
        return Server_Response(status=200, message="Data updated successfully")
    except Exception as e:
        return Server_Response(status=400, message=str(e))
    
async def create_documents(property_id: int, file_paths: list[str])->Server_Response:
    new_docs = [
            Documents(document=path, property_id=property_id)
            for path in file_paths
        ]
    # Add them all at once
    client.add_all(new_docs)
    client.commit()
    return Server_Response(status=200, message="Docs added successfully")

async def find_documents(property_id: int)->Docs_Response:
    try:
        docs = client.query(Documents).where(Documents.property_id == property_id).all()
        docs = [doc.document for doc in docs]
        return Docs_Response(status=200, message="Success", data=docs)
    except Exception as e:
        response = Docs_Response(status=400, message=str(e), data=None)
        return response

async def delete_document(property_id: int, file_name: str)->Server_Response:
    try:
        client.query(Documents).filter(Documents.property_id == property_id, Documents.document == file_name).delete()
        client.commit()
        return Server_Response(status=200, message="Data deleted successfully")
    except Exception as e:
        return Server_Response(status=400, message=str(e))

# Base.metadata.create_all(conn)
# client = clientmaker(bind=conn)
# client = client()
# client.commit()


