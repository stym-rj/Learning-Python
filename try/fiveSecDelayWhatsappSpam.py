from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
time.sleep(5)
while True:
    char = "."
    keyboard.type(char)
    keyboard.press(Key.enter)
    time.sleep(0.1)