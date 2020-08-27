
import os
import platform
from jinja2 import Environment, FileSystemLoader, select_autoescape


class Config(object):
    DEBUG = True
    ENV = "development"
    SECRET_KEY = os.environ.get('SECRET_KEY') or (
        "\xf9'\xe4p(\xa9\x12\x1a!\x94\x8d\x1c\x99l\xc7\xb7e\xc7c\x86\x02MJ\xa0")

    # app path variables
    APPLICATION_PATH = os.getcwd()
    if platform.system() == 'Windows':
        SCRIPTS_PATH = APPLICATION_PATH + '\\ressources\\scripts\\'
        OUTPUT_PDF_PATH = APPLICATION_PATH + '\\ressources\\reports_pdf'
        OUTPUT_EXCEL_PATH = APPLICATION_PATH + '\\ressources\\output_excel\\'
        WORK_ORDER_DIRECTORY = APPLICATION_PATH + \
            '\\ressources\\work_order_folder\\work_order_b2b\\'
        timos_excel_file = APPLICATION_PATH + '\\ressources\\formulaire.xls'
    else:
        SCRIPTS_PATH = APPLICATION_PATH + '/ressources/scripts/'
        OUTPUT_PDF_PATH = APPLICATION_PATH + '/ressources/reports_pdf'
        OUTPUT_EXCEL_PATH = APPLICATION_PATH + '/ressources/output_excel/'
        WORK_ORDER_DIRECTORY = APPLICATION_PATH + \
            '/ressources/work_order_folder/work_order_b2b/'
        timos_excel_file = APPLICATION_PATH + '/ressources/formulaire.xls'

    # db variables
    DB_URL = os.environ.get('DB_URL') or 'db:5432'
    DB_NAME = os.environ.get('DB_NAME') or 'db_app'
    DB_USER = os.environ.get('DB_USER') or 'postgress'
    DB_PASSWD = os.environ.get('DB_PASSWD') or 'root'

    # timos_excel_file =  APPLICATION_PATH+'/ressources/formulaire.xls'

    # cron manager variables
    CRON_ENV = Environment(
        loader=FileSystemLoader(
            os.path.join(
                os.path.join(APPLICATION_PATH, 'ressources'),
                'cron'
            )
        ),
        autoescape=select_autoescape(['html', 'txt', 'sh'])
    )
    CRON_SCRIPT_DIRECTORY = '/usr/local/bin/'
    CRON_LOG_DIRECTORY = '/var/log/cronlogs/'
    CRON_DESTINATION_EMAIL = 'ahess190@gmail.com'
    CRON_LOGGING_FORMAT = 'cron{0}.log'


def make_path(dir, file):
    if platform.system() == 'Windows':
        return dir + '\\' + file
    else:
        return dir + '/' + file


def convert_to_windows_path(path):
    return path.replace('/', '\\')


def convert_to_correct_path(path):
    if platform.system() == 'Windows':
        return convert_to_windows_path(path)
    else:
        return path
