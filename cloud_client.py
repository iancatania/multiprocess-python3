import socket
import argparse
import json

# connects the client to the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
client.connect((host, port))

# parses the arguments provided by the execution of the script
parser = argparse.ArgumentParser()
parser.add_argument('--UID', type = str, required = True)
parser.add_argument('--File', type = str, required = True)
parser.add_argument('--Data', type = str, required = False)
args = parser.parse_args()

# reads from the data provided
with open(args.Data, 'r') as read:
    data = read.read()

# creates dict with keys corresponding to each parsed argument
dict = {

    "UID": args.UID,
    "File": args.File,
    "Data": data  # data was already converted to a variable during the read process
}

# dumps content of dictionary to a .json file for sending
data = json.dumps(dict)

# sends data.json to server, encoded
res = client.recv(4096)
client.send(data.encode())
client.close()
print(res.decode('UTF-8'))
