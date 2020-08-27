
from src.commons.utils import util, network_validator
from src.controllers import template_controller
from src.mappers import network_mapper
from src.repositories import device_connector

def generate_workorder_internet(client_attribute, protocol_type, device_devices):
    public_bol =[]
    output = ""
    subnet_existance_bol = False
    client_attribute["serviceid"] = "9500"
    template_path = util.get_template_path()
    client_attribute["ip_hsi_cpe"] = client_attribute["ip_hsi_cpe"].split("/")[0]
    subnet_hsi_pba = network_mapper.convert_subnet(client_attribute["hsi_ip_pba"])
    client_attribute["qos_ingress"] = util.create_qos(client_attribute["qos"])
    try:
        net_connect = device_connector.Connection(device_devices[0]["ip_system"]).connect_to_nokia_device()
        qos_existance_bol = network_validator.check_qos_existance(net_connect, client_attribute["qos_ingress"])
        # will be delleted
        qos_existance_bol = False
        if qos_existance_bol:
            pass
        else:
            template_name = "template_qos.txt"
            output_qos = template_controller.tempalte_generator_qos(template_name, template_path, client_attribute)
            output += output_qos +"\n"

        vlan_existance_bol = network_validator.check_vlan_existance(net_connect, client_attribute["port"], client_attribute["hsi_vlan"])
        service_existance_bol = network_validator.check_service_existance(client_attribute["serviceid"], net_connect)
        if service_existance_bol:
            subnet_existance_bol = network_validator.check_address_existance_hsi(client_attribute["serviceid"], net_connect, subnet_hsi_pba)
            for publicip in client_attribute["public_ip"]:
                subnet_pub_existance_bol =network_validator.check_address_existance_hsi(client_attribute["serviceid"], net_connect, publicip)
                public_bol.append(subnet_pub_existance_bol)
        # a testet existance subnet publicpublic_bolvvvvvvvv
        device_connector.Connection(device_devices[0]["ip_system"]).disconnect_to_nokia_device(net_connect)
        vlan_existance_bol, subnet_existance_bol = False, False
        if vlan_existance_bol:
            return False, "The vlan of internet service " + client_attribute["hsi_vlan"] +" is already used in BB IP MPLS."
        elif subnet_existance_bol:
            return False, "The subnet of internet service " + subnet_hsi_pba +" is already used in BB IP MPLS."
        elif public_bol:
            return False, "The subnet public is already used in BB IP MPLS"
        else:
            if str(protocol_type).find("OSPF") != -1:
                template_name = "template_hsi_ospf.txt"
            else:
                template_name = "template_hsi_static.txt"
            output_service= template_controller.tempalte_generator_service(template_name, template_path,
                                                                      service_existance_bol, device_devices,
                                                                      client_attribute)
            output += output_service +"\n"
            print(output)
            return True, output
    except:
        return False, "Cannot connect to BB IPMPLS, please check the connection to local network of ooredoo "
    # test
    # return True, output