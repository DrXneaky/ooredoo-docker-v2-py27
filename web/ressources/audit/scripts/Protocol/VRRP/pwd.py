import os
from xlsxwriter import Workbook


try:
    print('hi')
    workbook = Workbook(
        'C:\\Users\\Ahmed\\Desktop\\automation tool folders\\from git\\ooredoo-docker-v2-py27\\web\\ressources\\output_excel\\Protocol\\VRRP\\pwd.xlsx')
    worksheet = workbook.add_worksheet("pwd")

    worksheet.write(0, 0, "Column1")
    worksheet.write(0, 1, "Column2")
    worksheet.write(0, 2, "Column3")
    worksheet.write(0, 3, "Column4")

    for i in [1, 2, 3, 4, 5]:
        worksheet.write(i, 0, "Column1")
        worksheet.write(i, 1, "Column2")
        worksheet.write(i, 2, "Column3")
        worksheet.write(i, 3, "Column4")

    workbook.close()
except Exception as e:
    print('lol', str(e))

