#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
from OpenSSL import crypto, SSL
import ssl
HOST,PORT = "127.0.0.1",443
FORMAT = "utf-8"
PAYLOAD=''

class TB_SSLWraper():
    

    def cert_gen(
        emailAddress="contact@th333boo.com",
        commonName="th333boo",
        countryName="FR",
        localityName="Marseille",
        stateOrProvinceName="PACA",
        organizationName="BBI WEBSEC",
        organizationUnitName="BBI WEBSEC",
        serialNumber=0,
        validityStartInSeconds=0,
        validityEndInSeconds=10*365*24*60*60,
        KEY_FILE = "private.key",
        CERT_FILE="selfsigned.crt"):
        #can look at generated file using openssl:
        #openssl x509 -inform pem -in selfsigned.crt -noout -text
        # create a key pair
        k = crypto.PKey()
        k.generate_key(crypto.TYPE_RSA, 4096)
        # create a self-signed cert
        cert = crypto.X509()
        cert.get_subject().C = countryName
        cert.get_subject().ST = stateOrProvinceName
        cert.get_subject().L = localityName
        cert.get_subject().O = organizationName
        cert.get_subject().OU = organizationUnitName
        cert.get_subject().CN = commonName
        cert.get_subject().emailAddress = emailAddress
        cert.set_serial_number(serialNumber)
        cert.gmtime_adj_notBefore(0)
        cert.gmtime_adj_notAfter(validityEndInSeconds)
        cert.set_issuer(cert.get_subject())
        cert.set_pubkey(k)
        cert.sign(k, 'sha512')
        with open(CERT_FILE, "wt") as f:
            f.write(crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode("utf-8"))
        with open(KEY_FILE, "wt") as f:
            f.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, k).decode("utf-8"))

    cert_gen()
    httpd = HTTPServer((HOST,PORT), BaseHTTPRequestHandler)
    httpd.socket = ssl.wrap_socket (httpd.socket, 
            keyfile="", 
            certfile='', server_side=True)
    httpd.serve_forever()

class TB_HTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/static/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
        except:
            file_to_open = 'Not found'
            self.send_response(404)
        self.wfile.write(bytes(file_to_open,FORMAT))
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