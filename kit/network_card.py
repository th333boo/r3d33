#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *

def TB_NetCard():
    print('### [ NETWORK CARD ] ###')
    for i in range(len(get_if_list())):
        print(i + 1, get_if_list()[i])
TB_NetCard()
print(TB_NetCard())