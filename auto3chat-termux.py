import discord
import subprocess as sb
import time
if discord.__version__ == '1.9.2':
    print('Atualizando discord.')
    time.sleep(1)
    sb.run(['pip', 'install', 'discord.py-self==2.0.0'])
    sb.run(['python3', 'main.py'])
    exit()
import re
import os
import asyncio
import random 
import string
import requests
from discord.ext import commands
from termcolor import colored
from unidecode import unidecode
from multiprocessing import Process
from threading import Thread


Arquivos = {
    'main.py': 'https://raw.githubusercontent.com/Kameil/autocatch3chats-termux/main/main.py',
    'bot.py': 'https://raw.githubusercontent.com/Kameil/autocatch3chats-termux/main/bot.py',
    'data/pokemon': 'https://raw.githubusercontent.com/Kameil/autocatch3chats-termux/main/data/pokemon',
    'data/legendary': 'https://raw.githubusercontent.com/Kameil/autocatch3chats-termux/main/data/legendary',
    'data/mythical': 'https://raw.githubusercontent.com/Kameil/autocatch3chats-termux/main/data/mythical'
    }

version = '2.5 files'
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Mobile Safari/537.36'
}

catch_ids = []

from config import user_token
from config import catch_id
from config import prefix
from config import ping
from config import catch_id2, catch_id3, catch_id4, catch_id5, catch_id6
catch_ids.append(str(catch_id))
catch_ids.append(str(catch_id2))
catch_ids.append(str(catch_id3))
catch_ids.append(str(catch_id4))
catch_ids.append(str(catch_id5))
catch_ids.append(str(catch_id6))

catch_ids = [catch_id for catch_id in catch_ids if catch_id != '']
with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()

def CarregarPokemons():
    global pokemon_list
    print('Carregando lista dos Pokemons..')
    try:
        url = Arquivos['data/pokemon']
        pokemons = requests.get(url)
        if pokemons.status_code == 200:
            with open('data/pokemon', 'w', encoding='utf8') as PokemonList:
                PokemonList.write(pokemons.text)
                print('lista dos pokemons atualizada.')
        else:
            print('nao foi possivel atualizar a lista dos pokemons.')
    except:
        pass
    with open('data/pokemon', 'r', encoding='utf8') as file:
        pokemon_list = file.read()

Thread(target=CarregarPokemons).start()


with open('data/legendary', 'r') as file:
    legendary_list = file.read()
with open('data/mythical', 'r') as file:
    mythical_list = file.read()
with open('data/level', 'r') as file:
    to_level = file.readline()

num_pokemon = 0
shiny = 0
legendary = 0
mythical = 0
captcha_content = None
captcha = False
poketwo = 716390085896962058
client = commands.Bot(command_prefix=[f"{prefix} ", f"{prefix}"], help_command=None)
def solve(message):
    hint = []
    for i in range(15, len(message) - 1):
        if message[i] != '\\':
            hint.append(message[i])
    hint_string = ''
    for i in hint:
        hint_string += i
    hint_replaced = hint_string.replace('_', '.')
    solution = re.findall('^' + hint_replaced + '$', pokemon_list, re.MULTILINE)
    return solution


paused = False

@client.event
async def on_ready():
    print(colored(f'Autocatch em execuçao em : {client.user.name}', 'black', 'on_white'))
    try:
        channel = client.get_channel(int(catch_ids[0]))
        if channel:
            await channel.typing()
            await asyncio.sleep(2)
            pro = ["autocatch online.", "ac online", "ac on", "autocatch on"]
            await channel.send(random.choice(pro))
        else:
            print(colored(f"Nao foi possivel obter o canal: {catch_id}!", "red"))
    except:
        print(colored("Ocorreu um erro!", "red"))


def remover_emojis(texto): 
     texto_sem_emojis = texto.replace('♀️', '').replace('♂️', '') 
     return texto_sem_emojis 
  

 
         
def remover_acentos(palavra):
    return unidecode(palavra)
  
  
def limpar_texto(texto): 
    texto_sem_emojis = remover_emojis(texto) 
    texto_sem_acentos = remover_acentos(texto_sem_emojis) 
    return texto_sem_acentos

@client.event
async def on_message(message):
    global paused
    global captcha_content
    if str(message.channel.id) in catch_ids:
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    timesleep = random.uniform(1.5, 7.5)
                    await asyncio.sleep(0)
                    if not paused:
                        await message.channel.typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            timesleep = random.uniform(0.8, 2.3)
                            if not paused:
                                await message.channel.typing()
                                pokemon_name = limpar_texto(i.lower())
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {pokemon_name}')
                            else:
                                if captcha:
                                    await asyncio.sleep(random.uniform(0.5,1.5))
                                    await message.channel.typing()
                                    await asyncio.sleep(random.uniform(0.5, 4.5))
                                    await message.channel.send(f"autocatch esta pausado pois o Bot detectou um captcha\n{captcha_content}")
                elif 'Congratulations' in content:
                    global shiny
                    global legendary
                    global num_pokemon
                    global mythical
                    num_pokemon += 1
                    split = content.split(' ')
                    pokemon = split[7].replace('!', '')
                    if 'seem unusual...' in content:
                        shiny += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary += 1
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical += 1
                        print(f'Mythical Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                    else:
                        print(f'Total Pokémon Caught: {num_pokemon} :{pokemon}')
                elif 'human' in content:
                    paused = True
                    await message.channel.typing()
                    await asyncio.sleep(random.uniform(0.5,3.5))
                    await message.channel.send(f'<@{ping}> Captcha Detectado! Bot pausado.')
                    captcha_content = message.content
                    captcha =True
    if not message.author.bot:
        await client.process_commands(message)
  
"""
Comando desativado
@client.command()
async def say(ctx, *, args):
    if str(ctx.channel.id) in str(catch_ids):
        await ctx.send(args)
"""

@client.command()
async def start(ctx):
    global paused
    if str(ctx.channel.id) in catch_ids:
        async with ctx.typing():
            await asyncio.sleep(random.uniform(0.5, 0.9))
            if not paused:
                await ctx.send('Bot ja esta em Execuçao.')
            else:
                paused = False
                await ctx.send('Bot Iniciado.')

@client.command()
async def stop(ctx):
    global paused
    if str(ctx.channel.id) in catch_ids:
        async with ctx.typing():
            await asyncio.sleep(random.uniform(0.5, 0.9))
            if not paused:
                paused = True
                await ctx.send('Bot Pausado.')
            else:
                await ctx.send('Bot Ja esta pausado.')
      


      

def Alerts():
    time.sleep(1)
    print(colored(f'\nPokétwo Autocacther.\n\nsò mitada violenta.', 'black', 'on_light_cyan')) 
    print(colored(f'Versao: {version} TERMUX', 'black', 'on_white')) 
    print(colored(f'o prefix do autocatch é "{prefix}".\n\nuse {prefix}ajuda para ver a lista de comandos.', 'yellow')) 
    

def ProcurarAtualizaçoes():
    requisicoes = 1
    while True:
        for file, url in Arquivos.items():
            print(f'{requisicoes} - (GET)[{url}]')
            requisicoes += 1
            response = requests.get(url)
            if response.status_code == 200:
                with open(file, 'w') as arch:
                    arch.write(response.text)
                    print(f'{file} Foi Recarregado.')
        time.sleep(600)


Thread(target=Alerts).start()
Thread(target=ProcurarAtualizaçoes).start()
try:
    client.run(f"{user_token}")
except discord.HTTPException as e:
    if e.status == 429:
        print(colored('Discord Recusou a Conexao com o Codigo De status: 429 too many requests.\n', 'red'), str(e))
        """
        FlasK.terminate()
        """
