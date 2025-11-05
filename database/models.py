from sqlalchemy import String, Column, Integer, ForeignKey
from database.client import client, Base, conn

class Property(Base):
    __tablename__ = "Property"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

class Documents(Base):
    __tablename__ = "Documents"
    id=Column(Integer, primary_key=True)
    document=Column(String)
    property_id=Column(Integer, ForeignKey("Property.id"))

# Base.metadata.create_all(conn)