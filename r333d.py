#!/usr/bin/env python3
from scapy.all import *
# from scrapy.mail import MailSender
from decouple import config
import threading,socket,time,requests

print('### [ IP INPUT ]###')
print("Enter IP_SRC <space> IP_DST")
IP_SRC, IP_DST = input().split(' ')

print('### [ DATA RUNNER ]###')
HOST,PORTS= "127.0.0.1",3338
TPORT = range(1,65535)
PAYLOAD=(b"th333boo is taking over")

print('### [ PUBLIC IP ]###')
PUBLIC_IP = requests.get('http://ipinfo.io/json').json()['ip']
print(PUBLIC_IP)

print('### [ NETWORK CARD ]###')
print(get_if_list())

print('### [ FOOTPRINT CUSTOM ]###')
HW_SRC = "FF:FF:FF:FF:FF:FF"
HW_DST = "FF:FF:FF:FF:FF:FF"
IP_SRC = "8.2.246.1"
IP_DST = "8.3.11.1"
IP_SRC = config('IP_SRC')
IP_DST = config('IP_DST')

print('### [ FOOTPRINT CLEANER ]###')
print('# [ BEFORE ]#')
ip = IP()
frame = Ether()
ip.show()
frame.show()
print('# [ AFTER ]#')
ip = IP(src=IP_SRC, dst=IP_DST, ttl=(111), frag=0, tos=0x0)
frame = Ether(src=HW_SRC, dst=HW_DST)
ip.show()
frame.show()

print('### [ TRACEROUTE ]###')

print('### [ TRACEROUTE TAKEOVER ]###')

print('### [ NETWORK TAKEOVER ]###')

print('### [ ARP TAKEOVER ]###')

print('### [ MULTICAST TAKEOVER ]###')

print('### [ DNS TAKEOVER ]###')

print("### [ PORT SCANNING TAKEOVER ]###")

print('### [ EMAIL SETUP ]###')
smtphost=settings[config('MAIL_HOST')],
mailfrom=settings[config('MAIL_FROM')],
smtpuser=settings[config('MAIL_USER')],
smtppass=settings[config('MAIL_PASS')],
smtpport=settings.getint(config('MAIL_PORT')),
smtptls=settings.getbool(config('MAIL_TLS')),
smtpssl=settings.getbool(config('MAIL_SSL')),
mailer  = MailSender().from_settings(settings)
print(smtphost)