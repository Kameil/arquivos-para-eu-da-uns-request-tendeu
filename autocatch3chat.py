import re, os, asyncio, random, string, keep_alive, random, termcolor
from discord.ext import commands, tasks
from termcolor import colored
version = 'v1.1.1'

user_token = os.environ['user_token']
catch_id = os.environ['catch_id']
catch_id2 = os.environ['catch_id2']
catch_id3 = os.environ['catch_id3']
ping = os.environ['captcha_ping']
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
num_pokemon2 = 0
shiny2 = 0
legendary2 = 0
mythical2 = 0
num_pokemon3 = 0
shiny3 = 0
legendary3 = 0
mythical3 = 0
prefix = os.environ['prefix']
# prefixo é ai agora belesinha

poketwo = 716390085896962058
client = commands.Bot(command_prefix=f'{prefix}')
intervals = [50000.0, 30000.2, 30000.4, 30000.6, 30000.8]
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
    print(f'Logged into account: {client.user.name}')
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
                elif "Congratulations" in embed_title:
                    embed_content = message.embeds[0].description
                    if 'now level' in embed_content:
                        split = embed_content.split(' ')
                        a = embed_content.count(' ')
                        level = int(split[a].replace('!', ''))
                        if level == 100:
                            await message.channel.send(f".s {to_level}")
                            with open('data/level', 'r') as fi:
                                data = fi.read().splitlines(True)
                            with open('data/level', 'w') as fo:
                                fo.writelines(data[1:])
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
                elif "Congratulations" in embed_title:
                    embed_content = message.embeds[0].description
                    if 'now level' in embed_content:
                        split = embed_content.split(' ')
                        a = embed_content.count(' ')
                        level = int(split[a].replace('!', ''))
                        if level == 100:
                            await message.channel.send(f".s {to_level}")
                            with open('data/level', 'r') as fi:
                                data = fi.read().splitlines(True)
                            with open('data/level', 'w') as fo:
                                fo.writelines(data[1:])
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
                    global shiny2
                    global legendary2
                    global num_pokemon2
                    global mythical2
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
                        shiny2 += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary2 += 1
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.8, 1.5)
                        typing_channel = client.get_channel(int(catch_id2))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical2 += 1
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
                elif "Congratulations" in embed_title:
                    embed_content = message.embeds[0].description
                    if 'now level' in embed_content:
                        split = embed_content.split(' ')
                        a = embed_content.count(' ')
                        level = int(split[a].replace('!', ''))
                        if level == 100:
                            await message.channel.send(f".s {to_level}")
                            with open('data/level', 'r') as fi:
                                data = fi.read().splitlines(True)
                            with open('data/level', 'w') as fo:
                                fo.writelines(data[1:])
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
                    global shiny3
                    global legendary3
                    global num_pokemon3
                    global mythical3
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
                        shiny3 += 1
                        print(f'Shiny Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.5, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', legendary_list, re.MULTILINE):
                        legendary3 += 1
                        print(f'Legendary Pokémon caught! Pokémon: {pokemon}')
                        print(f'Shiny: {shiny} | Legendary: {legendary} | Mythical: {mythical}')
                        timesleep = random.uniform(0.8, 1.5)
                        typing_channel = client.get_channel(int(catch_id3))
                        await typing_channel.trigger_typing()
                        await asyncio.sleep(timesleep)
                        await message.channel.send('<@716390085896962058> i l')
                    elif re.findall('^' + pokemon + '$', mythical_list, re.MULTILINE):
                        mythical3 += 1
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

@client.command()
async def say(ctx, *, args):
    if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
        await ctx.send(args)
      
@client.command()
async def start(ctx):
    global paused
    if paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = False
            await ctx.send('Bot started.')
        else:
            if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
                await ctx.send('Bot is already running.')

@client.command()
async def stop(ctx):
    global paused
    if not paused:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            paused = True
            await ctx.send('Bot stopped.')
    else:
        if ctx.channel.id in [int(catch_id), int(catch_id2), int(catch_id3)]:
            await ctx.send('Bot is already stopped.')

print(colored(f'Pokétwo Autocacther. o autocatch ira marca o id: \n{ping}\n Se nao for você, por favor, alterene na linha `16` do codigo, na variavel "ping".\nEvent Log:', 'green'))
print(colored(f'o prefix do autocatch é "{prefix}".', 'yellow'))
keep_alive.keep_alive()
client.run(f"{user_token}")
