import threading
import time
import socket
import subprocess
from datetime import datetime



HOST = '127.0.0.1'    # The remote host
PORT = 8080              # The same port as used by the server
FQDN = "localhost"
IDENTIFIER_STRING = ".pineapple."
data = "Hi world"


def send(data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            sock.send(data)
            now = datetime.now()
            print(f"Sent {data} to {HOST} at time " + now.strftime("%H:%M:%S"))
        pass
    except ConnectionRefusedError as e:
        print("CONREFUSED: ",e,"RECONNECTING IN (2) SECONDS")
        time.sleep(2)
        send(data)

def tunnel(data):
    target = str(data)+ IDENTIFIER_STRING + FQDN
    print(target)
    output = subprocess.call(['nslookup', target],stdout=subprocess.DEVNULL)
    print("sent ",data," to ",target)
