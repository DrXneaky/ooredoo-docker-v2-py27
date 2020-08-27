from netmiko import ConnectHandler


class Connection:
    def __init__(self, ip):
        self.ip = ip


    def connect_to_nokia_device(self):
        Alcatel7750 = {
            'device_type': 'alcatel_sros',
            'ip': self.ip,
            'username': 'OoredooIpam',
            'password': 'Or~DIpM$19#!',
            'verbose': False,  # optional, defaults to False
        }
        return ConnectHandler(**Alcatel7750)

    def disconnect_to_nokia_device(self, netmikoObject):
        netmikoObject.disconnect()
