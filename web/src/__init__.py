
from flask_cors import CORS
from flask import Flask
from src.repositories.entity import init_db, shutdown_db_session
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SECRET_KEY'] = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"

jwt = JWTManager(app)

CORS(app)

init_db()

""" @app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_db_session() """


from src.routes import b2b_routes, radio_routes, audit_routes
import src.entities

#from src.repositories.entity import init_db

#init_db()
