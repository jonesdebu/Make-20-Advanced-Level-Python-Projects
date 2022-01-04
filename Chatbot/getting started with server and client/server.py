import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # TODO: change to SOCK_DGRAM to test UDP
sock.bind((host, port))     # bind host and port to socket

sock.listen(1)  # listen to 1 request at one time
print("The server is running and is listening to client request\n")

conn, address = sock.accept()   # returns the connection socket and the address of the client

message = "Hello World"

conn.send(message.encode())

conn.close()
