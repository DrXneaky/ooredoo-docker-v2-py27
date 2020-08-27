
from jinja2 import Environment, FileSystemLoader


def tempalte_generator_service(template_name, template_path, service_existance_bol, device_devices, client_attribute):

    file_loader = FileSystemLoader(template_path)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    output = template.render(
                            attributes = client_attribute,
                            service_existance_bol = service_existance_bol,
                            device_devices = device_devices[0])
    return output

def tempalte_generator_service_vpn(template_name, template_path, service_existance_bol, device_devices, client_attribute, from_bgp_toospf_existance_bol, cpm_ospf_existance_bol):

    file_loader = FileSystemLoader(template_path)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    output = template.render(from_bgp_toospf_existance_bol = from_bgp_toospf_existance_bol,
                             cpm_ospf_existance_bol = cpm_ospf_existance_bol,
                            attributes = client_attribute,
                            service_existance_bol = service_existance_bol,
                            device_devices = device_devices[0])
    return output

def tempalte_generator_qos(template_name, template_path, client_attribute):
    file_loader = FileSystemLoader(template_path)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    output = template.render(
        qos = int(client_attribute["qos"]),
        attributes=client_attribute)
    return output

def tempalte_generator_hostname(template_name, template_path, device_devices):
    print (template_path)
    file_loader = FileSystemLoader(template_path)
    env = Environment(loader=file_loader)
    template = env.get_template(template_name)
    output = template.render( device_devices=device_devices[0] )
    return output

