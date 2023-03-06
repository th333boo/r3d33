#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
HOST,PORT = "127.0.0.1",443
FORMAT = "utf-8"
PAYLOAD=''

class TB_SSLWraper():
    import ssl
    httpd = HTTPServer((HOST,PORT), BaseHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, 
            keyfile="", 
            certfile='', server_side=True)
    httpd.serve_forever()

class TB_HTTPServer(BaseHTTPRequestHandler):
    pass
TB_HTTPServer()

#     def do_GET(self):
#         if self.path == '/':
#             self.path = '/static/index.html'
#         try:
#             file_to_open = open(self.path[1:]).read()
#             self.send_response(200)
#             self.send_header("Content-Type", "text/html")
#             self.end_headers()
#         except:
#             file_to_open = 'Not found'
#             self.send_response(404)
#         self.wfile.write(bytes(file_to_open,FORMAT))

#     def do_POST(self):
#         self.send_response(200)
#         self.send_header("Content-Type", "text/html")
#         self.end_headers()
# try:
#     webserver = HTTPServer((HOST, PORT),TB_HTTPServer)
#     webserver.serve_forever()
# except Exception as e:
#     print(e)
#     webserver.socket.close()