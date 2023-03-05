#!/usr/bin/env python3
# coding: utf-8

from decouple import config
from scapy.all import *

class SmS333():
    def main():
        scapy.layers=('gprs','bluetooth','dns')
        print(scapy.layers.gprs.GPRS(ls))

if __name__ == "__main__":
    SmS333()