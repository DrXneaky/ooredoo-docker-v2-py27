
from src.commons.utils import util, network_validator
from src.controllers import template_controller
from src.mappers import network_mapper
from src.repositories import device_connector


def generate_workorder_voip(client_attribute, protocol_type, device_devices):
    output_static = ""
    client_attribute["serviceid"] = "5101"
    template_path = util.get_template_path()
    subnet_existance_bol = False
    subnet_voip_pba = network_mapper.convert_subnet(client_attribute["voip_ip_pba"])
    client_attribute["qos_ingress"] = util.create_qos(client_attribute["qos"])
    try:
        net_connect = device_connector.Connection(device_devices[0]["ip_system"]).connect_to_nokia_device()

        vlan_existance_bol = network_validator.check_vlan_existance(net_connect, client_attribute["port"], client_attribute["voip_vlan"])
        service_existance_bol = network_validator.check_service_existance(client_attribute["serviceid"], net_connect)
        if service_existance_bol:
            subnet_existance_bol = network_validator.check_address_existance(client_attribute["serviceid"], net_connect,subnet_voip_pba)
        device_connector.Connection(device_devices[0]["ip_system"]).disconnect_to_nokia_device(net_connect)
        vlan_existance_bol, subnet_existance_bol =False, False
        if vlan_existance_bol:
            return False, "The vlan of voip service " + client_attribute["voip_vlan"] +"is already used."
        elif subnet_existance_bol:
            return False, "The subnet of voip service " + subnet_voip_pba +" is already used."
        else:
            if str(protocol_type).find("OSPF") != -1:
                template_name = "template_trunk_sip_ospf.txt"
                output_ospf = template_controller.tempalte_generator_service(template_name, template_path,
                                                                          service_existance_bol, device_devices,
                                                                          client_attribute)
                return True, output_ospf
            else:
                template_name = "template_trunk_sip_static.txt"
                output_static = template_controller.tempalte_generator_service(template_name, template_path,
                                                                              service_existance_bol, device_devices,
                                                                              client_attribute)
                return True, output_static
        # test
        return True, output_static
    except:
        return False, "Cannot connect to BB IPMPLS, please check the connection to local network of ooredoo "