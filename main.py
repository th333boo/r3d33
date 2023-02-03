#!/usr/bin/env python3
from kit.public_ip import PUBLIC_IP
from io.webserver import TB_HTTPServer
from tor.tor import Create_TUNTOR()
# from tor.th333booTOR import 
# from .io.websocket import *
# from .io.database import *
# from .bot.telegrambot import *
# from .bot.spambot import *

PUBLIC_IP()
TB_HTTPServer()
Create_TUNTOR()
######################################
print('### [ DNS TAKEOVER ] ###')

######################################
print('### [ ALL NETWORK TAKEOVER ] ###')