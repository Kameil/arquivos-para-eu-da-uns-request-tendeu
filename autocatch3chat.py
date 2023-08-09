import re, os, asyncio, random, string, keep_alive, random, termcolor, subprocess
from discord.ext import commands, tasks
from termcolor import colored
version = 'v1.7.4 mitada'

user_token = os.environ['user_token']
catch_id = os.environ['catch_id']
catch_id2 = os.environ['catch_id2']
catch_id3 = os.environ['catch_id3']
ping = os.environ['captcha_ping']
help_command = 1
with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()
with open('data/legendary', 'r') as file:
    legendary_list = file.read()
with open('data/mythical', 'r') as file:
    mythical_list = file.read()
num_pokemon = 0
shiny = 0
legendary = 0
mythical = 0
prefix = os.environ['prefix']
poketwo = 716390085896962058
client = commands.Bot(command_prefix=[f'{prefix} ', f'{prefix}'], help_command=None)
captcha_verify = False
captcha_message = 'Erro.!'
#vd
#solve ai dos pokemon tlgd ne
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


def remover_emojis(texto):
    texto_sem_emojis = texto.replace('♀️', '').replace('♂️', '')
    return texto_sem_emojis

def remover_acentos(palavra):
    try:
        from unidecode import unidecode
    except ImportError:
        try:
            subprocess.Popen(['pip', 'install', 'unidecode'])
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
async def on_ready():
    print(colored(f'Autocatch em execuçao em : {client.user.name}', 'black', 'on_white'))
    channel = client.get_channel(int(catch_id))
    await channel.trigger_typing()
    await asyncio.sleep(2)
    pro = random.randint(1,4)
    if pro == 1:
        await channel.send('autocatch online.')
    elif pro == 2:
        await channel.send('ac online')
    elif pro == 3:
        await channel.send('ac on')
    else:
        await channel.send('autocatch on')


@client.event
async def on_message(message):
    global paused
    global captcha_verify
    global captcha_message
    if message.channel.id == int(catch_id):
        channel = client.get_channel(int(catch_id))
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    if paused:
                        if captcha_verify:
                            typing_channel = client.get_channel(int(catch_id))
                            await typing_channel.trigger_typing()
                            await message.channel.send(f'Bot esta pausado pois detectou um **capctha**.\n{captcha_message}')
                    else:
                        timesleep = random.uniform(1.5, 2.0)
                        await asyncio.sleep(0)
                        if not paused:
                            typing_channel = client.get_channel(int(catch_id))
                            await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
                        if captcha_verify:
                            captcha_verify = False
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            pokemon_name = limpar_texto(iu)
                            timesleep = random.uniform(0.8, 2.5)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {pokemon_name}')
                    check = random.randint(1, 60)
                    if check == 1:
                        await asyncio.sleep(900)
                    else:
                        await asyncio.sleep(1)

                elif 'Congratulations' in content:
                    global shiny
                    global legendary
                    global num_pokemon
                    global mythical
                    num_pokemon += 1
                    split = content.split(' ')
                    pokemon = split[7].replace('!', '')
                    infol = random.randint(1, 20)
                    if infol == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    ping2 = random.randint(1, 30)
                    if ping2 == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> ping')
                    if f'a level 1 {pokemon}' in content:
                        timesleep = random.uniform(0.3, 0.9)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    if f'seem unusual...{pokemon}' in content:
                        shiny += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.4, 0.9)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary += 1
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 0.9)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical += 1
                        print(f'Mythical Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.4, 0.9)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    else:
                        print(colored(f'{client.user.name}  -  Total Pokémon Caught: {num_pokemon} :{pokemon}', 'blue'))
                elif 'You have completed the quest' in content:
                        timesleep = random.uniform(0.1, 2.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> q')
                elif 'You have completed this quest track and received the' in content:
                        timesleep = random.uniform(1.0, 2.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> profile')
                elif 'human' in content:
                        timesleep = random.uniform(1.5, 2.5)
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send(f'<@{ping}> captcha detectado, use {prefix}start para despausar.')
                        captcha_verify = True
                        paused = True
                        captcha_message = content
                        if not paused:
                            typing_channel =   client.get_channel(int(catch_id))
                            await typing_channel.trigger_typing()
                            await asyncio.sleep(3)
                            await message.channel.send('<@716390085896962058> h')
    elif message.channel.id == int(catch_id2):
        channel = client.get_channel(int(catch_id2))
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    if paused:
                        if captcha_verify:
                            typing_channel = client.get_channel(int(catch_id2))
                            await typing_channel.trigger_typing()
                            await asyncio.sleep(1)
                            await message.channel.send(f'Bot esta pausado pois detectou um **capctha**.\n{captcha_message}')
                    else:
                        timesleep = random.uniform(4.5, 6.0)
                        await asyncio.sleep(0)
                        if not paused:
                            typing_channel = client.get_channel(int(catch_id2))
                            await typing_channel.trigger_typing()
                            await asyncio.sleep(timesleep)
                            if paused:
                                await message.channel.send(f'Nao foi possivel concluir o catch!:red_sircle: pois um **captcha** foi dectado.\n{captcha_message}')
                            else:
                                await message.channel.send('<@716390085896962058> h')
                                if captcha_verify:
                                    captcha_verify = False
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            pokemon_name = limpar_texto(iu)
                            timesleep = random.uniform(0.8, 1.8)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id2))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {pokemon_name}')
                    check = random.randint(1, 60)
                    if check == 1:
                        await asyncio.sleep(900)
                    else:
                        await asyncio.sleep(1)

                elif 'Congratulations' in content:
                    num_pokemon += 1
                    split = content.split(' ')
                    pokemon = split[7].replace('!', '')
                    infol2 = random.randint(1, 20)
                    if infol2 == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    pingr = random.randint(1, 30)
                    if pingr == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> ping')
                    if f'a level 1 {pokemon}' in content:
                        timesleep = random.uniform(0.6, 1.0)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    if 'seem unusual...' in content:
                        shiny += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary += 1
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.8, 1.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical += 1
                        print(f'Mythical Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                elif 'You have completed the quest' in content:
                        timesleep = random.uniform(1.0, 2.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> q')
                elif 'You have completed this quest track and received the' in content:
                        timesleep = random.uniform(1.0, 2.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> profile')
                        print(colored(f'{client.user.name}  -  Total Pokémon Caught: {num_pokemon} :{pokemon}', 'blue'))
                elif 'human' in content:
                    timesleep = random.uniform(5.5, 1.5)
                    typing_channel = client.get_channel(int(catch_id))
                    await typing_channel.trigger_typing()
                    await asyncio.sleep(timesleep)
                    await message.channel.send(f'<@{ping}> captcha ai baitola, use {prefix}start para despausar.')
                    paused = True
                    captcha_verify = True
                    captcha_message = content
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(3)
                        await message.channel.send('<@716390085896962058> h')
                        
    elif message.channel.id == int(catch_id3):
        channel = client.get_channel(int(catch_id3))
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    if paused:
                        if captcha_verify:
                            typing_channel = client.get_channel(int(catch_id3))
                            await typing_channel.trigger_typing()
                            await message.channel.send(f'Bot esta pausado pois detectou um **capctha**.\n{captcha_message}')
                        
                    else:
                        timesleep = random.uniform(5.5, 6.5)
                        await asyncio.sleep(0)
                        if not paused:
                            typing_channel = client.get_channel(int(catch_id3))
                            await typing_channel.trigger_typing()
                            await asyncio.sleep(timesleep)
                            if paused:
                                await message.channel(f'Nao foi possivel pegar esse pokemon pois o bot detectou um captcha.\n{captcha_message}')
                            else:
                                await message.channel.send('<@716390085896962058> h')
                                if captcha_verify:
                                    captcha_verify = False
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            pokemon_name = limpar_texto(iu)
                            timesleep = random.uniform(3.8, 4.5)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id3))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {pokemon_name}')
                    check = random.randint(1, 60)
                    if check == 1:
                        await asyncio.sleep(900)
                    else:
                        await asyncio.sleep(1)

                elif 'Congratulations' in content:
                    num_pokemon += 1
                    split = content.split(' ')
                    pokemon = split[7].replace('!', '')
                    infol23 = random.randint(1, 20)
                    if infol23 == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    pingr3 = random.randint(1, 30)
                    if pingr3 == 1:
                        timesleep = random.uniform(1.5, 4.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> ping')
                    if f'a level 1 {pokemon}' in content:
                        timesleep = random.uniform(0.8, 1.2)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    if 'seem unusual...' in content:
                        shiny += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary += 1
                        print(colored(f'Legendary Pokémon caught! Pokémon: {pokemon}', 'yellow'))
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.8, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical += 1
                        print(colored(f'Pokemon Mythical Pego : {pokemon}', 'green'))
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    else:
                        print(colored(f'{client.user.name}  -  Total Pokémon Caught: {num_pokemon} :{pokemon}', 'blue'))
                elif 'You have completed the quest' in content:
                        timesleep = random.uniform(1.0, 2.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> q')
                elif 'You have completed the quest' in content:
                        timesleep = random.uniform(1.0, 2.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> q')
                elif 'You have completed this quest track and received the' in content:
                        timesleep = random.uniform(2.5, 6.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> profile')
                elif 'human' in content:
                    print('captcha detectado, medo.')
                    timesleep = random.uniform(1.5, 4.5)
                    typing_channel = client.get_channel(int(catch_id))
                    await typing_channel.trigger_typing()
                    await asyncio.sleep(timesleep)
                    await message.channel.send(f'<@{ping}> capctha, use {prefix}start para despausar.')
                    paused = True
                    captcha_verify = True
                    captcha_message = content
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(3)
                        await message.channel.send('<@716390085896962058> h')
    if not message.author.bot:
        content = message.content
        if content.startswith(f'{prefix}start') and message.author.id == client.user.id or content.startswith(f'{prefix}ligar') and message.author.id == client.user.id or content.startswith(f'{prefix} start') and message.author.id == client.user.id or content.startswith(f'{prefix} ligar') and message.author.id == client.user.id:
                    if paused:
                        if message.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                            paused = False
                            await message.channel.send('Bot iniciado.')
                    else:
                        if message.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                            await message.channel.send('Bot já está em execução.')
                            
                            
        if content.startswith(f'{prefix}buy incense') and message.author.id == client.user.id or content.startswith(f'{prefix}buy i') and message.author.id == client.user.id:
            item = "incense"
            channel = client.get_channel(int(catch_id))
            await asyncio.sleep(1)
            await channel.send(f'<@716390085896962058> buy {item}')
            channel = client.get_channel(int(catch_id2))
            await asyncio.sleep(1)
            await channel.send(f'<@716390085896962058> buy {item}')
            channel = client.get_channel(int(catch_id3))
            await asyncio.sleep(1)
            await channel.send(f'<@716390085896962058> buy {item}')
        
        
        if content.startswith(f'{prefix}stop') and message.author.id == client.user.id or content.startswith(f'{prefix}parar') and message.author.id == client.user.id or content.startswith(f'{prefix} stop') and message.author.id == client.user.id or content.startswith(f'{prefix} parar') and message.author.id == client.user.id:
            if not paused:
                if message.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                    paused = True
                    await message.channel.send('Bot pausado com sucesso.')
                else:
                    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                        await message.channel.send('Bot já está Pausado.')
        await client.process_commands(message)

@client.command(name='falar', aliases=['echo', 'say'])
async def say_cmd(ctx, *, args):
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
        digitar = ctx.channel.id
        typing_channel = client.get_channel(int(digitar))
        await typing_channel.trigger_typing()
        await asyncio.sleep(1)
        await ctx.send(args)
      
@client.command(name='ligar', aliases=['start'])
async def start_cmd(ctx):
    global paused
    if paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = False
            await ctx.send('Bot iniciado.')
        else:
            if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                await ctx.send('Bot já está em execução.')

@client.command(name='pausar', aliases=['stop'])
async def stop_cmd(ctx):
    global paused
    if not paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = True
            await ctx.send('Bot pausado com sucesso.')
    else:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            await ctx.send('Bot já está Pausado.')
            
@client.command(name='ajuda', aliases=['ajud', 'aju', 'aj', 'a', 'help'])
async def ajuda_cmd(ctx, comando=None, argumento=None):
    global help_command
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
        if comando in ['start', 'ligar']:
            await ctx.send(f'{comando} Comando para despausar o Bot.')
        elif comando in ['stop', 'pausar']:
            await ctx.send(f"{comando} Comando Para Pausar o Bot")
        elif comando in ['say', 'falar', 'echo']:
            await ctx.send(f'{comando}  -  Comando utlizado para controlar o bot aparti de outras contas.`')
        elif comando in ['buy', 'b', 'comprar']:
            await ctx.send(f'{comando}  -  Comando para comprar incenses.')
        else:
            if comando is not None:
                await ctx.send(f'Comando nao encontrado comando: {comando}')
        if comando == None:
            await ctx.send(f'```\n**lista de comandos**\nstart/ligar  •  usado para iniciar o bot\nstop/pausar  •  usado para parar o bot.\nsay/echo/falar  •  usado para controlar o bot atravez de outras contas.\nbuy/comprar/b  •  usado para compra incenses exemplo" {prefix}buy incense" ele ira comprar incense em todos os chats\n\npara saber mais detalhes sobre um comando escreva {prefix}help [nome-do-comando]\n```')
        print(colored(f"•  comando help executado por: {ctx.author.name}", "yellow"))

def item_name(item):
    if item in ['I', 'Incense', 'INCENSE', 'i', 'incense']:
        item = "incense"
    return item

@client.command(name='buy', aliases=['comprar', 'b'])
async def buy_cmd(ctx, item=None):
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)] and item in ['incense', 'i', 'INCENSE', 'Incense', 'I'] and item is not None:
        incense = item_name(item)
        channel = client.get_channel(int(catch_id))
        await asyncio.sleep(1)
        await channel.send(f'<@716390085896962058> buy {incense}')
        channel = client.get_channel(int(catch_id2))
        await asyncio.sleep(1)
        await channel.send(f'<@716390085896962058> buy {incense}')
        channel = client.get_channel(int(catch_id3))
        await asyncio.sleep(1)
        await channel.send(f'<@716390085896962058> buy {incense}')
        print(colored(" • Comando de incense executado", "yellow"))
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)] and item == None:
        await ctx.send("Você precisa selecionar um comando antes\n exemplo: [incense, i] ambos usados para comprar incense.")
        

@client.command(name='exec')
async def exec_cmd(ctx, process, *, executar):
    if os.environ.get('dev'):
        developer = os.environ['dev']
        if developer == 'True':
            if process == 'sub':
                await ctx.send('criando arquivo exec.py...')
                with open('exec-code.py', 'w') as exec_code:
                    exec_code.write(executar)
                await asyncio.sleep(1)
                await ctx.send('executando...')
                subprocess.Popen(["python3", "exec-code.py"])
            elif process == 'exec':
                await ctx.send('executando..')
                mitada = True
                try:
                    exec(executar)
                except Exception as e:
                    await ctx.send(f'Erro durante a execução:\n```{e}```')
                    mitada = False
                    return
                if mitada:
                    await ctx.send(f'executado.\nLogs:\n```{captured_logs}```')
            else:
                await ctx.send(f'process: "{process}" nao encontrado')
        else:
            await ctx.send('modo desenvolvedor nao esta ativo.')
            

async def somitada():
    await asyncio.sleep(1)
    print(colored(f'\nPokétwo Autocacther.\n\nsò mitada violenta.', 'black', 'on_light_cyan'))
    print(colored(f'Versao: {version}', 'black', 'on_white'))
    print(colored(f'o prefix do autocatch é "{prefix}".\n\nuse {prefix}ajuda para ver a lista de comandos.', 'yellow'))

keep_alive.keep_alive()
asyncio.run(somitada())
client.run(f"{user_token}")
