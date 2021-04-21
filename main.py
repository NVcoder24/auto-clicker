print("Please wait!")
from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
from threading import Thread
from time import sleep
from config import cfg

is_hold = False

def press_key():
    global is_hold
    mouse = Controller()
    while True:
        if is_hold:
            mouse.click(cfg["btn_press"], 1)
            sleep(cfg["delay"])

def press(key):
    global is_hold

    if key == cfg["button"]:
        is_hold=True

    if key == Key.delete:
        quit()

def release(key):
    global is_hold

    if key == cfg["button"]:
        is_hold = False

def listener_():
    with Listener(on_press=press, on_release=release) as listener:
        listener.join()

Thread(target=listener_).start()
Thread(target=press_key).start()
print("Auto clicker started!")
