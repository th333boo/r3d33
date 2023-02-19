#!/usr/bin/env python3
# coding: utf-8

from decouple import config
import socket 

HOST = str(config("HOST"))
PORT = int(config("PORT"))
PORTC = int(config("PORT"))
class SocketServerInfo:
	@staticmethod
	def __init__(self,HOST,PORT):
		self._HOST = HOST
		self._PORT = PORT

	def run(self):
		print("### [ SOCKET running ] ###")
		print("Server socket is running on IP {} and PORT {} congratulation {}".format(self.HOST,self.PORT))

class SocketClientInfo:
	@staticmethod
	def __init__(self,PORTC):
		PORTC = 3338
		self._HOST = HOST
		self._PORTC = PORTC
print("Your IP is {} and PORT is {}".format(HOST,PORTC))

class SocketServerConnect(SocketServerInfo):
	def __init__(self):	
		SocketServerInfo.__init__(self,HOST,PORT)
		io = socket.socket()
		io.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		print("### [ SOCKET Server is running ] ###")


print("Your IP is {} and PORT is {}".format(HOST,PORT))

print('### [ SOCKET running ] ###') 