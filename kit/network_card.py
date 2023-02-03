#!/usr/bin/env python3
from decouple import config
from scapy.all import *

print('### [ NETWORK CARD ] ###')
print(get_if_list())