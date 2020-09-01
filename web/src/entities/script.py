

from src.repositories.entity import Entity, Base
from sqlalchemy import Column, String, Table, DateTime, Integer, Text, ForeignKey
from marshmallow import Schema, fields
from src.entities.device import Device, DeviceSchema
from sqlalchemy.orm import relationship

script_device = Table('script_device', Base.metadata, Column('script_id', Integer, ForeignKey('script.id')),Column('device_id', Integer, ForeignKey('device.id')))


class Script(Entity, Base):
  __tablename__= 'script'
  creationDate = Column('creation_date', DateTime)
  scriptName = Column('script_name', String)
  target = Column(String)
  scriptType = Column('script_type',String)
  status = Column(String)
  report = Column(Text)
  log = Column(Text)
  devices = relationship('Device', secondary ='script_device')


  def __init__(self, creationDate, scriptName, target, scriptType, status, report, log, devices):
    self.creationDate = creationDate
    self.scriptName = scriptName
    self.target = target
    self.scriptType = scriptType
    self.status = status
    self.report = report
    self.log = log
    self.devices = devices
  

class ScriptSchema(Schema):
  id = fields.Number()
  creationDate = fields.DateTime("%Y-%m-%d, %H:%M:%S")
  scriptName = fields.Str()
  target = fields.Str()
  scriptType = fields.Str()
  status = fields.Str()
  report = fields.Str()
  log = fields.Str()
  devices = fields.List(fields.Nested(DeviceSchema))

