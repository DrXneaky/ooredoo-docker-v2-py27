from flask import (
    Flask, request, jsonify, send_file, send_from_directory, Response)
from sqlalchemy.exc import IntegrityError
import sys
import os
import requests
# import urllib.request
from src.services import workorder_service
from src.controllers import (
    work_order_controller, device_controller, role_controller, user_controller)
from src.repositories import (
    workorder_repository, device_repository, user_repository, role_repository)
from src.repositories.entity import Session, Base
from src.entities.device import Device
from src.entities.user import User
from src import app, jwt

from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity,
    get_raw_jwt)
from config import Config
from src.routes.jwt_auth import admin_required
from src.repositories.entity import init_db

# sys.path.append("/home/miladi/ooredoo-docker/web")


@app.route("/")
def hello():
    init_db()
    return "Hello World!"


@app.route("/work-orders/<page>/<size>", methods=['GET'])
@jwt_required
def get_work_orders(page, size):
    init_db()
    session = Session()
    workorders_json = work_order_controller.get_work_orders_schema(
        session, page, size)
    session.close()
    return jsonify(workorders_json)


@app.route("/work-order-detail/<id>", methods=['GET'])
@jwt_required
def fetch_work_order_detail(id):
    workorder_to_fetch = id
    session = Session()
    fetched_workorder = work_order_controller.fetch_work_orders_schema(
        session, workorder_to_fetch)
    session.close()
    print(fetched_workorder)
    return jsonify(fetched_workorder)


@app.route("/delete-work-order/<id>", methods=['DELETE'])
@jwt_required
def delete_work_order(id):
    # workorder_to_delete = request.get_json()
    # print(workorder_to_delete)
    print(id)
    session = Session()
    work_order_controller.delete_work_orders_schema(session, id)
    session.close()
    return jsonify(True)


@app.route('/generate-work-order', methods=['POST'])
@jwt_required
def generate_workorder():

    session = Session()
    workorder_to_save = request.get_json()
    print("workorder to save ", workorder_to_save)
    bol, message, services, workorder_to_save[
        "client"]["name"] = workorder_service.generate_workorder_file(
        workorder_to_save,
        session
    )
    if bol:
        workorder_repository.generate_work_order(
            session,
            workorder_to_save,
            services
        )
    session.close()
    return jsonify(workorder_to_save, bol, message), 201


@app.route('/download/<filename>', methods=['GET'])
@jwt_required
def download(filename):
    print("this file is "+filename)
    # uploads = os.path.join(
    # current_app.root_path, app.config['UPLOAD_FOLDER'])
    try:
        return send_from_directory(
            directory=Config.WORK_ORDER_DIRECTORY,
            filename=filename
        )
    except Exception:
        return "this file if not found"


# edit workorder put request
@app.route('/edit-work-order/<id>', methods=['PUT'])
@jwt_required
def edit_workorder(id):
    session = Session()
    workorder_changes = request.get_json()
    print(workorder_changes["client"]["code"])
    # changing the schema of that specific workorder in the database
    # work_order_controller.edit_work_order_schema(
    # session, id, workorder_changes)
    session.close()
    return jsonify(workorder_changes)


@app.route('/generate-device', methods=['POST'])
@jwt_required
def generate_device():
    session = Session()
    device_to_save = request.get_json()
    if device_to_save:
        message, error = device_repository.generate_device(
            session,
            device_to_save
        )
        session.close()
        return jsonify(message, error)


@app.route('/get-devices-from-type/<devicetype>', methods=['GET'])
@jwt_required
def get_devices_from_type(devicetype):
    session = Session()
    devices_json = device_controller.get_devices_schema_from_type(
        session,
        devicetype
    )
    session.close()
    return jsonify(devices_json)


@app.route("/devices/<page>/<size>", methods=['GET'])
@jwt_required
def get_devices(page, size):
    session = Session()
    devices_json = device_controller.get_devices_schema(session, page, size)
    # print(devices_json)
    session.close()
    return jsonify(devices_json)


@app.route("/devices/", methods=['GET'])
@jwt_required
def get_all_devices():
    session = Session()
    devices_json = device_controller.get_all_devices_schema(session)
    session.close()
    return jsonify(devices_json)


@app.route('/upload-devices', methods=['POST'])
@jwt_required
def upload_devices():
    session = Session()
    devices = request.get_json()
    print(devices)
    del devices[0]
    if devices:
        device_repository.upload_devices(session, devices)
        session.close()

        return jsonify(
            "The devices uploaded succesfully",
            200
        )
    else:
        return jsonify(
            "The excel File is empty please check your parameters",
            199
        )


@app.route('/edit-device', methods=['POST'])
@jwt_required
def edit_device():
    return jsonify(status='done')


@app.route('/delete-device', methods=['POST'])
@jwt_required
def delete_device():
    try:
        device = request.get_json()
        session = Session()
        print(device['hostname'])
        status = device_repository.delete_device(session, device['hostname'])
        session.close()
        return jsonify(status=status, device=device['hostname'])
    except IntegrityError:
        return jsonify(status="integrityError", device=device['hostname'])


@app.route('/register', methods=['POST'])
@jwt_required
@admin_required
def register():
    session = Session()
    json_data = request.json
    print(json_data)
    user = user_repository.generate_user(
        session,
        json_data
    )
    session.close()
    return jsonify(user)


@app.route("/users", methods=['GET'])
@jwt_required
@admin_required
def get_users():
    session = Session()
    users_json = user_controller.get_user_schema(session)
    session.close()
    return jsonify(users_json)


@app.route("/delete-user/<id>", methods=['DELETE'])
@jwt_required
@admin_required
def delete_user(id):
    print(id)
    session = Session()
    user_controller.delete_user_schema(
        session,
        id
    )
    session.close()
    return jsonify(True)


@app.route("/edit-user", methods=['PUT'])
@jwt_required
@admin_required
def edit_user():
    session = Session()
    user_data = request.json
    print(user_data)
    response_object = user_repository.edit_user(
        session,
        user_data
    )
    session.close()
    return jsonify(response_object)


@app.route("/delete-users", methods=['DELETE'])
@jwt_required
@admin_required
def delete_users():
    session = Session()
    user_controller.delete_users_schema(session)
    session.close()
    return jsonify(True)


@app.route('/login', methods=['POST'])
def login():
    session = Session()
    secrete_key = Config.SECRET_KEY
    json_data = request.get_json()
    # status, code = user_repository.check_user(
    # session, json_data, secrete_key)
    auth = user_repository.auth(session, json_data, secrete_key)
    session.close()
    # print(status)
    # return jsonify({'status': status, code: code})
    return jsonify(auth)


@app.route('/register_role', methods=['POST'])
@jwt_required
@admin_required
def register_role():
    session = Session()
    json_data = request.json
    role = role_repository.generate_role(session, json_data)
    session.close()
    return jsonify(role)


@app.route('/get_roles', methods=["GET"])
@jwt_required
@admin_required
def get_roles():
    session = Session()
    roles_json = role_controller.get_roles_schema(session)
    session.close()
    return jsonify(roles_json)


@app.route("/delete-role/<id>", methods=['DELETE'])
@jwt_required
@admin_required
def delete_role(id):
    session = Session()
    role_controller.delete_role_schema(session, id)
    session.close()
    return jsonify(True)
