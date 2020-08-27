import re


def validate_ipaddres(ip_system):
    pat = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")
    return pat.match(ip_system)


def get_device_type(ip_system):
    types = ['Router', 'Switch']
    return types[int(ip_system.split('.')[3])%2]