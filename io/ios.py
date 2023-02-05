import socket
from tor.th333boo_trail import th333booTRAIL

while True:
    try:
        th333booTRAIL()
    except LookupError(e):
        print(e)

# HOST= ""
# PORT=3333
# s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(HOST,PORT)


