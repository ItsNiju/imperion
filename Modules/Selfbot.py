import os
from sys import prefix
import sys
import discord
from discord.ext import commands
from discord import Embed 
import asyncio 
import logging
import random 
from colorama import init
from colorama import Fore, Style
import requests
import json
import datetime
import random
import threading
import random
import time
import threading
import ctypes
import math
import subprocess

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
    ctypes.windll.kernel32.SetConsoleTitleW(content)
headers = { 
    "Content-Type": "application/json", 
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
}

def openbb(c):
    subprocess.call(f'{c}', creationflags=subprocess.CREATE_NEW_CONSOLE)

token = input(f"""\nToken >>  """)
client = commands.Bot(command_prefix="$", case_insensitive=True,
                      self_bot=True)

header = {"Authorization": f'Bot {token}'}
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

intents = discord.Intents.all()
intents.members = True

@client.event
async def on_ready():
    title("[imperion] Selfbot")
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
{dblue}                             ║ {gray}[{green}${gray}] {white}(add/sub/mul/div)       {dblue}║ {gray}[{green}${gray}] {white}destruct               {dblue}║
{dblue}                             ║ {gray}[{green}${gray}] {white}utc                     {dblue}║ {gray}[{green}${gray}] {white}clone                  {dblue}║
{dblue}                             ║ {gray}[{green}${gray}] {white}nick                    {dblue}║ {gray}[{green}${gray}] {white}cmds                   {dblue}║
{dblue}                             ╚═════════════════════════════╩════════════════════════════╝
""")
    print(f"""{green}     - Logged in as {blue}""" + client.user.name + f"""#""" + client.user.discriminator)


@client.command()
async def clone(ctx): 
    await ctx.message.delete()
    wow = await client.create_guild(f'clone-of-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'clone-of{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await wow.create_role(name=role.name, color=role.color, permissions=role.permissions, hoist=role.hoist, mentionable=role.mentionable)
            except:
                break

@client.command()
async def utc(ctx):
    await ctx.message.delete()
    embed = Embed(title="UTC Time now", description=datetime.datetime.utcnow(), color=0x00F1BA)
    await ctx.send(embed=embed)

@client.command()
async def add(ctx, *nums):
    operation = " + ".join(nums)
    embed = Embed(title="Addition result", description = f'{eval(operation)}', color=0x00F1BA)
    await ctx.send(embed=embed)

@client.command()
async def sub(ctx, *nums):
    operation = " - ".join(nums)
    embed = Embed(title="subtraction result", description = f'{eval(operation)}', color=0x00F1BA)
    await ctx.send(embed=embed)

@client.command()
async def mul(ctx, *nums):
    operation = " * ".join(nums)
    embed = Embed(title="Multiplication result", description = f'{eval(operation)}', color=0x00F1BA)
    await ctx.send(embed=embed)

@client.command()
async def div(ctx, *nums):
    operation = " * ".join(nums)
    embed = Embed(title="Divition result", description = f'{eval(operation)}', color=0x00F1BA)
    await ctx.send(embed=embed)

@client.command()
async def destruct(ctx):
    await ctx.message.delete()
    embed = Embed(title="Destructed", color=0x00F1BA)
    await ctx.send(embed=embed)
    sys.exit()

@client.command()
async def nick(ctx, *, txt=None):
        await ctx.message.delete()
        await ctx.message.author.edit(nick=txt)
        embed = Embed(description='Changed nickname to: `%s`' % txt, color=0x00F1BA)
        await ctx.send(embed=embed)

@client.command()
async def clear(ctx):
    await ctx.message.delete()
    os.system('cls' if os.name == 'nt' else 'clear')
    title("[imperion] Selfbot")
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
{dblue}                             ║ {gray}[{green}${gray}] {white}(add/sub/mul/div)       {dblue}║ {gray}[{green}${gray}] {white}destruct               {dblue}║
{dblue}                             ║ {gray}[{green}${gray}] {white}clear(clears console    {dblue}║ {gray}[{green}${gray}] {white}clone                  {dblue}║
{dblue}                             ║ {gray}[{green}${gray}] {white}nick                    {dblue}║ {gray}[{green}${gray}] {white}cmds                   {dblue}║
{dblue}                             ╚═════════════════════════════╩════════════════════════════╝
""")
    print(f"""{green}     - Logged in as {blue}""" + client.user.name + f"""#""" + client.user.discriminator)   

@client.command()
async def cmds(ctx):
    await ctx.message.delete()

@client.command()
async def define(ctx,*,txt=None):
    await ctx

@client.command()
async def vape(ctx):
    await ctx.send("buy vape @ https://vape.gg/")

@client.command()
async def gayrate(ctx):
    

@client.command()
async def waifu(ctx):
    r = requests.get('https://nekos.life/api/v2/img/waifu')
    res = r.json()
    em = discord.Embed()
    em.set_image(url=(res['url']))
    await ctx.send(embed=em)

client.run(token, bot=False)