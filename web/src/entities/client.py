from sqlalchemy.orm import relationship

from src.entities.service import ServiceSchema
from ..repositories.entity import Entity, Base
# from .service import Service
from sqlalchemy import Column, String, Table, ForeignKey,Integer
from marshmallow import Schema, fields

client_service = Table(
    'client_service', Base.metadata,
    Column('service_id', Integer, ForeignKey('service.id')),
    Column('client_id', Integer, ForeignKey('client.id'))
)
class Client(Entity, Base):
    __tablename__ = 'client'
    name = Column(String)
    code = Column(String)
    workorders = relationship('WorkOrder', back_populates='client')
    services = relationship("Service", secondary=client_service)

    def __init__(self, name, code, services):
        self.name = name
        self.code = code
        self.services = services

class ClientSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    code = fields.Str()
    services = fields.List(fields.Nested(ServiceSchema))
