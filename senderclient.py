import socket
import pyautogui
import keyboard
import atexit
from time import sleep

def run():
    s = socket.socket()
    port = 45238

    s.connect((input("IP Address:\n"),port))
    print("connected")

    def cleanup():
        s.close()
    atexit.register(cleanup)

    s.send("sender".encode())

    def keypress():
        s.send((str(pyautogui.position()[0])+","+str(pyautogui.position()[1])).encode())
        print("sending"+str(pyautogui.position()[0])+","+str(pyautogui.position()[1]))

    keyboard.add_hotkey("ctrl+n", keypress)

    while True:
        sleep(0.1)