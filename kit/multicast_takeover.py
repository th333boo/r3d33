#!/usr/bin/env python3
from decouple import config
from scapy.all import *
from footprint_custom import FootPrint
print('### [ MULTICAST TAKEOVER ] ###')
FootPrint().FootPrintClean()
class Multicast_Takeover():
    def multicast_scan():
        pass
    def multicast_reply():
        pass
    def multicast_controller(Ether,HW_SRC,HW_DST,IP,UDP,PAYLOAD):
        ssdpRequest = Ether(src=HW_SRC, dst=HW_DST) / IP(src="192.168.1.143",dst="239.255.255.250") / UDP(sport=1025, dport= 1900) / PAYLOAD
        sendp(ssdpRequest)
        print (ssdpRequest)
    def multicast_takeover():
        pass