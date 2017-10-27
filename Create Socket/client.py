#-*- coding:utf-8 -*-
 
from socket import *  

import select  
import sys  
  
HOST = 'localhost'  
PORT = 21567  
BUFSIZ = 1024  
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)  
tcpCliSock.connect(ADDR)  
inputlist = [tcpCliSock, sys.stdin]  
  
while True:  
    readyInput,readyOutput,readyException = select.select(inputlist,[],[])  
    for indata in readyInput:  
        if indata==tcpCliSock:  
            data = tcpCliSock.recv(BUFSIZ).decode() 
            if data=='':  
                break
            print (data)
        else:  
            data = input('> ')  
            if data=='':      
                break  
            tcpCliSock.send(data.encode())  
    if data=='':    
        break  
tcpCliSock.close()  
