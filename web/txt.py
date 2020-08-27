from flask import Flask, request, jsonify, send_file,send_from_directory
from flask_cors import CORS
from src.repositories.entity import Session, init_db

# yalzam nraj3ou
from src.services import workorder_service
from src.controllers import work_order_controller, device_controller
from src.repositories import workorder_repository, device_repository, user_repository

app = Flask(__name__)
CORS(app)
#init_db()
#app.config['SECRET_KEY'] = "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0"

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/work-orders/<page>/<size>", methods=['GET'])
def get_work_orders(page, size):
    session = Session()
    workorders_json = work_order_controller.get_work_orders_schema(session, page, size)
    session.close()
    return jsonify(workorders_json)


@app.route("/work-order-detail/<id>", methods=['GET'])
def fetch_work_order_detail(id):
    workorder_to_fetch = id
    session = Session()
    fetched_workorder = work_order_controller.fetch_work_orders_schema(session, workorder_to_fetch)
    session.close()
    print(fetched_workorder)
    return jsonify(fetched_workorder)


@app.route("/delete-work-order/<id>", methods=['DELETE'])
def delete_work_order(id):
    # workorder_to_delete = request.get_json()
    # print(workorder_to_delete)
    print(id)
    session = Session()
    work_order_controller.delete_work_orders_schema(session, id)
    session.close()
    return jsonify(True)


@app.route('/generate-work-order', methods=['POST'])
def generate_workorder():
    session = Session()
    workorder_to_save = request.get_json()
    print(workorder_to_save)
    bol, message, services, workorder_to_save["client"]["name"] = workorder_service.generate_workorder_file(workorder_to_save, session)
    print(bol, message, services, workorder_to_save["client"]["name"])
    if bol:
        workorder_repository.generate_work_order(session, workorder_to_save, services)
    session.close()
    return jsonify(workorder_to_save, bol, message)


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    # uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
    try:
        return send_from_directory(directory='./ressources/work_order_folder/work_order_b2b/', filename= filename)
    except:
        return "file not found"

@app.route('/generate-device', methods=['POST'])
def generate_device():
    session = Session()
    device_to_save = request.get_json()
    print(device_to_save)
    if device_to_save:
        message, error = device_repository.generate_device(session, device_to_save)
        session.close()
        print(message, error)
        return jsonify(message, error)

@app.route("/devices/<page>/<size>", methods=['GET'])
def get_devices(page, size):
    session = Session()
    devices_json = device_controller.get_devices_schema(session, page, size)
    print(devices_json)
    session.close()
    return jsonify(devices_json)
@app.route("/devices/", methods=['GET'])
def get_all_devices():
    session = Session()
    devices_json = device_controller.get_all_devices_schema(session)
    session.close()
    return jsonify(devices_json)


@app.route('/upload-devices', methods=['POST'])
def upload_devices():
    session = Session()
    devices = request.get_json()
    print(devices)
    del devices[0]
    if devices:
        device_repository.upload_devices(session, devices)
        session.close()

        return jsonify("The devices uploaded succesfully", 200)
    else:
        return jsonify("The excel File is empty please check your parameters", 199)

#

@app.route('/register', methods=['POST'])
def register():
    session = Session()
    json_data = request.json
    print(json_data)
    secrete_key = app.config['SECRET_KEY']
    # check if user already exists
    user =  user_repository.check_user(session, json_data)
    if not user:
        user_repository.generate_user(session, json_data)
        session.close()
    return jsonify({"yes"})

from src.entities.user import User

@app.route('/login', methods=['POST'])
def login():
    session = Session()
    secrete_key = app.config['SECRET_KEY']
    json_data = request.get_json()
    status, code = user_repository.check_user(session, json_data, secrete_key)
    session.close()
    print(status)
    return jsonify({'status': status, code: code})



'''
@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})

def encode_auth_token(self, user_id):

    Generates the Auth Token
    :return: string

    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
            'iat': datetime.datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e
@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'status': True})
    else:
        return jsonify({'status': False})
'''

if __name__ == '__main__':
    # debug = True : to restart automatically if there   is any changes
    app.run(debug=True)
