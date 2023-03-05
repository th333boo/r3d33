#!/usr/bin/env python3
# coding: utf-8
import threading

print('### [ FOOTPRINT CUSTOM ] ###')
from kit.footprint_custom import TB_FootPrintCustom
print(TB_FootPrintCustom())

print('### [ SCANNER ] ###')
from kit.scanner import TB_Scanner
print(TB_Scanner())

print('### [ WEB SERVER ] ###')
from server.webserver import TB_HTTPServer
print(TB_HTTPServer())

print('### [ WEB SOCKET ] ###')
from server.websocket import TB_WebSocket
TB_WebSocket()
print(TB_WebSocket())

print('### [ SECURE SOCKET ] ###')
from server.ios import IO_SecureSocket
IO_SecureSocket()
print(IO_SecureSocket())