#!/usr/bin/env python3
from http.server import HTTPServer,BaseHTTPRequestHandler
HOST,PORT = "127.0.0.1",3339
FORMAT = "utf-8"

class bbiHTTPServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("""<!doctype html>
<html>

<head>
    <title>🔒 Access Denied 🔒 - Restricted Zone</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="Description" content="You are Trying To Access To A Restricted Zone">
    <meta name="Content-Language" content="en">
    <meta name="Copyright" content="th333boo">
    <meta name="Author" content="th333boo">
    <meta name="Robots" content="all">
    <meta name="Rating" content="general">
    <meta name="Distribution" content="global">
    <meta property="og:image" content="mask.gif">
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link rel="sitemap" type="application/xml" title="Sitemap" href="/sitemap.xml">
    <link href="https://fonts.googleapis.com/css?family=Share+Tech+Mono" rel="stylesheet" type="text/css">

    <style type="text/css">
        body,
        td,
        th {
            font-family: Source Code Pro, Courier New, Courier, monospace;
            font-weight: 500;
            font-size: 100%;
            text-align: center;
            background-color: #000;
            color: #fff;
        }

        .center {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            grid-template-rows: repeat(1, 1fr);
            grid-column-gap: 10px;
            grid-row-gap: 20px;
            margin-top: 10%;
        }

        .gif_img {
            grid-area: 2 / 2 / 3 / 3;
        }

        footer {
            margin-top: 30px;
            bottom: 15px;
            right: 15px;
            left: 15px;
            z-index: 20;
        }

        footer .footer-links {
            text-align: center;
        }

        footer .footer-links a,
        footer .footer-links span {
            cursor: pointer;
            color: #666;
            font-size: 7px;
            margin-right: 6px;
        }

        footer .footer-links a:hover,
        footer .footer-links span:hover {
            color: #fff;
        }

        footer {
            margin-top: 3px;
            text-align: center;
            color: #555;
            font-size: 7px;
        }

        footer :hover {
            color: #fff;
        }

        p.large {
            font-size: 20px;
            color: #00ff00;
            font-weight: bold;
            text-transform: uppercase;
        }

        @media screen and (min-width: 32em) {
            footer {
                text-align: center;
            }

            footer .footer-links,
            footer {
                display: inline-block;
            }

            footer .footer-links span a,
            footer {
                font-size: 10px
            }

            footer:before {
                content: '';
                height: 32px;
                left: 0;
                right: 0;
                top: 0;
                z-index: -1;
            }
        }

        @media screen and (min-width: 64em) {
            footer {
                float: right;
            }
        }

        @media screen and (min-width: 1200px) {
            .center {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(1, 1fr);
                grid-column-gap: 10px;
                grid-row-gap: 50px;
                margin-top: 3%;
            }

            p.large {
                font-size: 20px;
                color: #00ff00;
                font-weight: bold;
                text-transform: uppercase;
            }
        }

        @media screen and (max-width: 530px) {
            .center {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(1, 1fr);
                grid-column-gap: 10px;
                grid-row-gap: 50px;
                margin-top: 15%;
            }

            p.large {
                font-size: 20px;
                color: #00ff00;
                font-weight: bold;
                text-transform: uppercase;
            }
        }
    </style>
</head>

<body>
    <div class="center">
        <div class="gif_img">
            <img src="mask.gif" style="max-width:330px; " border="0" />
            <p class="large">🔒 Access Denied 🔒</br> Restricted Zone</p>
            <footer>
                <div class="footer-links">
                    <span><a href="#" target="_blank"></a></span>
                    <span><a href="#" target="_blank"><a></span>
                </div>
            </footer>
        </div>
    </div>
</body>

</html>""",FORMAT))
try:
    server = HTTPServer((HOST, PORT),bbiHTTPServer)
    server.serve_forever()
except Exception as e:
    print(e)
    server.socket.close()
bbiHTTPServer()