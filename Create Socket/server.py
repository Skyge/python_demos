#version1.2
#-*- coding:utf-8 -*-  
  
from socket import *  

import select  
import sys  
  
HOST = ''  
PORT = 21567  
BUFSIZ = 1024  
ADDR = (HOST, PORT)  
  
tcpSerSock = socket(AF_INET, SOCK_STREAM)  
tcpSerSock.bind(ADDR)  
tcpSerSock.listen(5)  
inputlist = [tcpSerSock, sys.stdin]      
  
while True:  
    print ('waiting for connection...')  
    tcpCliSock, addr = tcpSerSock.accept()  
    print ('...connected from:',addr)  
    inputlist.append(tcpCliSock)      
    while True:  
        readyInput, readyOutput, readyException = select.select(inputlist,[],[])    
        for indata in readyInput:  
            if indata==tcpCliSock:     
                data = tcpCliSock.recv(BUFSIZ).decode()   
                if data=='':  
                    inputlist.remove(tcpCliSock)  
                    break
                print('\033[1;33;40m')
                print (data)
                print('\033[0m')
            else:               
                data = input('> ')  
                if data=='':    
                    inputlist.remove(tcpCliSock)  
                    break  
                tcpCliSock.send(data.encode())  
        if data=='':  
            break  
    tcpCliSock.close()  
tcpSerSock.close()  
