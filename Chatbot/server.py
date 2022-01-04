import socket
from threading import Thread

host = '127.0.0.1'  # You can use this (localhost IP address) or just 'localhost'
port = 8080
clients = {}
addresses = {}

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))


def handle_clients(conn, address):
    name = conn.recv(1024).decode()
    welcome = "Welcome " + name + " You can type #quit if you ever want to leave the Chat Room"
    conn.send(bytes(welcome, "utf8"))

    msg = f"{name} Has recently joined the Chat Room"

    broadcast(bytes(msg, 'utf8'))
    clients[conn] = name

    while True:     # handle sending messages and submitting the quit command
        msg = conn.recv(1024)
        if msg != bytes("#quit", "utf8"):
            broadcast(msg, name+":")
        else:
            conn.send(bytes("#quit", "utf8"))
            conn.close()
            del clients[conn]
            broadcast(bytes(name + " Has Left the Chat Room", "utf8"))


def accept_client_connections():
    while True:
        client_conn, client_address = sock.accept()
        print(client_address, " Has Connected")
        client_conn.send(" Welcome to the Chat Room, Please Type your name to continue".encode('utf-8'))
        addresses[client_conn] = client_address

        Thread(target=handle_clients, args=(client_conn, client_address)).start()


def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix, "utf8")+msg)


if __name__ == "__main__":
    sock.listen(5)
    print("The server is running and is listening to client's requests")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()  # Stop execution of thread until active thread is finished executing
