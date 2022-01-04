import socket

host = 'localhost'
port = 8080

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))

# receive message from server
message = sock.recv(1024)

# continually receive, decode, and print the message then receive the next message
while message:
    print("Message:", message.decode())
    message = sock.recv(1024)

sock.close()