#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *

HW_SRC=str(config('HW_SRC'))
HW_DST=str(config('HW_DST'))
IP_SRC=str("8.2.246.1")
IP_DST=str("8.3.11.1")

class TB_FootPrintCustom ():
    print('### [ FOOTPRINT CUSTOM ] ###')
    def __init__(self,HW_SRC=str(config('HW_SRC')),HW_DST=str(config('HW_DST')),IP_SRC=str("8.2.246.1"),IP_DST=str("8.3.11.1")):
        self.HW_SRC = HW_SRC
        self.HW_DST = HW_DST
        self.IP_SRC = IP_SRC
        self.IP_SRC = IP_SRC
        self.IP_DST = IP_DST
        self.IP_GW = ''
    print('OK')
    print('### [ FOOTPRINT CLEANER ] ###')
    def TB_FootPrintClean(self,Ether,IP,FRAME_IP,FRAME):
        print('# [ BEFORE ] #')
        FRAME=Ether()
        IP=IP()
        FRAME.show()
        FRAME_IP.show()
        print('# [ AFTER ] #')
        FRAME = Ether(src=HW_SRC, dst=HW_DST)
        FRAME_IP = IP(src=IP_SRC, dst=IP_DST, ttl=(111), frag=0, tos=0x0)
        FRAME.show()
        FRAME_IP.show() 
    print('OK')