#!/usr/bin/env python3
# coding: utf-8

import requests

def DOMAIN_IP_HISTORY(DOMAIN_IP_HISTORY):
    print('###[ DOMAIN IP HISTORY ]###')
    DOMAIN_URL=config('DOMAIN_URL')
    DOMAIN_IP_HISTORY = requests.get('https://viewdns.info/iphistory/?domain='+ DOMAIN_URL)
DOMAIN_IP_HISTORY()
print(DOMAIN_IP_HISTORY)