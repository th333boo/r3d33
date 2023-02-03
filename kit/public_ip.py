#!/usr/bin/env python3
import requests,socket

print('### [ IP ]###')
HOSTNAME=socket.gethostname()   
LOCAL_IP=socket.gethostbyname(HOSTNAME)   
PUBLIC_IP = requests.get('http://ipinfo.io/json').json()['ip']
print("Your Computer HOSTNAME is:"+ HOSTNAME +"\n")   
print("Your Computer LOCAL_IP Address is:"+ LOCAL_IP +"\n")     
print("Your Computer PUBLIC IP Address is:"+ PUBLIC_IP +"\n")   