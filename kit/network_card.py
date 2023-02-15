#!/usr/bin/env python3
from decouple import config
from scapy.all import *

def NetCard():
    print('### [ NETWORK CARD ] ###')
    for i in range(len(get_if_list())):
        print(i + 1, get_if_list()[i])
NetCard()
print(NetCard)