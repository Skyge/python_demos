#-*- coding:utf-8 -*-
#version1.3

from socket import *

import threading

HOST = "localhost"
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

  
def rec(tcpCliSock): 
    while True:  
        data = tcpCliSock.recv(1024).decode()
        if data == "exit":  
            break  
        print('From Server:', data)  
chat = threading.Thread(target=rec, args=(tcpCliSock, ))  
chat.start()  
while True:  
    data = input(">") 
    if data == "exit":  
        break
    tcpCliSock.send(data.encode())

tcpCliSock.close()
