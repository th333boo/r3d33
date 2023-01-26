#!/usr/bin/env python3
import threading
import socket
HOST,PORTS,PORTC = "127.0.0.1",3338,[1:65535]

def SrvSocket():
    io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    io.bind((HOST,PORTS))

def CltSocket():
    io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    io.connect((HOST,PORTC))
