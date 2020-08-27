from config import Config
import os
import json

class Folder:
  def __init__(self, title='', children=[], parent=None, level=0, path=""):
    self.title = title
    self.children = children
    self.parent = parent
    self.level = level
    self.path = path

def get_children(folder,script_path):
  children = []
  for dirpath, subdir, files in os.walk(script_path+folder.path):
    for name in subdir:
      if name != '__pycache__':
        if folder.level == 0:
          child = os.path.join(dirpath, name).replace(script_path,'').replace('\\', '/').split('/')[1]
          children.append(child)
        elif folder.level == 1:
          child = os.path.join(dirpath, name).replace(script_path,'').replace('\\', '/').split('/')[2]
          children.append(child)
  children = set(children)
  return list(children)

def get_tree():  
  script_path = Config.SCRIPTS_PATH
  tree =[]
  folders = []
  value = 1
  for dirpath, subdir, files in os.walk(script_path):
    for name in subdir:
      if name != '__pycache__':
        path = os.path.join(dirpath, name).replace(script_path,'')
        path = path.replace('\\', '/')
        folder = Folder(name)
        folder.path = path
        folder.level = path.count("/")
        if folder.level == 1 :
          folder.parent = path.replace('/'+name,'')
        elif folder.level == 2:
          folder.parent = path.split('/')[1]
        elif folder.level == 0:
          folder.parent = '.'
        folders.append(folder)

  for folder in folders:
    folder.children = get_children(folder,script_path)  

  json_string = json.dumps([ob.__dict__ for ob in folders])
  return json_string

#print(get_tree())

