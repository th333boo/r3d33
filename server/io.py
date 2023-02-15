import socket 

HOST,PORT = "127.0.0.1",3333

print(f"Connecting to the server: {HOST} on port: {PORT}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as io:
	try:
		io.connect((HOST, PORT))
	except Exception as e:
		raise SystemExit(f"We have failed to connect to host: {HOST} on port: {PORT}, because: {e}")

	while True:
		msg = input("Welcome aboard! ")
		io.sendall(msg.encode('utf-8'))
		if msg =='exit':
			print("Client is disconnected!")
			break
		data = io.recv(1024)
		print(f"The server's response was: {data.decode()}")