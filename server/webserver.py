#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
from server.websocket import TB_WebSocket

HOST,PORT = "127.0.0.1",3339
FORMAT = "utf-8"
PAYLOAD=''

class TB_HTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/static/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
        except Exception as e:
            print(e)
            file_to_open = '404 NOT FOUND !'
            self.send_response(404)
            TB_WebSocket()
            self.wfile.write(bytes(file_to_open,FORMAT))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
try:
    webserver = HTTPServer((HOST, PORT),TB_HTTPServer)
    webserver.serve_forever()
except Exception as e:
    print(e)
    webserver.socket.close()

TB_HTTPServer().do_GET()
TB_HTTPServer().do_POST()