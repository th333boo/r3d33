#!/usr/bin/env python3
from scapy.all import *
import socket
import threading 


HOST="127.0.0.1"
PORT=28987

print(f"Running the server on: {HOST} and port: {PORT}")

io = socket.socket()
io.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	io.bind((HOST, PORT))
	io.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {HOST} to port: {PORT}, because: {e}")

def OpenPort():
    for i in sniff:
        pkt = sniff(filter='tcp and tcp.flags.syn==1',iface='lo')
        pkt.show()
