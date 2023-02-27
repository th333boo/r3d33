#!/usr/bin/env python3
# coding: utf-8
import threading

print('### [ WEB SERVER ] ###')
from server.webserver import TB_HTTPServer
def WebStarter():
    while True:
        web = TB_HTTPServer()
        t1 = threading.Thread(target=web.do_GET)
        t1.start()
print(TB_HTTPServer())

print('### [ WEB SOCKET ] ###')
from server.websocket import TB_WebSocket
TB_WebSocket()
print(TB_WebSocket())

print('### [ SECURE SOCKET ] ###')
from server.ios import IO_SecureSocket
IO_SecureSocket()
print(IO_SecureSocket())