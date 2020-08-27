from sqlalchemy.orm import relationship
from ..repositories.entity import Entity, Base
from sqlalchemy import Column, String
from marshmallow import Schema, fields

# Define the Role DataModel
class Role(Entity, Base):
    __tablename__ = 'roles'
    name = Column(String(80), unique=True)
    description = Column(String(255))
    users = relationship('User', back_populates='role')

    def __init__(self, name, description):
        self.name = name
        self.description = description

class RoleSchema(Schema):
    id = fields.Number()
    name = fields.String()
    description = fields.Str()
    # is_enabled = fields.Boolean()