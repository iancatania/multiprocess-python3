import os
import subprocess
import multiprocessing as mp
import numpy as np
import socket
import json

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
server.bind((host,port))
server.listen(10)



x = 0
while True:
    client,addr = server.accept()
    x += 1
    print('Servicing client at %s'%addr[0])
    res = 'You have connected to %s, please stand by...'%host
    client.send(res.encode('UTF-8'))
    client.send(data)
    client.close()
server.close()
