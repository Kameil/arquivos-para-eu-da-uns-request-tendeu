import re, os, asyncio, random, string, keep_alive, random
from discord.ext import commands, tasks
from termcolor import colored

pokeone = 473020399060385792
if os.environ.get('prefix'):
    prefixo = os.environ['prefix']
else:
    prefixo = await osenv("prefix")
paused = False
token = os.environ['user_token']
chat = os.environ['chat_id']

client = commands.Bot(command_prefix='vdd', help_command=None)
esperar = [60.0, 120.0, 90.0]

@tasks.loop(seconds=random.choice(esperar))
async def analize_loop():
    fast = random.randint(3,6)
    numero = 1
    channel = client.get_channel(int(chat))
    channel.trigger_typing()
    await channel.send(f'{prefixo}s')

@analize_loop.before_loop
async def fazsentido():
    await client.wait_until_ready()

analize_loop.start()

@client.event
async def on_ready():
    print(colored(f"Auto Spawn em Execuçao em - {client.user.name}", "blue")) 

@client.event
async def on_message(message):
    global paused
    fast = random.randint(1,3)
    channel = client.get_channel(int(chat))
    if message.channel.id == int(chat):
        if message.author.id == pokeone:
            if message.embeds:
                embed_desc = message.embeds[0].description
                embed_title = message.embeds[0].title
                embed_footer = message.embeds[0].footer
                if embed_desc and 'You have won the Wild Battle!' in embed_desc:
                    channel.trigger_typing()
                    await asyncio.sleep(fast)
                    dangoro = random.randint(1,10)
                    if dangoro == 5:
                        await message.channel.send(f'{prefixo}spawn')
                    else:
                        await message.channel.send(f'{prefixo}s')
                
                if embed_title and 'Shiny Wild Pokémon' in embed_title:
                    channel.trigger_typing()
                    await message.channel.send(f'{prefixo}master')
                else:
                    if embed_footer and 'Send 1' in embed_footer.text:
                        channel.trigger_typing()
                        await asyncio.sleep(fast)
                        await message.channel.send('1')
                if embed_desc and "You're already in a battle." in embed_desc:
                    channel.trigger_typing()
                    await asyncio.sleep(fast)
                    await channel.send('1')
            else:
                if 'Keep the calm!' in message.content:
                    channel.trigger_typing()
                    await asyncio.sleep(2)
                    await message.channel.send(f'{prefixo}s')

async def osenv(envv):
    if envv == "prefix":
        await asyncio.sleep(3)
        print(colored('''Voce nao possui o secret "prefix" o AutoSpawn ira Iniciar Utilizando o prefixo Padrao "."''', "red"))
        return "."


async def pokeoneautospawn():
    await asyncio.sleep(1)
    print(colored(f'iniciando autospawn com prefix: "{prefixo}"...', 'black', 'on_white'))
    
keep_alive.keep_alive()
asyncio.run(pokeoneautospawn())
client.run(f"{token}")
