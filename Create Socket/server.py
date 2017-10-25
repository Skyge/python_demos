#-*- coding:utf-8 -*-
#version1.0

from socket import *

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('...connected from:',addr)

    while True:
        data_from = tcpCliSock.recv(BUFSIZ).decode()
        print('Form Client: ',data_from)
        if not data_from:
            break
        data_to = input('To Client: ')
        tcpCliSock.send(data_to.encode())

    tcpCliSock.close()
tcpSerSock.close()
