import os
import subprocess
import multiprocessing as mp
import numpy as np
import socket
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
server.bind((host, port))
server.listen(10)

x = 0
while True:
    client, addr = server.accept()
    x += 1
    print('Servicing client at %s' % addr[0])
    res = 'You have connected to %s, please stand by...' % host
    client.send(res.encode('UTF-8'))

    # receive data from client side
    data = client.recv(1024)
    data = json.loads(data) # loads data into .json from encoded string

    # check if directory exists with name of provided UID
    if not os.path.exists(f"./{data['UID']}"):
        os.mkdir(data['UID']) # if not, make directory

    write = open(f"{data['File']}", "w") # write to file with name provided
    write.write(f"{data['Data']}") # write data to file

    print(data)  # debug

    client.close()
server.close()
