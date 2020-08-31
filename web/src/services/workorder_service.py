"""

"""
from src.mappers import device_mapper
from src.services import vpn_service, om_corp_service, internet_service, voip_service, hostname_service
from src.commons.utils import excel_manager, file_manager, util
from src.controllers import device_controller
from src.repositories import entity
import sys
from src.commons.utils.file_manager import create_workorder_file

sys.path.append("..")


def generate_workorder_file(workorder_to_save, session):
    services = []
    work_order_name = workorder_to_save["name"]
    client_code = workorder_to_save["client"]["code"]
    template_type = workorder_to_save["templateType"]
    vendor = workorder_to_save["vendor"]
    error_creat = ""
    workorder_final = ""
    creat_bol_templ = False
    clients_services, services = excel_manager.fetch_client_services(
        client_code)

    if clients_services:
        hostname = clients_services[0]["hostname"].split(".")[0]
        # test the router or hostname
        if hostname:
            hostname = device_mapper.validate_hostname(hostname)
            device_devices = device_controller.get_device_schema(
                session, hostname)
            if device_devices:
                creat_bol_templ, output = hostname_service.generate_workorder_hostname(
                    device_devices)
                workorder_final += output
            for client_attribute in clients_services:

                if device_devices:
                    protocol_type = client_attribute["protocol_type"]
                    service_type = client_attribute["service"]
                    # we will returned
                    if service_type == "OM_Corporate" and template_type == "Normal" and vendor == "NOKIA":
                        creat_bol_templ, output = om_corp_service.generate_workorder_om_corp(
                            client_attribute, protocol_type, device_devices)
                        if creat_bol_templ:
                            workorder_final += output + "\n"
                        else:
                            error_creat = output
                            break
                    if service_type == "VPN MPLS" and template_type == "Normal" and vendor == "NOKIA":
                        creat_bol_templ, output = vpn_service.generate_workorder_vpn(
                            client_attribute, protocol_type, device_devices)
                        if creat_bol_templ:
                            workorder_final += output + "\n"
                        else:
                            error_creat = output
                            break
                    if service_type == "Internet" and template_type == "Normal" and vendor == "NOKIA":
                        creat_bol_templ, output = internet_service.generate_workorder_internet(
                            client_attribute, protocol_type, device_devices)
                        if creat_bol_templ:
                            workorder_final += output + "\n"
                        else:
                            error_creat = output
                            break

                    if service_type == "Trunk SIP" and template_type == "Normal" and vendor == "NOKIA":
                        creat_bol_templ, output = voip_service.generate_workorder_voip(
                            client_attribute, protocol_type, device_devices)
                        if creat_bol_templ:
                            workorder_final += output + "\n"
                        else:
                            error_creat = output
                            break

                    if service_type == "VPLS_MH":
                        pass
                else:
                    return False, "The device" + hostname+" is not found in list device.", services, clients_services[0]["client"]
            creat_bol_templ = True
            if creat_bol_templ:
                work_order_name = work_order_name + ".txt"
                workorder_file_name = util.get_path_workorder(work_order_name)
                file_manager.create_workorder_file(
                    workorder_file_name, workorder_final)
                return True, "your workorder is created successfully. You can download it now", services, clients_services[0]["client"]
            else:
                return False, error_creat

        else:
            return False, "router is not found in Timos, please check your parameters", services, clients_services[0]["client"]

    else:
        return False, "client is not found in Timos, please check your parameters", services, ""
# pour test session apres on va deleter
# session = entity.Session()
#
# generate_workorder_file({'name': 'WO_BAR_8678@SUPPORT_IP', 'client': {'name': None, 'code': 'BAR_8678'}, 'creationDate': '2019-11-07T08:42:48.382Z', 'templateType': 'Normal', 'vendor': 'NOKIA'}
# , session)
