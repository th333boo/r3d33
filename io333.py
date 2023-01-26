#!/usr/bin/env python3
import threading
import socket
import time

HOST,PORTS,PORTC = "127.0.0.1",3338,3339
io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def SrvSocket():
    io.bind((HOST,PORTS))

def CltSocket():
    io.connect((HOST,PORTC))

print("START SCANNING PORT")
def PortScan(PORT):
    status = False
    try:
        CltSocket()
        print(CltSocket)
        status = True
    except:
        status = False
    if status:
        print("port {} is open".format(PORT))
start_time = time.time()
  
for i in range(0, 100000):
    thread = threading.Thread(target=PortScan, args=[i])
    thread.start()

end_time = time.time()
print("To scan all ports it took {} seconds".format(end_time-start_time))