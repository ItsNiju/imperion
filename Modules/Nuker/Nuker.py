import discord
import os
import ctypes
import threading
from discord.ext import commands
import requests
from colorama import Fore, init
import yaml
import time
import random, sys
import json
init(autoreset=True)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def title(content):
    try: ctypes.windll.kernel32.SetConsoleTitleW(content)
    except: pass

purp = Fore.MAGENTA 
pink = Fore.LIGHTMAGENTA_EX 
gray = Fore.LIGHTBLACK_EX 
white = Fore.WHITE 
red = Fore.RED 
lred = Fore.LIGHTRED_EX 

cls()
title("[imperion] Nuker")
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print(f"""
{red}                                                                            
{red}                                         _                        _           
{red}                                        <_>._ _ _  ___  ___  _ _ <_> ___ ._ _ 
{red}                                        | || ' ' || . \/ ._>| '_>| |/ . \| ' |
{red}                                        |_||_|_|_||  _/\___.|_|  |_|\___/|_|_|
{red}                                                  |_|          {gray}           By Niju                         
{red}                                       
{red}                                                         
""")
print(f"{pink}>{red} $nuke to nuke and $ban for massban")
print(f"{pink}>{red} Skidded from chasa")
global config, TOKEN, PREFIX, GUILD_NAME, CHANNEL_NAMES, ROLE_NAMES, SPAM_MESSAGES, AUDIT_LOG
try:
    file = open('config.uwu', 'r+')
    with open('config.uwu') as f:
        config = file.readlines(f)
    TOKEN = config["token"]
    CHANNEL_NAMES = config["channel-names"].split(",")
    SPAM_MESSAGES = config["spam-messages"].split(",")
except Exception as e:
    print(f"{red}[!]{white} Couldn't load config.uwu. Creating now...     ")
    file.write(r'''{ 
    "token" : "token goes here",
    "channel-names" : "ok,oky",
    "role-names" : "ok,ok again",
    "spam-messages" : "@everyone,@everyone cope",
}''')
    print(f"{lred}[+]{white} Created config.uwu.")
    print(f"{red}[!]{white} Add token to the config and reboot.")
    time.sleep(3)
    sys.exit()                