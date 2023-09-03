import re, os, asyncio, random, string, keep_alive, random
from discord.ext import commands
from termcolor import colored

version = '2.0 beta'

catch_ids = []

user_token = os.environ['user_token']
catch_id = os.environ['catch_id']
catch_ids.append(catch_id)
catch_id2 = os.environ['catch_id2']
catch_ids.append(catch_id2)
catch_id3 = os.environ['catch_id3']
catch_ids.append(catch_id3)
try:
    catch_id4 = os.environ['catch_id4']
    catch_ids.append(catch_id4)
except:
    pass
try:
    catch_id5 = os.environ["catch_id5"]
    catch_ids.append(catch_id5)
except:
    pass
try:
    catch_id6 = os.environ['catch_id6']
    catch_ids.append(catch_id5)
except:
    pass
ping = os.environ['captcha_ping']
prefix = os.environ['prefix']


with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
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
            await channel.trigger_typing()
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
    try: 
        from unidecode import unidecode 
        return unidecode(palavra) 
    except ImportError: 
        try: 
            subprocess.Popen(['pip', 'install', 'unidecode']) 
            time.sleep(5) 
            from unidecode import unidecode 
            return unidecode(palavra) 
        except Exception as e: 
            print(f"Ocorreu um Erro no 'unidecode' o bot proseguira Normalmente. Mas sem a Funçao de remover acentos.\n{e}\n dica: Voce pode instalar o unidecode utilizando\npip install unidecode\nno shell.") 
            return palavra 
  
  
def limpar_texto(texto): 
    texto_sem_emojis = remover_emojis(texto) 
    texto_sem_acentos = remover_acentos(texto_sem_emojis) 
    return texto_sem_acentos

@client.event
async def on_message(message):
    global paused
    global captcha_content
    if message.channel.id in catch_ids:
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    timesleep = random.uniform(1.5, 4.5)
                    await asyncio.sleep(0)
                    if not paused:
                        await message.channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            timesleep = random.uniform(0.8, 5.5)
                            if not paused:
                                await message.channel.trigger_typing()
                                pokemon_name = limpar_texto(i.lower())
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {pokemon_name}')
                            else:
                                if captcha:
                                    await asyncio.sleep(random.uniform(0.5,1.5))
                                    await message.channel.trigger_typing()
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
                    await message.channel.trigger_typing()
                    await asyncio.sleep(random.uniform(0.5,3.5))
                    await message.channel.send(f'<@{ping}> Captcha Detectado! Bot pausado.')
                    captcha_content = message.content
                    captcha =True
    if not message.author.bot:
        await client.process_commands(message)
  

@client.command()
async def say(ctx, *, args):
    if ctx.channel.id in catch_ids:
        await ctx.send(args)

@client.command()
async def start(ctx):
    global paused
    if ctx.channel.id in catch_ids:
        if not paused:
            await ctx.send('Bot ja esta em Execuçao.')
        else:
            paused = False
            await ctx.send('Bot Iniciado.')

@client.command()
async def stop(ctx):
    if ctx.channel.id in catch_ids:
        if not paused:
            paused = True
            await ctx.send('Bot Pausado.')
        else:
            await ctx.send('Bot Ja esta pausado.')
    else:
        pass
      


      

async def somitada(): 
    await asyncio.sleep(1) 
    print(colored(f'\nPokétwo Autocacther.\n\nsò mitada violenta.', 'black', 'on_light_cyan')) 
    print(colored(f'Versao: {version}', 'black', 'on_white')) 
    print(colored(f'o prefix do autocatch é "{prefix}".\n\nuse {prefix}ajuda para ver a lista de comandos.', 'yellow')) 
  
keep_alive.keep_alive() 
asyncio.run(somitada()) 
client.run(f"{user_token}")