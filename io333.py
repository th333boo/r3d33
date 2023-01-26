#!/usr/bin/env python3
import socket
HOST,PORT = "127.0.0.1",3338

io = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
io.bind((HOST,PORT))