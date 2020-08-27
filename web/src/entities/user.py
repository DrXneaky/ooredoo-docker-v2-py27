from sqlalchemy.orm import relationship
from ..repositories.entity import Entity, Base
from src.entities.role import RoleSchema
from sqlalchemy import Column, String, DateTime,  Boolean, Integer, ForeignKey
from marshmallow import Schema, fields
from werkzeug.security import generate_password_hash, check_password_hash

# Define the UserRoles DataModel
# class UserRoles(Entity):
#     id = Column(Integer(), primary_key=True)
#     user_id = Column(Integer(), ForeignKey('user.id', ondelete='CASCADE'))
#     role_id = Column(Integer(), ForeignKey('role.id', ondelete='CASCADE'))
#
# role_users = Table(
#     'role_users', Base.metadata,
#     Column('user_id', Integer, ForeignKey('users.id')),
#     Column('role_id', Integer, ForeignKey('roles.id'))
# )
# Define User DataModel
class User(Entity, Base):
    __tablename__ = 'users'
    name = Column(String, nullable=False, default='')
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False, unique=True)
    creationDate = Column('creation_date', DateTime)
    role_id = Column(Integer, ForeignKey('roles.id'))
    role = relationship("Role", back_populates="users")
    # registered_on = Column(DateTime, nullable=False)
    # is_enabled = Column(Boolean, nullable=False, default=False)
    # full_name = Column(String, nullable=False, default='')
    # roles = relationship('Role', secondary=role_users, backreff('users', lazy='dynamic'))
    # def __init__(self, email, password, creationDate, is_enabled, first_name, last_name):
    def __init__(self, name, email, password, creationDate, role):
        self.name = name
        self.email = email
        self.password = generate_password_hash(password,  method='sha256')
        self.creationDate = creationDate
        self.role = role
        # self.registered_on = creationDate
        # self.is_enabled = is_enabled
        # self.first_name = first_name
        # self.last_name = last_name

    # def is_active(self):
    #   return self.is_enabled
# class UserSchema(Schema):
#     id = fields.Number()
#     email = fields.Str()
#     password = fields.Str()
#     registered_on = fields.DateTime('%Y-%m-%d')
#     is_enabled = fields.Boolean()
#     first_name = fields.Str()
#     last_name = fields.Str()


class UserSchema(Schema):
    id = fields.Number()
    name = fields.String()
    email = fields.Str()
    creationDate = fields.DateTime('%Y-%m-%d')
    role = fields.Nested(RoleSchema)
    # is_enabled = fields.Boolean()





# Define UserAuth DataModel. Make sure to add flask_user UserMixin!!
# class UserAuth(Base, UserMixin):
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer(), ForeignKey('user.id', ondelete='CASCADE'))
#
#     # User authentication information
#     username = Column(String(50), nullable=False, unique=True)
#     password = Column(String(255), nullable=False, default='')
#
#     # Relationships
#     user = relationship('User', uselist=False, foreign_keys=user_id)