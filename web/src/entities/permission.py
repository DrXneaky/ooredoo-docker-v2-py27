
from ..repositories.entity import Entity, Base
from sqlalchemy import Column, String
from marshmallow import Schema, fields
print(Base)
# Define the Role DataModel
class Permission(Entity, Base):
    __tablename__ = 'permissions'
    perm_desc = Column(String(50), unique=True, nullable=False)
    def __init__(self, perm_desc):
        self.perm_desc = perm_desc
