
from src.commons.utils import util, network_validator
from src.controllers import template_controller
from src.mappers import network_mapper
from src.repositories import device_connector


def generate_workorder_om_corp(client_attribute, protocol_type, device_devices):
    output= ""
    client_attribute["serviceid"] = "5101"
    template_path = util.get_template_path()
    subnet_existance_bol = False
    client_attribute["om_ip_cpe"] = client_attribute["om_ip_cpe"].split("/")[0]
    subnet_om_corp_pba = network_mapper.convert_subnet(client_attribute["om_ip_pba"])
    client_attribute["qos_ingress"] = util.create_qos(client_attribute["qos"])
    try:
        # will be commented temporary because we're not connect to local network.(2 below lines)
        # net_connect = device_connector.Connection(device_devices[0]["ip_system"]).connect_to_nokia_device()
        # qos_existance_bol = network_validator.check_qos_existance(net_connect, client_attribute["qos_ingress"])
        # will be delleted
        qos_existance_bol = False
        if qos_existance_bol ==False:
            template_name = "template_qos.txt"
            output_qos = template_controller.tempalte_generator_qos(template_name, template_path, client_attribute)
            output += output_qos + "\n"
        ###########will be commented temporary because we're not connect to local network.(2 below lines)
        # vlan_existance_bol = network_validator.check_vlan_existance(net_connect, client_attribute["port"], client_attribute["om_vlan"])
        # service_existance_bol = network_validator.check_service_existance(client_attribute["serviceid"], net_connect)
        service_existance_bol = True
        ########### will be commented temporary because we're not connect to local network.(3 below lines)
        # if service_existance_bol:
        #     subnet_existance_bol = network_validator.check_address_existance(client_attribute["serviceid"], net_connect,subnet_om_corp_pba)
        #device_connector.Connection(device_devices[0]["ip_system"]).disconnect_to_nokia_device(net_connect)
        vlan_existance_bol, subnet_existance_bol =False, False
        if vlan_existance_bol:
            return False, "The vlan of OM_corporate service" + client_attribute["om_vlan"] +"is already used."
        elif subnet_existance_bol:
            return False, "The subnet of OM_corporate service" + subnet_om_corp_pba +" is already used."
        else:
            if str(protocol_type).find("OSPF") != -1:
                template_name = "template_om_corp_ospf.txt"
            else:
                template_name = "template_om_corp_static.txt"
            output_service_om = template_controller.tempalte_generator_service(template_name, template_path,service_existance_bol, device_devices,client_attribute)
            output += output_service_om +"\n"
            return True, output
    except:
        return False, "Cannot connect to BB IPMPLS, please check the connection to local network of ooredoo "
