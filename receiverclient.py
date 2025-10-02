import socket
import atexit
import pyautogui

def run():
    s = socket.socket()

    port = 45238


    s.connect((input("IP Address:\n"),port))
    print("connected")

    def cleanup():
        s.close()
    atexit.register(cleanup)

    s.send("receiver".encode())
    print("setup complete")



    while True:
        data = s.recv(1024).decode()
        print("received: "+data)
        split = data.split(",")
        pyautogui.moveTo(int(split[0]), int(split[1]), duration=10)



