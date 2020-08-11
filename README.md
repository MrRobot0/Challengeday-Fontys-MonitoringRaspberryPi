# Challengeday-Fontys-MonitoringRaspberryPi
This is a project for a Challenge day at the Fontys.

## About
It is a monitoring tool for Raspberry Pi's. There is a dashboard where you can monitor mutiple Raspberry Pi's and see if the CPU, RAM and Disk usage are all in the allowed zone. There also is an detailed page where you can see detailed info for a Raspberry Pi

## Screenshots
### Simpel page
<img src="https://i.imgur.com/p4mbfaj.gif"/>

### Detailed page
<img src="https://i.imgur.com/IaEbRWv.gif"/>

## Installation
1. Download all the files.
2. Install the requirements with pip: 
```python
pip install -r requirements.txt
```
3. Set port of you own choosing at the end of the app.py where port 80 is now: 
```python
app.run(host='0.0.0.0', port=80, debug=True)
```
4. Launch the app.py
5. goto the website with your own port: 
```html
localhost:80
```
