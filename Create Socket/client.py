#-*- coding:utf-8 -*-
#version1.0

from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    data_to = input('To Server: ')
    if not data_to:
        break
    tcpCliSock.send(data_to.encode())
    
    data_from = tcpCliSock.recv(BUFSIZ).decode()
    if not data_from:
        break
    print('From Server: ',data_from)

tcpCliSock.close()
