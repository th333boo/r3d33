#!/usr/bin/env python3
# coding: utf-8

from scapy.all import *
#from kit.footprint_custom import TB_FootPrintCustom

class TB_Scanner():
    def Scan():
        capture = sniff(prn=lambda x:x.show(), count=5)
        wrpcap("th333boo_dump", capture)
    Scan()

    # def foo(x):
    # return x+1
    # print "last"
    
    # def scanner():
    #     for ip in FRAME:
    #         if (ip.haslayer(53)):
    #             pass

    # #    for pkt.haslayer(UDP) and pkt.getlayer(UDP).sport == ports:
TB_Scanner()