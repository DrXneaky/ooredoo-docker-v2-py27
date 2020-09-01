from xlsxwriter import Workbook
from netmiko import ConnectHandler, redispatch
import time
import sys
import time
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
from jinja2 import Environment, FileSystemLoader
import os
import smtplib
import datetime
import platform


# working directory in VM nNetwork automation
if platform.system()=='Windows':
    base_path = 'C:\\Users\\Ahmed\\Desktop\\automation tool folders\\from git\\ooredoo-docker-v2-py27\\web\\ressources\\audit\\'
else:
    base_path = '/ressources/audit/'

relative_path = sys.argv[2].strip()

# get device list from input
list_routers = sys.argv[1].strip().split(' ')

# command: check
command = " "        # command goes here

# script output
output = []

# audit function to be executed for each device 
def audit_function(ip):

    alcatel_lucent = {'device_type': 'alcatel_sros',
                      'ip': '{0}'.format(ip),
                      'username': 'OoredooIpam',
                      'password': 'Or~DIpM$19#!', }
    print('connecting to router', ip, '<br>')

    try:
        net_connect = ConnectHandler(**alcatel_lucent)
        cmd_output = net_connect.send_command(command, max_loops=1000)

        # Function goes here: manipulate cmd_output


        net_connect.disconnect()

    except Exception as e:
        print(str(e)+'<br>')
  

threads = []
try:
    for ip in list_routers:
        t = threading.Thread(target=audit_function, args=(ip,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
except Exception as e:
    print(str(e)+'<br>')



""" if len(output):
    output = output
else:
    output = [["NA", 0, 0]] """


# send mail
email_subject_line = 'Email Subject' # change email subject
sender_email_address = 'IPMPLS.Automation@ooredoo.tn'
sender_email_password = '123456'
receiver_email_address = "DTIngenierieServiceIP@ooredoo.tn, lobna.belgaied@ooredoo.tn, Karim.BEDOUI@ooredoo.tn"
cc_Of_Monthly_BH = "lobna.belgaied@ooredoo.tn"

file_loader = FileSystemLoader(base_path + 'email_templates/' + relative_path)
env = Environment(loader=file_loader)
template = env.get_template('html.html') # change template name 
output = template.render(anomalis_init=output)
template_attach = MIMEText(output, 'html')

msg = MIMEMultipart()
msg.attach(template_attach)


# attach Ooredoo logo to the email
try: 
    attachment = '/Ooredoo.jpg'
    fp = open(attachment, 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-ID', '<{}>'.format(attachment))
    msg.attach(img)
except Exception as e:
    print(str(e))


# setup the parameters of the message
msg['From'] = sender_email_address
msg['To'] = receiver_email_address
msg['Subject'] = email_subject_line

email_body_content = msg.as_string()

try:
    print('sending email..<br>')
    server = smtplib.SMTP('172.22.111.6:25')
    server.sendmail(sender_email_address,
                    receiver_email_address, email_body_content)
    print("mail is sent to "+ receiver_email_address + '<br>')
    server.quit()
except Exception as e:
    print(str(e)+'<br>')

#print(output)


# save output in an excel file 
try:
    workbook = Workbook(base_path + 'output_excel/' + relative_path + '/script_template_nokia.xlsx') # change 'script_template_nokia.xlsx'
    worksheet = workbook.add_worksheet("sheet1")
    worksheet.write(0, 0, "column1")
    worksheet.write(0, 1, "column2")
    worksheet.write(0, 2, "column3")
    worksheet.write(0, 3, "column4")
    """ for row, anomaly in enumerate(output, start=1):
        worksheet.write(row, 0, anomaly[0])
        worksheet.write(row, 1, anomaly[1])
        worksheet.write(row, 2, anomaly[2])"""
    workbook.close()
except Exception as e:
    print('error while creating the excel output file<br>')
    print(str(e))


print('script executed successfully<br>')