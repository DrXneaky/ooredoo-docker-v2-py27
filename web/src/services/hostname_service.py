
from src.commons.utils import util
from src.controllers import template_controller


def generate_workorder_hostname( device_devices):
    template_name = "template_hostname.txt"
    template_path = util.get_template_path()
    output = ""
    output_hostname= template_controller.tempalte_generator_hostname(template_name, template_path, device_devices)
    output += output_hostname + "\n"
    return True, output