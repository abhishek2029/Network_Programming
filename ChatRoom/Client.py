#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#a simple python program for server-client communication. 
#The user first runs the server program. 

#importing library

import socket


# In[ ]:


#enter the IP address here and we have taken a predefined port number of 8080. 

s = socket.socket()
host = input(str('host IP : '))
port = 8080


# In[ ]:


s.connect((host, port))
print('Connected to chat server')
while 1:
    incoming_message = s.recv(1024)
    incoming_message = incoming_message.decode()
    print(' Server : ', incoming_message)
    print()
    message = input(str('>> '))
    message = message.encode()
    s.send(message)
    print('Sent')
    print()

