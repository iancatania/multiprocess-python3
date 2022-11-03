import socket
import argparse
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
client.connect((host, port))

parser = argparse.ArgumentParser()
parser.add_argument('--UID', type=str, required=True)
parser.add_argument('--File', type=str, required=True)
parser.add_argument('--Data', type=str, required=False)

args = parser.parse_args()

with open(args.Data, 'r') as read:
    data = read.read()

dict = {

    "UID": args.UID,
    "File": args.File,
    "Data": data
}

data = json.dumps(dict)

res = client.recv(4096)
client.send(data.encode())
client.close()
print(res.decode('UTF-8'))
