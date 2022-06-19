"""
chat server

"""
import socket
import os
import threading

sockListen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockListen.bind(('', 50008))
sockListen.listen()

clients = []

def handleSock(sockConn, addr):
    try:
        while True:
            data =sockConn.recv(1024)
            if not data:
                break
            for sock in clients:
                try:
                    sock.send(('[%s]: %s' % (addr, data.decode('utf-8'))).encode('utf-8'))
                except Exception as e:
                    print("sending failed.", e)
    except Exception as e:
        print(e)
    finally:
        clients.remove(sockConn)
        sockConn.close()

while True:
    try:
        sockConn, address = sockListen.accept()
        print('Server connected by', address)
        clients.append(sockConn)
        threading.Thread(target=handleSock, args=(sockConn, address)).start()

    except Exception as e:
        print(e)
