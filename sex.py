import discord
from discord import webhook
from discord.ext import commands
from colorama import Fore, init
import ctypes
import time
import subprocess
import os
import threading
import sys
import requests

init(autoreset=True)
green = Fore.LIGHTGREEN_EX
white = Fore.RESET
red = Fore.LIGHTRED_EX
yellow = Fore.YELLOW
blue = Fore.LIGHTCYAN_EX
dblue = Fore.CYAN
gray = Fore.LIGHTBLACK_EX

def get_base_prefix_compat():
    return getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None) or sys.prefix

def in_virtualenv(): 
    return get_base_prefix_compat() != sys.prefix

if in_virtualenv() == True: 
    sys.exit() 

def title(content):
    ctypes.windll.kernel32.SetConsoleTitleW(content)
headers = { 
    "Content-Type": "application/json", 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

cwd = os.getcwd()

def openbb(c):
    subprocess.call(f'{c}', creationflags=subprocess.CREATE_NEW_CONSOLE)

while True:
    title("[imperion] [Beta 1.2] Menu")
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
{dblue}                             ╔═════════════════════════════╦════════════════════════════╗
{dblue}                             ║ {gray}[{green}1{gray}] {white}Nuker                   {dblue}║ {gray}[{green}2{gray}] {white}WebHook Deleter        {dblue}║
{dblue}                             ║ {gray}[{green}3{gray}] {white}Nitro Gen & Checker     {dblue}║ {gray}[{green}4{gray}] {white}SelfBot                {dblue}║
{dblue}                             ╚═════════════════════════════╩════════════════════════════╝
""")

    print(f"\n\n\n{blue}      >> {white}", end='')
    try:
        choice = int(input())
    except:
        print(f"\n                                                 {gray}[{red}!{gray}]{white} Invalid Choice.")
        time.sleep(5)
    else:
        if choice == 1:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading Nuker...")
            time.sleep(0.7)
            try:
             mydir = cwd + "\\Modules"
             mydir_new = os.chdir(mydir)
             threading.Thread(target=openbb, args=(f'{cwd}\\Modules\\Nuker.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        elif choice == 2:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading webhook deleter...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\Modules"
                os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\\Modules\\hookdel.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        elif choice == 3:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading Nitro Gen...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\Modules"
                mydir_new = os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\\Modules\\Gen.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        elif choice == 4:
            print(f"                                                 {gray}[{yellow}/{gray}]{white} Loading SelfBot...")
            time.sleep(0.7)
            try:
                mydir = cwd + "\\Modules"
                mydir_new = os.chdir(mydir)
                threading.Thread(target=openbb, args=(f'{cwd}\\Modules\\Selfbot.exe',)).start()
            except:
                print(f"                                                {gray}[{red}!{gray}]{white} Error finding Module.")
        else:
            print(f"                                                   {gray}[{red}!{gray}]{white} Invalid Choice.")

                  
        