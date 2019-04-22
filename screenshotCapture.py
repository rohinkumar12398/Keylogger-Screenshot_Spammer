#!/usr/bin/env python3

#Import Necessary Libraries
from pynput import keyboard
from pynput.keyboard import Key, Controller
from pynput import mouse

#Setup The Keyboard Controller
keyboard = Controller()

#Definition For Click Function (Takes A Screenshot Everytime A Click Occurs)
def on_click(x, y, button, pressed):
    keyboard.press(Key.shift)
    keyboard.press(Key.cmd)
    keyboard.press('3')
    keyboard.release(Key.shift)
    keyboard.release(Key.cmd)
    keyboard.release('3')

#Function For Key Press (Screenshot Capture Can Be Terminated Using 'esc' Key)
def on_press(key):
    if str(key) == 'Key.esc':
        print('Terminated')
        return False

#Configure The Listener
with mouse.Listener(on_click = on_click, on_press = on_press) as listener:
    listener.join()
