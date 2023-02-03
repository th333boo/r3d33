#!/usr/bin/env python3
from decouple import config
from scapy.all import *

print('### [ FOOTPRINT CUSTOM ] ###')
HW_SRC = "FF:FF:FF:FF:FF:FF"
HW_DST = "FF:FF:FF:FF:FF:FF"
IP_SRC = "8.2.246.1"
IP_DST = "8.3.11.1"
IP_GW = "192.168.1.1"
IP_SRC = config('IP_SRC')
IP_DST = config('IP_DST')


print('### [ FOOTPRINT CLEANER ] ###')
print('# [ BEFORE ] #')
FRAME_IP = IP()
FRAME = Ether()

FRAME.show()
FRAME_IP.show()

print('# [ AFTER ] #')
FRAME = Ether(src=HW_SRC, dst=HW_DST)
FRAME_IP = IP(src=IP_SRC, dst=IP_DST, ttl=(111), frag=0, tos=0x0)
FRAME.show()
FRAME_IP.show()