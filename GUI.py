from tkinter import *
import discord
import requests
import time
from colorama import Fore, init
import ctypes

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

root = Tk()
root.title("[imperion] [Beta 1.7] Menu")

ok = Label(root, text="Hello!")
ok.pack()

def myClick():
    requests.delete(webhook)
    ok = requests.get(webhook)
    if ok.status_code == 404:
        print(f"""{green}\n Deleted""")
        time.sleep(5)
    elif ok.status_code == 200:
        print(f"""{red}\n Failed""")
        time.sleep(5)

delete = Button(root, text="Delete Webhook")
delete.pack()

root.mainloop()