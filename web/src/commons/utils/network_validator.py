"""


"""

def check_service_existance(serviceid, net_connect):
    """
    :param serviceid:
    :param net_connect:
    :return:
    """
    output=net_connect.send_command('show service service-using | match '+ serviceid +' context all')
    service = output.split(" ")
    if serviceid == str(service[0].strip()):
        return True
    else:
        return False


def check_address_existance(serviceid, net_connect,  address):
    output=net_connect.send_command('show router '+ serviceid +' route-table '+ address + ' | match \"No. of Routes:\"')
    if "No. of Routes:0" in output:
        return False
    else:
        return True

def check_address_existance_hsi(serviceid, net_connect, address):
    output = net_connect.send_command('show router route-table ' + address + ' longer')
    if "No. of Routes:0" in output:
        return False
    else:
        return True

def check_vlan_existance(net_connect, port,vlan):
    output = net_connect.send_command('show service sap-using | match '+ port+':'+vlan)
    sap=port+":"+vlan
    if sap in output:
        return True
    else:
        return False

def check_qos_existance(net_connect, qos):
    output = net_connect.send_command('show qos sap-ingress | match ' + str(qos) +'| count')
    if "Count: 0 lines" in output:
        return False
    else:
        return True
def check_from_bgp_toospf_existance(net_connect):
    output = net_connect.send_command('admin display-config | match policy-options context all | match from-BGPVPN-to-OSPF | count')
    if "Count: 0 lines" in output:
        return True
    else:
        return False

def check_cpm_ospf_existance(net_connect):
        output = net_connect.send_command('admin display-config | match CPM-OSPF | count')
        if "Count: 0 lines" in output:
            return True
        else:
            return False



