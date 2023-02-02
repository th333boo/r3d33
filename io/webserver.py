#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
HOST,PORT = "127.0.0.1",3339
FORMAT = "utf-8"


class bbiHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("""Hello World""",FORMAT))
try:
    webserver = HTTPServer((HOST, PORT),bbiHTTPServer)
    webserver.serve_forever()
except Exception as e:
    print(e)
    webserver.socket.close()
bbiHTTPServer()