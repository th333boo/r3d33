#!/usr/bin/env python3
import threading
import socket
import time

HOST,PORTS= "127.0.0.1",3338

print("START SCANNING PORT")
def PortScan(PORT):
    try:
        io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = False
        io.connect((HOST,PORT))
        try:
            banner = io.recv(1024).decode()
            print("port {} is open with banner {}".format(PORT, banner))
        except:
            print("port {} is open ".format(PORT))
    except:
        pass    
start_time = time.time()
    
for i in range(0, 65536):
    thread = threading.Thread(target=PortScan, args=[i])
    thread.start()

end_time = time.time()
print("To scan all ports it took {} seconds".format(end_time-start_time))