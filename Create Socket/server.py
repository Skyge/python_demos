#-*- coding:utf-8 -*-
#version1.3

from socket import *

import threading

HOST = ""
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(4)


print("waiting for connection...")
tcpCliSock, addr = tcpSerSock.accept()
print("...connected from:", addr)

    
def rec(tcpCliSock):    
    while True:  
        data = tcpCliSock.recv(1024).decode()
        if data == "exit":  
            break  
        print('From Client:', data)  
chat = threading.Thread(target=rec, args=(tcpCliSock, ))  
chat.start()  
while True:  
    data = input(">") 
    if data == "exit":  
        break
    tcpCliSock.send(data.encode())

tcpCliSock.close()  
