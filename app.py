from flask import Flask, render_template, Markup
import datetime
import socket
import shutil
import psutil
import struct
import sys
import time
app = Flask(__name__, static_url_path='/static')



@app.route("/refreshsimpel")
def refreshsimpel():
	now = datetime.datetime.now()
	timeString = now.strftime("%H:%M")
   
	hostnameString = socket.gethostname()
   
	total, used, free = shutil.disk_usage("\\")
	disktotal = (total // (2**30))
	diskused = (used // (2**30))
	diskfree = (free // (2**30))
   
   
	IP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
   
	cpu_usage = psutil.cpu_percent()
	ram_usage = psutil.virtual_memory()[2]
 
	
	
	
	templateData = {
		'title' : 'Monitoring',
		'time': timeString,
		'hostname': hostnameString,
		'disktotal': disktotal,
		'diskused': diskused,
		'diskfree': diskfree,
		'IP': IP,
		'cpu_usage': cpu_usage,
		'ram_usage': ram_usage
    }
	return render_template('refreshsimpel.html', **templateData)

@app.route("/dash")
def dash():
	templateData = {
	'title': 'Dashboard'
	}
	return render_template('dashboard.html', **templateData)

	
@app.route("/detail")
def detail():
	hostnameString = socket.gethostname()
	
	templateData = {
		'title' : 'Monitoring',
		'hostname' : hostnameString
    }
	return render_template('detailed.html', **templateData)

	
@app.route("/")
def simpel():
	hostnameString = socket.gethostname()
	
	templateData = {
		'title' : 'Simpel',
		'hostname' : hostnameString
    }
	return render_template('simple.html', **templateData)

	
@app.route("/cpuram")
def cpuram():
	cpu_usage = psutil.cpu_percent()
	ram_usage = psutil.virtual_memory()[2]
   
	templateData = {
		'title' : 'cpuram',
		'cpu_usage': cpu_usage,
		'ram_usage': ram_usage
    }
	return render_template('cpuram.html', **templateData)
	
	
@app.route("/timehostipdisk")
def timehostipdisk():
	now = datetime.datetime.now()
	timeString = now.strftime("%H:%M")
   
	hostnameString = socket.gethostname()
   
	total, used, free = shutil.disk_usage("\\")
	disktotal = "%d GB" % (total // (2**30))
	diskused = "%d GB" % (used // (2**30))
	diskfree = "%d GB" % (free // (2**30))
   
	IP = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]	
   
	templateData = {
		'title' : 'timehostipdisk',
		'time': timeString,
		'hostname': hostnameString,
		'disktotal': disktotal,
		'diskused': diskused,
		'diskfree': diskfree,
		'IP': IP
    }
	return render_template('timehostipdisk.html', **templateData)

@app.route("/chart")
def chart():
	cpu_usage = psutil.cpu_percent()
	
	def chartcpu():
		global cpu1
		global cpu2
		global cpu3
		global cpu4
		global cpu5
		cpu1 = psutil.cpu_percent()
		chartcpu()
		
	
	
	templateData = {
		'title' : 'Chart',
		'cpu_usage': cpu_usage,
		'cpu1' : cpu1,
		'cpu2' : cpu2,
		'cpu3' : cpu3,
		'cpu4' : cpu4,
		'cpu5' : cpu5
    }
	return render_template('chart.html', **templateData)
	
@app.route("/test")
def test():
	
	templateData = {
	'title': 'test'
	}
	return render_template('test.html', **templateData)


if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
