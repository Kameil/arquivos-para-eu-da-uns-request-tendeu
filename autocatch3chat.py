import re, os, asyncio, random, string, keep_alive, random, termcolor
from discord.ext import commands, tasks
from termcolor import colored
version = 'v1.3.5'

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
client = commands.Bot(command_prefix=f'{prefix}')

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

@client.event
async def on_ready():
    print(colored(f'Autocatch em execuçao em : {client.user.name}', 'green'))
    channel = client.get_channel(int(catch_id))
    typing_channel = client.get_channel(int(catch_id))
    await typing_channel.trigger_typing()
    await asyncio.sleep(2)
    await channel.send('autocatch online.')


@client.event
async def on_message(message):
    global paused
    if message.channel.id == int(catch_id):
        channel = client.get_channel(int(catch_id))
        if message.author.id == poketwo:
            if message.embeds:
                embed_title = message.embeds[0].title
                if 'wild pokémon has appeared!' in embed_title:
                    timesleep = random.uniform(1.5, 2.0)
                    await asyncio.sleep(0)
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            timesleep = random.uniform(0.8, 2.5)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {iu}')
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
                        print(f'Total Pokémon Caught c1: {num_pokemon} :{pokemon}')
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
                        await message.channel.send(f'<@{ping}> captcha ai baitola, use {prefix}start para despausar.')
                        paused = True
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
                    timesleep = random.uniform(4.5, 6.0)
                    await asyncio.sleep(0)
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            timesleep = random.uniform(0.8, 1.8)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id2))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {iu}')
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
                        print(f'Total Pokémon Caught c2: {num_pokemon} :{pokemon}')
                elif 'human' in content:
                    timesleep = random.uniform(5.5, 1.5)
                    typing_channel = client.get_channel(int(catch_id))
                    await typing_channel.trigger_typing()
                    await asyncio.sleep(timesleep)
                    await message.channel.send(f'<@{ping}> captcha ai baitola, use {prefix}start para despausar.')
                    paused = True
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
                    timesleep = random.uniform(5.5, 6.5)
                    await asyncio.sleep(0)
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> h')
            else:
                content = message.content
                if 'The pokémon is ' in content:
                    if not len(solve(content)):
                        print('Pokemon not found.')
                    else:
                        for i in solve(content):
                            iu = i.lower()
                            timesleep = random.uniform(3.8, 4.5)
                            await asyncio.sleep(0)
                            if not paused:
                                typing_channel = client.get_channel(int(catch_id3))
                                await typing_channel.trigger_typing()
                                await asyncio.sleep(timesleep)
                                await message.channel.send(f'<@716390085896962058> c {iu}')
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
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.8, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical += 1
                        print(f'Mythical Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    else:
                        print(f'Total Pokémon Caught c2: {num_pokemon} :{pokemon}')
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
                    if not paused:
                        typing_channel = client.get_channel(int(catch_id))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(3)
                        await message.channel.send('<@716390085896962058> h')
    if not message.author.bot:
        await client.process_commands(message)

@client.command(name='falar', aliases['echo', 'say'])
async def say(ctx, *, args):
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
        await ctx.send(args)
      
@client.command(name='iniciar', aliases['start'])
async def start_cmd(ctx):
    global paused
    if paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = False
            await ctx.send('Bot iniciado.')
        else:
            if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                await ctx.send('Bot já está em execução.')

@client.command(name='parar', aliases=['stop'])
async def stop_cmd(ctx):
    global paused
    if not paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = True
            await ctx.send('Bot pausado com sucesso.')
    else:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            await ctx.send('Bot já está Pausado.')
            
@client.command(name='ajuda', aliases['ajud', 'aju', 'aj', 'a'])
async def ajuda_cmd(ctx):
    global help_command
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)] and help_command == 1:
        await ctx.send(f'```\n**lista de comandos**\n{prefix}start  •  usado para iniciar o bot\n{prefix}stop  •  usado para parar o bot.\nem-breve novos comandos.')
        help_command += 1
    else:
        if help_command == 2:
            await ctx.send('O comando **help** só pode ser utilizado uma vez a cada vez que voce inicia o bot.')
            help_command += 1
        else:
            if help_command == 3:
                print('ih ala tentou usar o help')
                help_command += 1

async def help(ctx):
    global help_command
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)] and help_command == 1:
        await ctx.send(f'```\n**lista de comandos**\n{prefix}start  •  usado para iniciar o bot\n{prefix}stop  •  usado para parar o bot.\nem-breve novos comandos.')
        help_command += 1
    else:
        if help_command == 2:
            await ctx.send('O comando **help** só pode ser utilizado uma vez a cada vez que voce inicia o bot.')
            help_command += 1
        else:
            if help_command == 3:
                print('ih ala tentou usar o help')
                help_command += 1
  

keep_alive.keep_alive()
print(colored(f'Pokétwo Autocacther.\n\nsò mitada violenta versão :{version}\n\nEvent Log:', 'green'))
print(colored(f'o prefix do autocatch é "{prefix}".', 'yellow'))
client.run(f"{user_token}")
