from src.entities.user import UserSchema
from ..entities.user import User
from werkzeug.security import  check_password_hash, generate_password_hash
from ..commons.utils.token_manager import *
from src.repositories.role_repository import fetch_role
from src.controllers.role_controller import get_role_schema



""" def generate_user(session, json_data):
    user = User(json_data["email"], json_data["password"])
    session.add(user)
    session.commit()


def check_user(session, json_data, secrete_key):
    user = session.query(User).filter(User.email == json_data['email']).first()
    if user :
        if check_password_hash(user.password, json_data['password']):
            auth_token = encode_auth_token(user.password, secrete_key)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                #'auth_token': auth_token.decode()}
                'auth_token': auth_token}
            return responseObject, 201
        else:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return responseObject, 401

 """
def generate_user(session, json_data):
    '''
    func to create a user
    :param session:
    :param json_data: its a data from the front end
    :return:
    '''
    user = session.query(User).filter(User.email == json_data['email']).first()
    if not user:
        role = fetch_role(session, json_data['role'])
        print(get_role_schema(session,json_data['role']))
        user = User(json_data["name"], json_data["email"], json_data["password"], json_data["creationDate"], role)
        session.add(user)
        session.commit()
        responseObject = {
            'status': 'success',
            'message': 'Successfully registered.'}
    else:
        responseObject = {
            'status': 'failed',
            'message': 'User already registered.'}
    return responseObject

def auth(session, json_data, secrete_key):
    '''

    :param session:
    :param json_data:
    :param secrete_key:
    :return:
    '''
    user = session.query(User).filter(User.email == json_data['email']).first()
    #print(user[0])
    if user and check_password_hash(user.password,  json_data['password']):
        auth_token = encode_auth_token(user.role.name, secrete_key)
        schema = UserSchema()
        user_auth = schema.dump(user).data
        user_auth["token"] = auth_token
        return user_auth
    else:
        return { 
            'code': 401,
            'message': 'login or password invalid. Please try again.'
        }

def fetch_users(session):
    '''
    get all users from tables
    :param session:
    :return
    '''
    return session.query(User).all()

def delete_user(session, id):
    delete_user = session.query(User).filter(User.id == id).first()
    session.delete(delete_user)
    session.commit()

def delete_users(session):
    delete_users = session.query(User).delete(synchronize_session=False)
    session.commit()

def edit_user(session, user_data):
    print(user_data)
    # user = User(user_data["name"], user_data["email"], user_data["password"] , user_data["creationDate"])
    a = session.query(User).filter(User.email == user_data['email']). \
        update({User.name: user_data["name"]}, synchronize_session=False)
    session.commit()
    print(a)
    responseObject = {
        'status': 'success',
        'message': 'Successfully registered.'}
    return responseObject
