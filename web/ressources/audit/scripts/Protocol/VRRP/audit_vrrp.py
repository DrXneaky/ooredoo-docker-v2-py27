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
from netmiko.ssh_exception import NetMikoTimeoutException

# upload Nokia.txt, Ooredoo.jpg under Protocol/VRRP
# change email creds
print('input_list', sys.argv[1].strip().split(' '))
# working directory in VM nNetwork automation
if platform.system() == 'Windows':
    base_path = 'C:\\Users\\Ahmed\\Desktop\\automation tool folders\\from git\\ooredoo-docker-v2-py27\\web\\ressources\\audit\\'
else:
    base_path = '/ressources/audit/'

# variable initialization
cmd_vrrp_policy = "admin display-config detail | match port-down context all | match \"no priority\" context all | match policy "
cmd_vrrp_policy_check = "admin display-config | match \"policy {} context\" context all"
FILEPATH_NOKIA = base_path + "scripts/Protocol/VRRP/Nokia.txt"
READING = "r"
threads = []
# script output
anomalie_list = []

# read list of routers
with open(FILEPATH_NOKIA, READING) as f:
    list_routers = f.readlines()

list_routers = sys.argv[1].strip().split(' ')

def find_vrrp_anomalies(ip):

    alcatel_lucent = {'device_type': 'alcatel_sros',
                      'ip': '{0}'.format(ip),
                      'username': 'OoredooIpam',
                      'password': 'Or~DIpM$19#!', }
    list_vrrp = []
    list_vrrp_anomalie_by_router = []
    try:
        net_connect = ConnectHandler(**alcatel_lucent)
        out_vrrp_policy = net_connect.send_command(cmd_vrrp_policy, max_loops=1000)
        if out_vrrp_policy:
            for line in out_vrrp_policy.splitlines():
                list_vrrp.append(line.split()[1])
            if list_vrrp:
                hostname = net_connect.find_prompt().split("#")[0]
                list_vrrp_anomalie_by_router.append(list_vrrp)
                list_vrrp_anomalie_by_router.append(hostname)
                list_vrrp_anomalie_by_router.append(len(list_vrrp))
                anomalie_list.append(list_vrrp_anomalie_by_router)
        net_connect.disconnect()
    except NetMikoTimeoutException as exception:
        print(str(exception))

# find_vrrp_anomalies("192.168.160.100")
# print anomalie_list
try:
    for ip in list_routers:
        t = threading.Thread(target=find_vrrp_anomalies, args=(ip,))
        threads.append(t)
        t.start()
    for thread in threads:
        thread.join()
except Exception as e:
    print('connection de device failed')


if len(anomalie_list):
    anomalie_list = anomalie_list
else:
    anomalie_list = [["NA", 0, 0]]

# send mail
attachment = base_path + 'scripts/Protocol/VRRP/Ooredoo.jpg'
READING = "r+"
email_subject_line = 'Weekly Report Nokia vrrp Check'
sender_email_address = 'phpipam.bbipmpls@ooredoo.tn'
sender_email_password = '123456'
receiver_email_address = "DTIngenierieServiceIP@ooredoo.tn, lobna.belgaied@ooredoo.tn, Karim.BEDOUI@ooredoo.tn"
cc_Of_Monthly_BH = ""
file_loader = FileSystemLoader(base_path + 'scripts/Protocol/VRRP')
env = Environment(loader=file_loader)
template = env.get_template('vrrp_core.html')
output = template.render(anomalis_init=anomalie_list)
template_attach = MIMEText(output, 'html')
fp = open(attachment, 'rb')
img = MIMEImage(fp.read())
fp.close()
msg = MIMEMultipart()
msg.attach(template_attach)
img.add_header('Content-ID', '<{}>'.format(attachment))
msg.attach(img)
# setup the parameters of the message
msg['From'] = sender_email_address
msg['To'] = receiver_email_address
msg['Subject'] = email_subject_line

email_body_content = msg.as_string()

try:
    server = smtplib.SMTP('172.22.111.6:25')
    server.sendmail(sender_email_address,
                    receiver_email_address, email_body_content)
    # print("mail is sent to "+ receiver_email_address)
    server.quit()
except Exception as e:
    print('mail failed')
#print(output)

try:
    workbook = Workbook(base_path + 'output_excel\\Protocol\\VRRP\\audit_vrrp.xlsx')
    worksheet = workbook.add_worksheet("sheet1")
    worksheet.write(0, 0, "Hostname")
    worksheet.write(0, 1, "Nombre d'anomalies")
    worksheet.write(0, 2, "interface ID")
    for row, anomaly in enumerate(anomalie_list, start=1):
        worksheet.write(row, 0, anomaly[0])
        worksheet.write(row, 1, anomaly[1])
        worksheet.write(row, 2, anomaly[2])
    workbook.close()
except Exception as e:
    print(str(e))
