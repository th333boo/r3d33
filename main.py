#!/usr/bin/env python3
# from io.webserver import TB_HTTPServer
from kit.public_ip import PUBLIC_IP
from kit.network_card import NetCard
from kit.footprint_custom import FootPrint
# from tor.th333boo_trail import th333booTRAIL
# from tor.th333booTOR import 
# from .io.websocket import *
# from .io.database import *
# from .bot.telegrambot import *
# from .bot.spambot import *

print('### [ WEB SERVER ] ###')
# TB_HTTPServer() 

print('### [ PUBLIC IP ] ###')
print(PUBLIC_IP())

print('### [ NETWORK CARD AVAILABLE ] ###')
print(NetCard())

print('### [ FOOTPRINT CLEANER ] ###')
print(FootPrint().FootPrintClean())
# FootPrint().FootPrintClean()

print('### [ th333boo trail TUNNEL CREATED ] ###')

print('### [ TOR TUNNEL CREATED ] ###')
# th333booTRAIL()
# Create_TUNTOR().th333booTRAILrunner()
