
from ..entities.device import Device
from sqlalchemy_pagination import paginate
from sqlalchemy.exc import IntegrityError
from ..commons.utils import data_validator


def fetch_device(session, device_to_fetch):
    query_fetch_device = session.query(Device).filter(
        Device.hostname == device_to_fetch)
    fetched_device = query_fetch_device.all()
    return fetched_device


def fetch_devices(session):
    fetched_devices = session.query(Device).all()
    return fetched_devices


def fetch_devices_from_type(session, devicetype):
    return session.query(Device).filter(Device.deviceType == devicetype).all()


def fetch_devices_from_hostnamelist(session, hostnamelist):
    # return []
    return session.query(Device).filter(Device.hostname.in_(hostnamelist)).all()


def generate_device(session, device_to_save):
    if data_validator.validate_ipaddres(device_to_save["ipSystem"]):
        device_to_save["deviceType"] = data_validator.get_device_type(
            device_to_save["ipSystem"])
        device = Device(device_to_save["hostname"], device_to_save["ipSystem"],
                        device_to_save["rd"], device_to_save["vendor"], device_to_save["deviceType"])
        session.add(device)
        try:
            session.commit()
            return "The device "+device_to_save["hostname"] + " is created succefully", 200
        except IntegrityError:
            session.rollback()
            return "The IP address or the hostname is already used. try again!", 199
    return "The IP system is not IPv4 address.", 199


def get_devices(session, page, size):
    pagination = paginate(session.query(Device).order_by(
        Device.hostname.desc()), int(page), int(size))
    return pagination


def upload_devices(session, devices):

    devices_list = [Device(device["hostname"], device["ipSystem"], device["rd"], device["vendor"], 'Router')
                    for device in devices if data_validator.validate_ipaddres(device["ipSystem"])]
    print(devices_list)
    session.add_all(devices_list)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()


def delete_device(session, hostname):
    device_to_delete = session.query(Device).filter(
        Device.hostname == hostname).first()
    print('device_to_delete:', device_to_delete.hostname)
    session.delete(device_to_delete)
    session.commit()
    return 'done'
    # session.commit()
    # error = ""
    # bol = True
    # for device in devices:
    #
    #     print(device)
    #     if device and data_validator.validate_ipaddres(device["ipSystem"]):
    #         devi = Device(device["hostname"], device["ipSystem"], device["rd"], device["vendor"])
    #         session.add(devi)
    #         try:
    #             session.commit()
    #         except IntegrityError:
    #             return False, "repeated ip system or RD"
    #             session.rollback()
    #             # error, there already is a user using this bank address or other
    #             # constraint failed
    #     else:
    #         return False, "data invalid"
