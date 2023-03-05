#!/usr/bin/env python3
# coding: utf-8

import requests,socket

def TB_PUBLIC_IP():
    print('### [ IP ]###')
    HOSTNAME=socket.gethostname()   
    LOCAL_IP=socket.gethostbyname(HOSTNAME)
    URL_IP='http://ipinfo.io/json'
    PUBLIC_IP = requests.get(URL_IP).json()['ip']
    print("Your Computer HOSTNAME is:"+ HOSTNAME +"\n")   
    print("Your Computer LOCAL_IP Address is:"+ LOCAL_IP +"\n")     
    print("Your Computer PUBLIC IP Address is:"+ PUBLIC_IP +"\n")   
TB_PUBLIC_IP()