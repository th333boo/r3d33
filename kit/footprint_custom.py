#!/usr/bin/env python3
from decouple import config
from scapy.all import *

class FootPrint ():
    print('### [ FOOTPRINT CUSTOM ] ###')
    def __self__(self):
        self.HW_SRC = "FF:FF:FF:FF:FF:FF"
        self.HW_DST = "FF:FF:FF:FF:FF:FF"
        # self.IP_SRC = "8.2.246.1"
        # self.IP_DST = "8.3.11.1"
        self.IP_GW = "192.168.1.1"
        self.IP_SRC = config('IP_SRC')
        self.IP_DST = config('IP_DST')
        return self
    print(__self__.__format__)
    print('### [ FOOTPRINT CLEANER ] ###')
    def FootPrintClean(self,HW_SRC,HW_DST,IP_DST,IP_GW,IP_SRC,Ether,IP,FRAME_IP,FRAME):
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
    FootPrintClean()

