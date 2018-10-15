import time
import urllib3
import json
import RPi.GPIO as device
while 1:
    baseURL="https://deepakkumarpandeychs.000webhostapp.com/getstatus1.php"
    http = urllib3.PoolManager()
    r=http.request('GET',"https://deepakkumarpandeychs.000webhostapp.com/getstatus1.php")
    data = r.data.decode('utf-8')
    data=data[2:-2].split("},{")
    f=14
    a=2
    l=3
    m=15
    device.setwarnings(False)
    device.setmode(device.BCM)
    device.setup(f,device.OUT)
    device.setup(a,device.OUT)
    device.setup(l,device.OUT)
    device.setup(m,device.OUT)
    if "ON" in data[0]:
        device.output(f, True)
    elif "OFF" in data[0]:
        device.output(f, False)
    if "ON" in data[1]:
        device.output(a, True)
    elif "OFF" in data[1]:
        device.output(a, False)
    if "ON" in data[2]:
        device.output(l, True)
    elif "OFF" in data[2]:
        device.output(l, False)
    if "ON" in data[3]:
        device.output(m, True)
    elif "OFF" in data[3]:
        device.output(m, False)
