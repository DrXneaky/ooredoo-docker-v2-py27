from sqlalchemy.orm import relationship

from src.entities.client import ClientSchema
from src.repositories.entity import Entity, Base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from marshmallow import Schema, fields


class WorkOrderRadio(Entity, Base):
    __tablename__ = 'work_order_radio'
    name = Column(String)
    creationDate = Column('creation_date', DateTime)
    vendor = Column(String)
    """ templateType = Column('template_type', String)

    client_id = Column(Integer, ForeignKey('client.id'))
    client = relationship("Client", back_populates="workorders")
    def __init__(self, name, creationDate, vendor, templateType, client):
        self.name = name
        self.creationDate = creationDate
        self.vendor = vendor
        self.templateType = templateType
        self.client = client """


class WorkOrderRadioSchema(Schema):
    id = fields.Number()
    name = fields.Str()
    vendor = fields.Str()
    creationDate = fields.DateTime('%Y-%m-%d')
    #templateType = fields.Str()
    #client = fields.Nested(ClientSchema)


    ##### client_id = fields.Integer()
