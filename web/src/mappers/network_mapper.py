from netaddr import *

def convert_subnet(ip):
    """
    convert ip interface to subnet
    :param ip:
    :return: subnet
    """
    return str(IPNetwork(ip).cidr)