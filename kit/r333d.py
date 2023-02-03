#!/usr/bin/env python3
from decouple import config
from scapy.all import *

######################################
print('### [ IP INPUT ] ###')
print("Enter IP_SRC <space> IP_DST")
IP_SRC, IP_DST = input().split(' ')

######################################
print('### [ DATA RUNNER ] ###')
HOST,PORTS= "127.0.0.1",3338
ALL_PORT = range(1,65535)
PAYLOAD=(b"th333boo is taking over")
