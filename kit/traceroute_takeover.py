#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *

print('### [ TRACEROUTE ] ###')
ans,unans=traceroute(PUBLIC_IP,l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="th333boo.com")))
res,unans = sr(IP(dst=PUBLIC_IP", ttl=(5,10), flags="MF")/UDP(sport=RandShort( ), dport=53), timeout=125)

print('### [ TRACEROUTE TAKEOVER ] ###')