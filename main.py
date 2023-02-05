#!/usr/bin/env python3
from io.webserver import TB_HTTPServer
from tor import Create_TUNTOR, th333boo_trail

from kit.public_ip import PUBLIC_IP
# from tor.th333booTOR import 
# from .io.websocket import *
# from .io.database import *
# from .bot.telegrambot import *
# from .bot.spambot import *

# print('### [ th333boo trail TUNNEL CREATED ] ###')
# th333boo_trail()
# print('### [ TOR TUNNEL CREATED ] ###')
# Create_TUNTOR()
print('### [ WEB SERVER ] ###')
TB_HTTPServer()
PUBLIC_IP()