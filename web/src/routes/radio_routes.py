from flask import Flask, request, jsonify, send_file, send_from_directory, Response

from src.services import workorder_radio_service
from src.controllers import work_order_radio_controller
from src.repositories import workorder_radio_repository
import sys
import os
import requests
#import urllib.request
from src.repositories.entity import Session, Base
from src.entities.device import Device
from src import app

from flask_jwt_extended import jwt_required, get_jwt_identity,get_raw_jwt
from src.routes.jwt_auth import admin_required
# sys.path.append("/home/miladi/ooredoo-docker/web")



@app.route("/work-orders-radio/<page>/<size>", methods=['GET'])
@jwt_required
def get_work_orders_radio(page, size):
    session = Session()
    workorders_json = work_order_radio_controller.get_work_orders_schema(
        session, page, size)
    session.close()
    return jsonify(workorders_json)


@app.route("/work-order-radio-detail/<id>", methods=['GET'])
@jwt_required
def fetch_work_order_radio_detail(id):
    workorder_to_fetch = id
    session = Session()
    fetched_workorder = work_order_radio_controller.fetch_work_orders_schema(
        session, workorder_to_fetch)
    session.close()
    print(fetched_workorder)
    return jsonify(fetched_workorder)


@app.route("/delete-work-order-radio/<id>", methods=['DELETE'])
@jwt_required
def delete_work_order_radio(id):
    # workorder_to_delete = request.get_json()
    # print(workorder_to_delete)
    print(id)
    session = Session()
    work_order_radio_controller.delete_work_orders_schema(session, id)
    session.close()
    return jsonify(True)


@app.route('/generate-work-order-radio', methods=['POST'])
@jwt_required
def generate_workorder_radio():

    session = Session()
    workorder_to_save = request.get_json()
    print("workorder to save ", workorder_to_save)
    bol, message, services, workorder_to_save["client"]["name"] = workorder_radio_service.generate_workorder_file(
        workorder_to_save, session)
    if bol:
        workorder__radio_repository.generate_work_order(
            session, workorder_to_save, services)
    session.close()
    return jsonify(workorder_to_save, bol, message), 201


@app.route('/download-radio/<filename>', methods=['GET'])
@jwt_required
def download_radio(filename):
    print("this file is "+filename)
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    try:
        print("this file is "+filename)
        return send_from_directory(directory='./ressources/work_order_folder/work_order_radio/', filename=filename)
    except:
        return "this file if not found"

# edit workorder put request
@app.route('/edit-work-order-radio/<id>', methods=['PUT'])
@jwt_required
def edit_workorder_radio(id):
    session = Session()
    workorder_changes = request.get_json()
    print(workorder_changes["client"]["code"])
    # changing the schema of that specific workorder in the database
    # work_order_controller.edit_work_order_schema(session, id, workorder_changes)
    session.close()

    return jsonify(workorder_changes)
