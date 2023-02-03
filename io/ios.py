import socket
HOST= ""
PORT=3333
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(HOST,PORT)

