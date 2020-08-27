from src.entities.user import UserSchema
from src.repositories.user_repository import fetch_users, auth, delete_user, delete_users


def get_user_schema(session):
    '''
    func ro deserialise the object uers
    :param session:sqlachemy object
    :return:list of json object
    '''
    schema = UserSchema(many=True)
    user_object= fetch_users(session)
    users = schema.dump(user_object)
    return users.data

def auth_schema(user_object):
    '''

    :param session:
    :return:
    '''
    schema = UserSchema(many=True)
    return schema.dump(user_object).data


def delete_user_schema(session, id):
    schema = UserSchema(many=True)
    schema.dump(delete_user(session, id))

def delete_users_schema(session):
    schema = UserSchema(many=True)
    schema.dump(delete_users(session))