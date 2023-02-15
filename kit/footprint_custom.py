#!/usr/bin/env python3
from decouple import config
from scapy.all import *

FRAME_IP = IP()
FRAME = Ether()
class FootPrint ():
    print('### [ FOOTPRINT CUSTOM ] ###')
    def __init__(self,HW_SRC,HW_DST,IP_GW,IP_SRC,IP_DST):
        self.HW_SRC = HW_SRC
        self.HW_DST = HW_DST
        # self.IP_SRC = "8.2.246.1"
        # self.IP_DST = "8.3.11.1"
        self.IP_SRC = IP_SRC
        self.IP_DST = IP_DST
        self.IP_GW = IP_GW
    print('### [ FOOTPRINT CLEANER ] ###')
    def FootPrintClean(self,HW_SRC,HW_DST,IP_DST,IP_SRC,Ether,IP,FRAME_IP,FRAME):
        print('# [ BEFORE ] #')
        FRAME.show()
        FRAME_IP.show()
        print('# [ AFTER ] #')
        FRAME = Ether(src=HW_SRC, dst=HW_DST)
        FRAME_IP = IP(src=IP_SRC, dst=IP_DST, ttl=(111), frag=0, tos=0x0)
        FRAME.show()
        FRAME_IP.show()

CurrentFrame = __init__(config('HW_SRC'),config('HW_DST'),config('IP_SRC'),config('IP_DST'),config('IP_GW'),config('IP_SRC'),config('IP_SRC'))

