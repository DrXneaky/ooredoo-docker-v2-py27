from netmiko import ConnectHandler


class Connection:
    def __init__(self, router):
        self.router = router
    def _NokiaConnection(self):
        Alcatel7750 = {
            'device_type': 'alcatel_sros',
            'ip':   self.router,
            'username': 'abdelbasset.zabi',
            'password': 'Mohamed.22',
            'verbose': False,       # optional, defaults to False
        }
        return ConnectHandler(**Alcatel7750)
