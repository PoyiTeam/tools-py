# -*- coding: utf-8 -*-
import socket
HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

#conn, addr = server.accept()
i = 1
serverMessage = f"num {i}"
while True:
    conn, addr = server.accept()
    clientMessage = str(conn.recv(1024), encoding='utf-8')
    print('Client message is:', clientMessage)
    conn.sendall(serverMessage.encode())
    i += 1
    conn.close()
