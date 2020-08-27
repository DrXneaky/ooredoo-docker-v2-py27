from src.entities.role import RoleSchema
from src.repositories.role_repository import fetch_roles, delete_role, fetch_role


def get_roles_schema(session):
    '''
    func ro deserialise the object roles
    :param session:sqlachemy object
    :return:list of json object
    '''
    schema = RoleSchema(many=True)
    roles= fetch_roles(session)
    role_roles = schema.dump(roles)
    return role_roles.data


def delete_role_schema(session, id):
    schema = RoleSchema(many=True)
    schema.dump(delete_role(session, id))


def get_role_schema(session, role_name):
    schema = RoleSchema(many=False)
    role = fetch_role(session, role_name)
    role = schema.dump(role)
    return role.data

