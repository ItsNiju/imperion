import time
import os
from colorama import Fore, init
import requests
import ctypes

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def title(content):
    try: ctypes.windll.kernel32.SetConsoleTitleW(content)
    except: pass

cls()
title("[imperion] Webhook Deleter")
webhook = input(f"""Enter the webhook url {blue}>> {white}""")

def delete():
    requests.delete(webhook)
    ok = requests.get(webhook)
    if ok.status_code == 404:
        print(f"""{green}\n Deleted""")
        time.sleep(5)
    elif ok.status_code == 200:
        print(f"""{red}\n Failed""")
        time.sleep(5)

sus = requests.get(webhook)
if sus.status_code == 404:
    print("\n")
elif sus.status_code == 200:
    print("\n")
    delete()