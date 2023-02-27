import socket
import threading 

HOST,PORT = "127.0.0.1",3333

print(f"Running the server on: {HOST} and port: {PORT}")

io = socket.socket()
io.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try: 
	io.bind((HOST, PORT))
	io.listen(5)
except Exception as e:
	raise SystemExit(f"We could not bind the server on host: {HOST} to port: {PORT}, because: {e}")


def on_new_client(client, connection):
	ip = connection[0]
	port = connection[1]
	print(f"THe new connection was made from IP: {ip}, and port: {port}!")
	while True:
		msg = client.recv(1024)
		if msg.decode() == 'exit':
			break
		print(f"The client said: {msg.decode()}")
		reply = f"You told me: {msg.decode()}"
		client.sendall(reply.encode('utf-8'))
	print(f"The client from ip: {ip}, and port: {port}, has gracefully diconnected!")
	client.close()

while True:
	try: 
		client, ip = io.accept()
		threading._start_new_thread(on_new_client,(client, ip))
	except KeyboardInterrupt:
		print(f"Gracefully shutting down the server!")
	except Exception as e:
		print(f"Well I did not anticipate this: {e}")


