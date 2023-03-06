#!/usr/bin/env python3
# coding: utf-8
import threading

print('### [ PUBLIC_IP ] ###')
from kit.public_ip import TB_PUBLIC_IP
print(TB_PUBLIC_IP())

print('### [ FOOTPRINT CUSTOM ] ###')
from kit.footprint_custom import TB_FootPrintCustom
print(TB_FootPrintCustom())

print('### [ SCANNER ] ###')
from kit.scanner import TB_Scanner
print(TB_Scanner())

print('### [ NETWORK CARD ] ###')
from kit.network_card import TB_NetCard
print(TB_NetCard())

print('### [ WEB SOCKET ] ###')
from server.websocket import TB_WebSocket
TB_WebSocket()
print(TB_WebSocket())

print('### [ WEB SERVER ] ###')
from io.webserver import TB_HTTPServer
print(TB_HTTPServer())

print('### [ TRACEROUTE ] ###')
from kit.traceroute_takeover import TB_TraceRoute
print(TB_TraceRoute())

print('### [ DATABASE CONNEXION ] ###')
from io.database import TB_Scanner
print(TB_Scanner())



# print('### [ SECURE SOCKET ] ###')
# from server.ios import IO_SecureSocket
# IO_SecureSocket()
# print(IO_SecureSocket())