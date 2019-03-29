from flask import Flask, render_template, Markup
import datetime
import socket
import shutil
import psutil
import struct
import sys
import time
import ConfigParser
app = Flask(__name__, static_url_path='/static')







@app.route("/simpel")
def simple():

	def synctime():
		# List of servers in order of attempt of fetching
		server_list = ['ntp.iitb.ac.in', 'time.nist.gov', 'time.windows.com', 'pool.ntp.org']

		'''
		Returns the epoch time fetched from the NTP server passed as argument.
		Returns none if the request is timed out (5 seconds).
		'''
		def gettime_ntp(addr='time.nist.gov'):
			# http://code.activestate.com/recipes/117211-simple-very-sntp-client/
			TIME1970 = 2208988800      # Thanks to F.Lundh
			client = socket.socket( socket.AF_INET, socket.SOCK_DGRAM )
			data = '\x1b' + 47 * '\0'
			try:
				# Timing out the connection after 5 seconds, if no response received
				client.settimeout(5.0)
				client.sendto( data, (addr, 123))
				data, address = client.recvfrom( 1024 )
				if data:
					epoch_time = struct.unpack( '!12I', data )[10]
					epoch_time -= TIME1970
					return epoch_time
			except socket.timeout:
				return None

		if __name__ == "__main__":
			# Iterates over every server in the list until it finds time from any one.
			for server in server_list:
				epoch_time = gettime_ntp(server)
				if epoch_time is not None:
					# SetSystemTime takes time as argument in UTC time. UTC time is obtained using utcfromtimestamp()
					utcTime = datetime.datetime.utcfromtimestamp(epoch_time)
					win32api.SetSystemTime(utcTime.year, utcTime.month, utcTime.weekday(), utcTime.day, utcTime.hour, utcTime.minute, utcTime.second, 0)
					# Local time is obtained using fromtimestamp()
					localTime = datetime.datetime.fromtimestamp(epoch_time)
					print("Time updated to: " + localTime.strftime("%Y-%m-%d %H:%M") + " from " + server)
					break
				else:
					print("Could not find time from " + server)

	def test():
		global test
		test = "test1"



	now = datetime.datetime.now()
	timeString = now.strftime("%H:%M")
   
	hostnameString = socket.gethostname()
   
	total, used, free = shutil.disk_usage("\\")
	disktotal = "%d GB" % (total // (2**30))
	diskused = "%d GB" % (used // (2**30))
	diskfree = "%d GB" % (free // (2**30))
   
   
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
		'ram_usage': ram_usage,
		'test' : test
    }
	return render_template('simple.html', **templateData)

@app.route("/dash")
def dash():
	templateData = {
	'title': 'Dashboard'
	}
	return render_template('dashboard.html', **templateData)

@app.route("/")
def detail():	
	templateData = {
		'title' : 'Monitoring'
    }
	return render_template('detailed.html', **templateData)
	
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
	
@app.route("/test")
def dash():
     configParser = ConfigParser.RawConfigParser()   
	 configFilePath = r'/static/IP adressen/configuration-infrastructure.cfg'
	 configParser.read(configFilePath)
	 
	 self.path = configParser.get('your config', 'sensorftpMAC')
	
	
	
	templateData = {
	'title': 'test'
	}
	return render_template('test.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
