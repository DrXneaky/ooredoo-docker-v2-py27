
import os
import platform
from config import Config



def get_path_workorder(workorder_name):
    if workorder_name:
        script_dir = os.path.dirname(__file__).split("src")[0]
        #rel_path = "ressources\work_order_folder\\work_order_b2b\\"+workorder_name
        if platform.system()=='Windows':
            rel_path = "\\ressources\work_order_folder\\work_order_b2b\\"+workorder_name
        else:
            rel_path = "/ressources/work_order_folder/work_order_b2b/"+workorder_name
        #abs_file_path = os.path.join(script_dir, rel_path)
        abs_file_path = Config.APPLICATION_PATH + rel_path
        return abs_file_path

def get_template_path():
    script_dir = os.path.dirname(__file__).split("src")[0]
    #rel_path = "ressources\\templates\\"
    if platform.system()=='Windows':
        rel_path = '\\ressources\\templates\\'
    else:
        rel_path = '/ressources/templates/' 
    abs_file_path = Config.APPLICATION_PATH + rel_path
    return abs_file_path

def create_qos(qos):
    if qos:
        return int(qos) + 1000
    else:
        return 1010