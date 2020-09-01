from config import Config
import os
import json
#import pandas
from xlsx2html import xlsx2html


def create_workorder_file(workorder_file_name, output_workorder):
    file = open(workorder_file_name, "w")
    try:
        try:
            file.write(output_workorder)
        finally:
            file.close()
    except IOError:
        print("file not created")


def get_file_names_util(path):
    script_names = []
    value = 1
    for path, directory, files in os.walk(path):
        for file in files:
            if '.py' in file and '.pyc' not in file:
                script = {
                    "name": file,
                    "value": value,
                }
                value += 1
                script_names.append(script)
    return script_names


class Folder:
    def __init__(self, title='', children=[], parent=None, level=0, path=""):
        self.title = title
        self.children = children
        self.parent = parent
        self.level = level
        self.path = path


def get_children(folder, script_path):
    children = []
    for dirpath, subdir, files in os.walk(script_path+folder.path):
        for name in subdir:
            if name != '__pycache__':
                if folder.level == 0:
                    child = os.path.join(dirpath, name).replace(
                        script_path, '').replace('\\', '/').split('/')[1]
                    children.append(child)
                elif folder.level == 1:
                    child = os.path.join(dirpath, name).replace(
                        script_path, '').replace('\\', '/').split('/')[2]
                    children.append(child)
    children = set(children)
    return list(children)


def get_tree(script_path):
    folders = []
    for dirpath, subdir, files in os.walk(script_path):
        for name in subdir:
            if name != '__pycache__':
                path = os.path.join(dirpath, name).replace(script_path, '')
                path = path.replace('\\', '/')
                folder = Folder(name)
                folder.path = path
                folder.level = path.count("/")
                if folder.level == 1:
                    folder.parent = path.replace('/'+name, '')
                elif folder.level == 2:
                    folder.parent = path.split('/')[1]
                elif folder.level == 0:
                    folder.parent = '.'
                folders.append(folder)

    for folder in folders:
        folder.children = get_children(folder, script_path)

    json_string = json.dumps([ob.__dict__ for ob in folders])
    return json_string


def convert_xlsx2html(excel_path, title):
    try:
        """ wb = pandas.read_excel(excel_path)
        return (wb.to_html()) """
        out_stream = xlsx2html(excel_path)
        out_stream.seek(0)
        html = out_stream.read()
        html = html.replace(
            '<table  style="border-collapse: collapse" border="0" cellspacing="0" cellpadding="0"><colgroup>',
            '<table  style="border-collapse: collapse" border="1px" cellspacing="5px" cellpadding="5px"><colgroup>'
            )
        html = html.replace('<title>Title</title>', '<title>{0}</title>'.format(title))
        return(html)
    except Exception as e:
        return str(e)
