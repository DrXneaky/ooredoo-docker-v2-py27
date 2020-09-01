
from src.entities.device import DeviceSchema
from src.repositories.device_repository import fetch_device, get_devices, fetch_devices, fetch_devices_from_type,fetch_devices_from_hostnamelist
import json

def get_device_schema(session, device_to_fetch):
    schema = DeviceSchema(many=True)
    device= fetch_device(session, device_to_fetch)
    device_devices = schema.dump(fetch_device(session, device_to_fetch))
    return device_devices.data
    # ip_system = schema.dump(device.data)

def get_devices_schema(session, page, size):
    schema = DeviceSchema(many=True)
    # page = schema.dumps(get_work_orders(session, page, size))
    page = get_devices(session, page, size)
    page.items = schema.dump(page.items)
    return page.__dict__

def get_all_devices_schema(session):
    schema = DeviceSchema(many=True)
    devices= fetch_devices(session)
    device_devices = schema.dump(devices)
    return device_devices.data

def get_devices_schema_from_type(session, devicetype):
    schema = DeviceSchema(many=True)
    devices = fetch_devices_from_type(session, devicetype)
    devices_json = schema.dump(devices)
    return devices_json.data

def get_devices_schema_from_hostnamelist(session, hostnamelist):
    schema = DeviceSchema(many=True)
    try:
        if (type(hostnamelist[0])==str):
            devices = fetch_devices_from_hostnamelist(session, hostnamelist)
        else:
            hostnamelist = [device['hostname'] for device in hostnamelist]
            devices = fetch_devices_from_hostnamelist(session, hostnamelist)
    except Exception as e:
        print(str(e))
    devices_json = schema.dump(devices)
    return devices_json.data