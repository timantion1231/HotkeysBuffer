import keyboard
import psutil
import os
import pyperclip
import sys
from random import randint as rnd
import win32api
import win32con
import win32event
import win32gui
from datetime import datetime
import threading
import time

doc_ptinyat = "Документы приняты, схема отрисована."
izm_vneseni = "Изменения внесены."

start_time = datetime.now()
start_time = start_time.time()


def chk_buffer():  # check if buffer is open
    for proc in psutil.process_iter():
        if proc.name() == "clipdiary.exe":  # insert "buffer" program
            return True
    return False


def buffer_operation():  # open or close buffer
    if chk_buffer():
        for proc in psutil.process_iter():
            if proc.name() == "clipdiary.exe":
                proc.kill()
                print("Closed")
                break
    else:
        os.startfile(r'C:\Program Files (x86)\Clipdiary\clipdiary.exe')
        print("Started")


def set_fence():
    rand = rnd(1, 100)
    s = f"{rand}_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-{rand}"
    pyperclip.copy(s)


try:
    keyboard.add_hotkey('Ctrl + Shift + 3', buffer_operation)
    keyboard.add_hotkey('Win + L', lambda: sys.exit(0))
    keyboard.add_hotkey('Ctrl + Shift + 1', lambda: pyperclip.copy(doc_ptinyat))
    keyboard.add_hotkey('Ctrl + Shift + 2', lambda: pyperclip.copy(izm_vneseni))
    keyboard.add_hotkey('Ctrl + Shift + 4', set_fence)

except(err):
    print("ERR: " + err)
keyboard.wait()
