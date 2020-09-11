from flask import (
    Flask, request, jsonify, send_file, send_from_directory,
    safe_join, Response
)
from flask_jwt_extended import jwt_required, get_jwt_identity, get_raw_jwt
from cron_descriptor import get_description
from werkzeug.utils import secure_filename
import os
import datetime
import platform

from config import Config, convert_to_windows_path
from src.repositories.entity import Session, Base
from src.repositories import cronjob_repository, script_repository
from src.services import cronjob_service, script_service
from src.commons.utils import get_folder_tree, file_manager
from src.controllers import cron_job_controller, script_controller
from src.routes.jwt_auth import admin_required
from src import app

# ------- CronJOb Routes ---------
# --------------------------------


@app.route('/cron-jobs/<page>/<size>', methods=['GET'])
@jwt_required
def get_cron_jobs(page, size):
    session = Session()
    cronjobs_json = cron_job_controller.get_cron_jobs_schema(
        session,
        page,
        size
    )
    session.close()
    return jsonify(cronjobs_json)


@app.route('/generate-cron-job', methods=['POST'])
@jwt_required
def generate_cron_job():
    session = Session()
    cronjob_from_request = request.get_json()
    print("cronjob_from_request: ", cronjob_from_request)
    # try:
    # The cronjob is only added and is not committed until it runs
    # successfully; in case of an error: session.rollback()
    cron_job,  message, response = cronjob_repository.generate_cron_job(
        session, cronjob_from_request, 'Pending', datetime.datetime.now()
    )
    if (response):
        status = cronjob_service.add_cron_job(
            cronjob_from_request,
            cron_job
        )
        session.commit()
        session.close()
    else:
        status = "Error"
        session.rollback()
        message = 'schedule failed'

    return jsonify(cronjob_from_request, status, response, message), 201



@app.route('/convert-cron-job', methods=['POST'])
@jwt_required
def convert_cron_job():
    cronjob_from_request = request.get_json()
    cronjob_to_convert = cronjob_from_request['expression']
    print("cronjob_to_convert", cronjob_to_convert)
    try:
        converted = get_description(cronjob_to_convert)
        return jsonify(converted_cron_job=converted, status="ok")
    except Exception:
        return jsonify(converted_cron_job="", status="error")


@app.route('/activate-cronjob/<id>', methods=['GET'])
def activate_cronjob(id):
    print(id, 'this cronjob was activated')
    try:
        cronjob_service.activate_cron_job()
    except:
        pass
    return jsonify(id=id, msg='this cronjob was activated')


@app.route('/stop-cronjob/<id>', methods=['GET'])
def stop_cronjob(id):
    print(id, 'this cronjob was stopped')
    return jsonify(id=id, msg='this cronjob was stopped')


# ------- Script Routes ---------
# -------------------------------

@app.route('/get-scripts/<scriptType>/<page>/<size>', methods=['GET'])
@jwt_required
def get_scripts(scriptType, page, size):
    session = Session()
    scripts = script_controller.get_scripts_schema(
        session,
        scriptType,
        page,
        size)
    session.close()
    return jsonify(scripts)


@app.route('/get-script-names', methods=['POST'])
@jwt_required
def get_script_names():
    path = Config.SCRIPTS_PATH + request.get_json()['path']
    return jsonify(file_manager.get_file_names_util(path))


@app.route('/generate-script', methods=['POST'])
@jwt_required
def generate_script():
    session = Session()
    script = request.get_json()
    # try:
    status, report, log = script_service.run_script(script)
    script_repository.generate_script(script, status, report, log, session)
    session.close()
    return jsonify(status=status, report=report)
    # except:
    # return jsonify(status='error', report="An error occurred while trying
    # to execute the script")


@app.route('/run-script', methods=['POST'])
@jwt_required
def run_script():
    session = Session()
    script = request.get_json()
    status, report, log = script_service.run_script(script)
    if status != script["status"] or report != script["report"] or log!=script["log"]:
        edited_script = script_controller.edit_script_schema(
            script, session, status, report, log
        )
        changed = "Changed"
    else:
        edited_script = {}
        changed = "Not changed"
    session.close()
    return jsonify(
        edited_script=edited_script,
        response=changed,
        status=status
    )


@app.route('/get-script-tree-arch', methods=['GET'])
@jwt_required
def get_tree_arch():
    return file_manager.get_tree(Config.SCRIPTS_PATH)


@app.route('/edit-script-folder', methods=['POST'])
@jwt_required
def edit_folder():
    script_path = safe_join(Config.SCRIPTS_PATH, request.get_json()['path'])
    output_pdf_path = safe_join(
        Config.OUTPUT_PDF_PATH, request.get_json()['path'])
    output_excel_path = safe_join(
        Config.OUTPUT_EXCEL_PATH, request.get_json()['path'])
    email_template_path = safe_join(
        Config.EMAIL_HTML_TEMPLATE_PATH, request.get_json()['path'])
    path = []
    path.append(script_path)
    path.append(output_pdf_path)
    path.append(output_excel_path)
    path.append(email_template_path)
    print("path ", request.get_json()['path'])
    name = request.get_json()['name']
    if (request.get_json()['action'] == 'add'):
        response = script_service.add_folder(path, name)
    elif (request.get_json()['action'] == 'delete'):
        response = script_service.delete_folder(path, name)
    return jsonify(
        action=request.get_json()['action'],
        response=response, path='Scripts/'+request.get_json()['path'],
        name=name
    )


@app.route('/upload-script/<path>', methods=['POST'])
@jwt_required
def upload_script(path):
    try:
        profile = request.files['uploadFile']
        print("profile", profile)
        try:
            if platform.system() == 'windows':
                savePath = path.replace('_', '\\')
            else:
                savePath = path.replace('_', '/')

            profile.save(os.path.join(
                Config.SCRIPTS_PATH + savePath,
                secure_filename(profile.filename))
            )
            return jsonify(response='File uploaded successfully')
        except Exception:
            profile.save(os.path.join(
                Config.SCRIPTS_PATH,
                secure_filename(profile.filename))
            )
            return jsonify(response='File uploaded in the root directory')
    except KeyError:
        return jsonify(response='Bad Request Error')


@app.route('/upload-template/<path>', methods=['POST'])
@jwt_required
def upload_template(path):
    try:
        profile = request.files['uploadFile']
        print("profile", profile)
        try:
            if platform.system() == 'windows':
                savePath = path.replace('_', '\\')
            else:
                savePath = path.replace('_', '/')

            profile.save(os.path.join(
                Config.EMAIL_HTML_TEMPLATE_PATH + savePath,
                secure_filename(profile.filename))
            )
            return jsonify(response='File uploaded successfully')
        except Exception as e:
            print(str(e))
            profile.save(os.path.join(
                Config.EMAIL_HTML_TEMPLATE_PATH,
                secure_filename(profile.filename))
            )
            return jsonify(response='File uploaded in the root directory')
    except KeyError:
        return jsonify(response='Bad Request Error')


@app.route('/view-pdf', methods=['POST', 'GET'])
def view_pdf():
    if request.method == 'POST':
        try:
            filename = request.get_json()['filename']
            pdf_path = Config.PDF_PATH
            safe_path = safe_join(pdf_path, filename)
            return send_file(
                safe_path,
                as_attachment=False
            )
        except FileNotFoundError:
            return "File not found"
        except Exception as exp:
            return str(exp)
    else:
        try:
            safe_path = safe_join(Config.PDF_PATH, 'pdf-test.pdf')
            return send_file(
                safe_path,
                as_attachment=False
            )
        except FileNotFoundError:
            return "File not found"
        except Exception as exp:
            return str(exp)


@app.route('/view-pdf-file/<filepath>', methods=['GET'])
def view_pdf_file(filepath):
    try:
        if platform.system() == 'windows':
            savePath = filepath.replace('+', '\\')
        else:
            print('yes')
            savePath = filepath.replace('+', '/')
        pdf_path = Config.OUTPUT_PDF_PATH
        print('savepath', savePath)
        safe_path = safe_join(pdf_path, savePath)
        print(safe_path)
        return send_file(
            safe_path,
            as_attachment=False
        )
        return 'true'
    except FileNotFoundError:
        print('filenotfound')
        return "File not found"
    except Exception as exp:
        print(str(exp))
        return str(exp)


# example http://172.22.114.45/api/display-file/path&/home/user/file.txt
@app.route('/get-file/<path:file_path>', methods=['GET'])
def display_file(file_path):
    print(file_path)
    thispath = file_path.split('&')[1]
    command = "".join(['cat ', '"', thispath, '"'])
    stream = os.popen(command)
    stream.seek(0)
    file_content = stream.read()
    json_object = dict(path=thispath, file_content=file_content) 
    return jsonify(path=thispath, file=file_content) 
