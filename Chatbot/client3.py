import tkinter
import socket
from tkinter import *
from threading import Thread


def receive():
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except:
            print("There is an error receiving the message)")


def send():
    msg = my_msg.get()
    my_msg.set("")
    s.send(bytes(msg, "utf8"))
    if msg == "#quit":
        s.close()
        window.close()


def on_closing():
    my_msg.set("#quit")
    send()


window = Tk()  # Everything between this line and mainloop() will be executed in the window
window.title("Chat Room Application")
window.configure(bg="green")

msg_frame = Frame(window, height=100, width=100, bg='red')
msg_frame.pack()

my_msg = StringVar()
my_msg.set("")

scroll_bar = Scrollbar(msg_frame)
msg_list = Listbox(msg_frame, height=50, width=100, bg='red', yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()

label = Label(window, text="Enter the Message", fg='blue', font='Aerial', bg='red')
label.pack()

entry_field = Entry(window, textvariable=my_msg, fg='red', width=50)
entry_field.pack()

send_button = Button(window, text="Send", font="Aerial", fg='white', command=send)
send_button.pack()

quit_button = Button(window, text="Quit", font="Aerial", fg='white', command=on_closing)
quit_button.pack()

Host = '127.0.0.1'
Port = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Host, Port))

receive_Thread = Thread(target=receive)
receive_Thread.start()
mainloop()
