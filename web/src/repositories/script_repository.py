from src.entities.script import Script
import datetime
from sqlalchemy_pagination import paginate
from src.controllers import device_controller
from src.repositories import device_repository


def generate_script(script, status, report, session):
  try:
    device_list = script['devices']
  except:
    device_list = []

  #devices_list = device_controller.get_devices_schema_from_hostnamelist(session, device_list)
  devices_list = device_repository.fetch_devices_from_hostnamelist(session, device_list)
  script_to_save = Script (
    script['creationDate'],
    script['scriptName'],
    "",
    script['scriptType'],
    status,
    report,
    devices_list,
  )
  session.add(script_to_save)
  session.commit()

def get_scripts(session, scriptType, page, size):
  pagination = paginate(session.query(Script).order_by(Script.creationDate.desc()).filter(Script.scriptType == scriptType), int(page), int(size))
  return pagination

def edit_script(script, session, status, report):
  script_to_edit = session.query(Script).filter(Script.id == script['id']).first()
  #print ("script_to_edit: ", script_to_edit)
  script_to_edit.status = status
  script_to_edit.report = report
  session.commit()
  return script_to_edit