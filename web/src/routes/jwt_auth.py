from functools import wraps

from flask import Flask, jsonify, request, abort
from flask_jwt_extended import JWTManager, verify_jwt_in_request, create_access_token,get_jwt_claims
from src import app, jwt


def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['role'] != 'admin':
            return jsonify(msg='Admins only!'), 403
        else:
            return fn(*args, **kwargs)
    return wrapper


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity == 'Admin':
        return {'role': 'admin'}
    else:
        return {'role': 'not_admin'}