
from netaddr import *

IP='10.123.10.1/30'
ip=IPNetwork('10.123.10.1/30')
ip=ip.cidr
print(ip)
