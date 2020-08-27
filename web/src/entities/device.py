
from ..repositories.entity import Entity, Base
from sqlalchemy import Column, String
from marshmallow import Schema, fields

class Device(Entity, Base):
    __tablename__ = 'device'
    hostname = Column(String, unique=True, nullable=False)
    ipSystem = Column(String, unique=True, nullable=False)
    rd = Column(String)
    deviceType = Column(String)
    vendor = Column(String, nullable=False)
    def __init__(self, hostname, ip_system, rd, vendor, deviceType):
        self.hostname = hostname
        self.ipSystem = ip_system
        self.rd = rd
        self.vendor = vendor
        self.deviceType = deviceType

class DeviceSchema(Schema):
    hostname = fields.Str()
    ipSystem = fields.Str()
    rd = fields.Str()
    vendor = fields.Str()
    deviceType = fields.Str()
