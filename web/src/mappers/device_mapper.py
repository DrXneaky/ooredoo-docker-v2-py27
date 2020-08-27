"""

"""

def validate_hostname(hostname):
    list_hostname = list(hostname)
    device_name =""
    for caracter in list_hostname:
        try:
            device_name = device_name + str(int(caracter))
        except:
            continue
    try:
        print(int(list_hostname[-1]))
    except:
        device_name = device_name + list_hostname[-2] + list_hostname[-1]
    return device_name
