#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#first run the server program. 
#then run the client program and give your local IP address and connection is established. 
#import libraries

import socket


# In[ ]:


#we are setting the port number for the server to run on.
# once connected with the client, the user can communicate.

s = socket.socket()
host = socket.gethostname()
print(' Server will start on host : ', host)
port = 8080
s.bind((host, port))
print()
print('Waiting for connection')
print()
s.listen(1)
conn, addr = s.accept()
print(addr, ' Has connected to the server')
print()
while 1:
    message = input(str('>> '))
    message = message.encode()
    conn.send(message)
    print('Sent')
    print()
    incoming_message = conn.recv(1024)
    incoming_message = incoming_message.decode()
    print(' Client : ', incoming_message)
    print()

