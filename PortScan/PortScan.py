#!/usr/bin/env python
# coding: utf-8

# In[1]:


#simple port scanner

#importing library

import socket
import time
import threading
from queue import Queue


# In[ ]:


socket.setdefaulttimeout(0.25)
lock = threading.Lock()


# In[ ]:


#enter your ip address to scan the open ports

ip_address = input('IP Address: ')
host = socket.gethostbyname(ip_address)
print ('Scanning on IP Address: ', host)


# In[ ]:


#scan the port and print which port is open

def scan(port):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = sock.connect((host, port))
      with lock:
         print(port, 'is open')
      con.close()
   except:
    pass


# In[ ]:


def execute():
   while True:
      worker = queue.get()
      scan(worker)
      queue.task_done()


# In[ ]:


queue = Queue()
start_time = time.time()


# In[ ]:


for x in range(100):
   thread = threading.Thread(target = execute)
   thread.daemon = True
   thread.start()


# In[ ]:


for worker in range(1, 500):
   queue.put(worker)


# In[ ]:


queue.join()


# In[ ]:


print('Time taken:', time.time() - start_time)

