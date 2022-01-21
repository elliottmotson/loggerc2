import socketserver
from pathlib import Path
from datetime import datetime
import os
import base64

class clientcon(socketserver.StreamRequestHandler):
    def handle(self):
        now = datetime.now()
        time = str(now.strftime("%H:%M:%S"))
        data = decrypt(self.rfile.readline().strip())
        user = self.client_address[0]
        print("Recieved one request from {}".format(self.client_address[0])," @ ", time)
        savedata(data,user)
        return

    def send(data):
        self.wfile.write(data.encode())
        print(f"Sent {data} to client")


class server():

    def svr_start(host,port):
        aServer = socketserver.TCPServer((host, port), clientcon)
        print(f"Listening at {host} on port {port}")
        aServer.serve_forever()


def init():
    host = "127.0.0.1"
    port = 8080
    C2NAME = "Elliott's awesome C2 server"
    print(f"Starting {C2NAME}")

    server.svr_start(host,port)

def savedata(data,user):
    if data is not None:
        print(f"Received: {data}")
        f = open(Path(f'./{user.replace(".","")}.log'), "a")
        f.write(data)
        f.close()

def decrypt(data):
    print(f"Decrypting {data}")
    data = base64.b64decode(data)
    data = data.decode("utf-8")
    print(data)
    return data


init()
