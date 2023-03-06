#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *
from kit.footprint_custom import TB_FootPrintCustom
from kit.public_ip import TB_PUBLIC_IP

class TB_TraceRoute():
    print('### [ TRACEROUTE ] ###')
    ans,unans=sr(TB_PUBLIC_IP,l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="th333boo.com")))
    res,unans = sr(IP(dst=TB_PUBLIC_IP, ttl=(5,10), flags="MF")/UDP(sport=RandShort( ), dport=53), timeout=125)

    print('### [ TRACEROUTE TAKEOVER ] ###')