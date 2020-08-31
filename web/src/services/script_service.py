import sys
import os
import shutil
from config import Config, make_path
import subprocess
from src.commons.utils.file_manager import convert_xlsx2html


def run_script(script):
    status = "Failed"
    report = "A problem has occurred when trying to run the script!"
    try:
        path = "".join([
            Config.SCRIPTS_PATH,
            script['scriptType'].replace('_', '\\'),
            '\\',
            script['scriptName'],
        ])
        command = "".join(['python ', '"',path,'"'])
        print(command)
        stream = os.popen(command)
        #stream = os.popen(" ".join(['python', path]))
        report = stream.read()
        print('report', report)
        report = convert_xlsx2html("".join([
            Config.OUTPUT_EXCEL_PATH,
            script['scriptType'].replace('_', '/'),
            '/',
            script['scriptName'].replace('.py', '.xlsx')
        ]))
        # pdfkit.from_file('pandas_output.html', 'pandas_out.pdf')
        # path = Config.SCRIPTS_PATH+script['scriptType'].replace('_', '/')
        # +'/'+script['scriptName']
        # result = subprocess.run(['python', path],
        #                         stderr=subprocess.PIPE,
        #                         stdout=subprocess.PIPE)
        # report = result.stderr.decode('utf-8') +result.stdout.decode('utf-8')
        status = "Success"
    except AttributeError as attErr:
        #path = Config.SCRIPTS_PATH+script['scriptType'].replace('_','/')+'/'+script['scriptName']
        #process = subprocess.Popen(['python', path],shell = True,stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        #status = "Success"
        #resOut, resErr = process.communicate()
        #report = "stdout:\n" + resOut + "\nstderr:\n" + resErr
        execute = execfile(make_path(
            Config.SCRIPTS_PATH+script['scriptType'].replace('_', '/')+'/', script['scriptName']), globals())
        report = message
        status = 'Success'
    except Exception as exception:
        #print ("exception",str(exception))
        status = "Error"
        report = str(exception)
    finally:
        return status, report


def add_folder(dir_path, name):
    try:
        # print("added folder", os.path.join(path, name))
        for path in dir_path:
            os.mkdir(os.path.join(path, name))
        response = "OK"
    except FileExistsError:
        response = name + " Folder already exists"
    except Exception:
        response = "An error occurred while creating the folder"
    return response


def delete_folder(dir_path, name):
    try:
        for path in dir_path:
            shutil.rmtree(os.path.join(path))
        response = "OK"
    except OSError as e:
        response = "Error: " + e.filename + ' - ' + e.strerror
    except FileNotFoundError:
        response = name + " Folder not found"
    except Exception:
        response = "An error occurred while deleting the folder"
    return response
