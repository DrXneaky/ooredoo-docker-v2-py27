
from src.commons.utils import network_validator, util
from src.controllers import template_controller
from src.mappers import network_mapper
from src.repositories import device_connector


def _Run_ServiceVPN(VPNServiceInstance, check, Protocol_type, net_connect, Serviceid):
    if Device_type == "Nokia":
        if Protocol_type == "OSPF":
            Intero = IPNetwork(IPpbaVPN).cidr
            Filter_VPN = Policy._filter_VPN(Intero)
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._OSPF_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                      IPpbaVPN, port, vlanVPN, qos_ingress, qos_egress,
                                                                      interface_name, Authentication_Key)
            else:

                VPNService = VPNServiceInstance._OSPF_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                      interface_name, IPpbaVPN, port, vlanVPN,
                                                                      qos_ingress, qos_egress, interface_name,
                                                                      Authentication_Key, VpnDescription)

        else:
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._STATIC_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                        IPpbaVPN, port, vlanVPN, Authentication_Key,
                                                                        routes, IPVPNCpeAdress)
            else:
                VPNService = VPNServiceInstance._STATIC_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                        interface_name, port, vlanVPN,
                                                                        Authentication_Key, routes, IPVPNCpeAdress)

        print(VPNService)

    elif Device_type == "Cisco":
        if Protocol_type == "OSPF":
            Intero = IPNetwork(IPpbaVPN).cidr
            Filter_VPN = Policy._filter_VPN(Intero)
            checkInstance = check._CheckVRFExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._OSPF_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                      IPpbaVPN, port, vlanVPN, qos_ingress, qos_egress,
                                                                      interface_name, Authentication_Key)
            # else:
            #     Serviceid, = Create_New_VRF()
            #     VPNService = VPNServiceInstance._OSPF_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
            #                                                           interface_name, IPpbaVPN, port, vlanVPN,
            #                                                           qos_ingress, qos_egress, interface_name,
            #                                                           Authentication_Key, VpnDescription)

        else:
            checkInstance = check._CheckServiceExistance(Serviceid, net_connect)
            if (checkInstance == "TRUE"):
                VPNService = VPNServiceInstance._STATIC_Old_VPN_Service(Serviceid, interface_name, interface_name,
                                                                        IPpbaVPN, port, vlanVPN, Authentication_Key,
                                                                        routes, IPVPNCpeAdress)
            else:
                VPNService = VPNServiceInstance._STATIC_New_VPN_Service(Serviceid, interface_name, rd, interface_name,
                                                                        interface_name, port, vlanVPN,
                                                                        Authentication_Key, routes, IPVPNCpeAdress)

        print(VPNService)

    return VPNService


def generate_workorder_vpn(client_attribute, protocol_type, device_devices):
    template_path = util.get_template_path()
    subnet_existance_bol = False
    output = ""
    client_attribute["ip_lan_routes"] = client_attribute["routes"].split(";")

    subnet_vpn_pba = network_mapper.convert_subnet(client_attribute["vpn_ip_pba"])
    client_attribute["subnet_vpn_pba"] = subnet_vpn_pba
    client_attribute["qos_ingress"] = util.create_qos(client_attribute["qos"])
    try:
        net_connect = device_connector.Connection(device_devices[0]["ip_system"]).connect_to_nokia_device()
        qos_existance_bol = network_validator.check_qos_existance(net_connect, client_attribute["qos_ingress"])
        from_bgp_toospf_existance_bol = network_validator.check_from_bgp_toospf_existance(net_connect)
        cpm_ospf_existance_bol = network_validator.check_cpm_ospf_existance(net_connect)
        # will be delleted
        qos_existance_bol = False
        if qos_existance_bol ==False:
            template_name = "template_qos.txt"
            output_qos = template_controller.tempalte_generator_qos(template_name, template_path, client_attribute)
            output += output_qos + "\n"
        vlan_existance_bol = network_validator.check_vlan_existance(net_connect, client_attribute["port"],client_attribute["vpn_vlan"])
        service_existance_bol = network_validator.check_service_existance(client_attribute["serviceid"], net_connect)
        if service_existance_bol:
            subnet_existance_bol = network_validator.check_address_existance(client_attribute["serviceid"], net_connect, subnet_vpn_pba)
        # after the verification of the
        device_connector.Connection(device_devices[0]["ip_system"]).disconnect_to_nokia_device(net_connect)
        vlan_existance_bol, subnet_existance_bol = False, False
        if vlan_existance_bol:
            return False, "The vlan of vpn service "+client_attribute["vpn_vlan"]+" is already used."
        elif subnet_existance_bol:
            return False, "The subnet of vpn service "+ subnet_vpn_pba +"is already used."
        else:
            if str(protocol_type).find("OSPF") != -1:
                template_name = "template_vpn_ospf.txt"
            else:
                template_name = "template_vpn_static.txt"
            output_service_vpn = template_controller.tempalte_generator_service_vpn(template_name, template_path, service_existance_bol, device_devices,
                                                                                    client_attribute, from_bgp_toospf_existance_bol, cpm_ospf_existance_bol)
            output +=output_service_vpn + "\n"
            return True, output
    except:
        return False,"please check the connection to local network of ooredoo "