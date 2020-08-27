
#timos_excel_file =  'C:/Users/Monia/Downloads/devWorks/ooredoo_migrate_backend/ressources/formulaire.xls'

import platform
from config import Config
if platform.system()=='Windows':
  timos_excel_file = Config.APPLICATION_PATH + '\\ressources\\formulaire.xls'
else:
  timos_excel_file = Config.APPLICATION_PATH + '/ressources/formulaire.xls'  
