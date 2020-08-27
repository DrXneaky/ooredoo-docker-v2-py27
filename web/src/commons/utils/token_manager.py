import datetime
import jwt
from flask_jwt_extended import JWTManager, verify_jwt_in_request, create_access_token,get_jwt_claims
def encode_auth_token(user_role,secrete_key):
    """
    Generates the Auth Token
    :return: string
    """
    return create_access_token(identity=user_role, expires_delta = datetime.timedelta(days=1, minutes=0, seconds=0))
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
            'iat': datetime.datetime.utcnow(),
            'iss': user_id
        }
        #print ("secret key: ", secrete_key)
        return jwt.encode(
            payload,
            key=secrete_key,
            algorithm='HS256'
        )
    except Exception as e:
        return e