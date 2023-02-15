#!/usr/bin/env python3

from server.ios import IO_SecureSocket
print('### [ WEB SERVER ] ###')
IO_SecureSocket()
print(IO_SecureSocket())

from server.webserver import TB_HTTPServer
print('### [ WEB SERVER ] ###')
TB_HTTPServer()
print(TB_HTTPServer())

from server.websocket import TB_WebSocket
print('### [ WEB SOCKET ] ###')
TB_WebSocket()
print(TB_WebSocket())

from kit.public_ip import PUBLIC_IP
print('### [ PUBLIC IP ] ###')
print(PUBLIC_IP())

from kit.network_card import NetCard
print('### [ NETWORK CARD AVAILABLE ] ###')
print(NetCard())

from kit.footprint_custom import FootPrint
print('### [ FOOTPRINT CLEANER ] ###')
# print(FootPrint().FootPrintClean())
# FootPrint().FootPrintClean()

# from tor.th333boo_trail import th333booTRAIL
print('### [ th333boo trail TUNNEL CREATED ] ###')

# from tor.th333booTOR import 
print('### [ TOR TUNNEL CREATED ] ###')
# th333booTRAIL()
# Create_TUNTOR().th333booTRAILrunner()

# from .io.database import *
# from .bot.telegrambot import *
# from .bot.spambot import *




