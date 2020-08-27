from src.entities.role import Role


def generate_role(session, json_data):
    '''
    insert role in table  role.
    :param session : object sqlachemy
    :param json_data: json object have parameters of role table
    :return: json object that have true or false
    '''
    role = session.query(Role).filter(Role.name == json_data['name']).first()
    print(role)
    if not role:
        role = Role(json_data["name"], json_data["description"])
        session.add(role)
        session.commit()
        responseObject = {
            'status': 'success',
            'message': 'Successfully registered.'}
    else:
        responseObject = {
            'status': 'failed',
            'message': 'Role already registered.'}
    return responseObject


def fetch_roles(session):
    '''
    fetch roles from table role
    :param session: object sqlachemy
    :return: object non serialiseable
    '''
    all_roles = session.query(Role).all()
    return all_roles

def _roles(session):
    '''
    fetch roles from table role
    :param session: object sqlachemy
    :return: object non serialiseable
    '''
    all_roles = session.query(Role).all()
    return all_roles

def delete_role(session, id):
    print(id)
    delete_role = session.query(Role).filter(Role.id == id).first()
    session.delete(delete_role)
    session.commit()
    print(delete_role)


def fetch_role(session, role_name):
    return session.query(Role).filter(Role.name == role_name).first()