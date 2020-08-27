# # -*- coding: utf-8 -*-
# import os
# import subprocess
# from flask import Flask, render_template, request
#
# app = Flask(__name__)
#
# @app.route('/send',methods=['GET', 'POST'])
# def send():
# 	if request.method == 'POST':
# 		print "hello"
# 		ClientID=request.form['CLientId']
# 		Service_Type=request.form['Redundancy_Type']
# 		Device_Type=request.form['Device_Type']
# 		print Device_Type
# 		process=subprocess.Popen("python /home/my_flask_app/Nokia/Testing/Template.py "+ ClientID+" "+Service_Type +" " +Device_Type, stdout=subprocess.PIPE,universal_newlines=False, stderr=None, shell=True)
# 		output = process.communicate()
# 		output=output[0]
# 		f= open("/home/my_flask_app/Nokia/Testing/"+ClientID+".txt","w+")
# 		f.write(output)
# 		f.close()
# 		return render_template('work_order.html', age=output)
# 	return render_template('index.html')
#
# if __name__ =="__main__":
# 	app.run()
