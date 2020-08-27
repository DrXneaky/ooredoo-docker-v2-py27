from ..repositories.entity import Entity, Base
from sqlalchemy import Column, String, Table, ForeignKey,Integer
from sqlalchemy.orm import relationship
from marshmallow import Schema, fields


class Service(Entity, Base):
    __tablename__ = 'service'
    vrf_id = Column(String)
    vrf_name = Column(String)
    description = Column(String)
    qos = Column(Integer)

    def __init__(self, vrf_id, vrf_name,description, qos):
        self.vrf_id = vrf_id
        self.vrf_name = vrf_name
        self.description = description
        self.qos = qos

class ServiceSchema(Schema):
    id = fields.Number()
    vrf_id = fields.Str()
    vrf_name = fields.Str()
    description = fields.Str()
    qos = fields.Number()