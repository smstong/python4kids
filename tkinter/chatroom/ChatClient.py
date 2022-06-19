"""
chat client
"""
import socket
import sys
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading

def thread_recv():
    while True:
        data = sock.recv(1024)
        text.insert("end", data.decode('utf-8')+"\n")

def on_send():
    try:
        sock.send(strSend.get().encode('utf-8'))
    except Exception as e:
        print(e)
    else:
        strSend.set("")

serverHost = '127.0.0.1'
serverPort = 50008

if len(sys.argv) > 1:
    serverHost = sys.argv[1]

root = tk.Tk()

# Text
text = ScrolledText(root, bg='lightblue')
text.pack(expand=tk.YES, fill=tk.BOTH)

# Entry
strSend = tk.StringVar()
ent = tk.Entry(root)
ent.pack(fill=tk.BOTH)
ent.configure(textvariable=strSend)
ent.bind('<Return>', lambda event: on_send())
strSend.set("hello")

# network
sock = socket.socket()
sock.connect((serverHost, serverPort))
threading.Thread(target=thread_recv).start()

root.mainloop()
