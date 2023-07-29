import re, os, asyncio, random, string, keep_alive, random
from discord.ext import commands, tasks
from termcolor import colored

pokeone = 473020399060385792
prefixo = os.environ['prefix']
paused = False
token = os.environ['user_token']
chat = os.environ['chat_id']

client = commands.Bot(command_prefix='vdd')
esperar = [60.0, 120.0, 90.0]

@tasks.loop(seconds=random.choice(esperar))
async def analize_loop():
    fast = random.randint(3,6)
    numero = 1
    channel = client.get_channel(int(chat))
    await channel.send(f'{prefixo}s')

@analize_loop.before_loop
async def fazsentido():
    await client.wait_until_ready()

analize_loop.start()

@client.event
async def on_ready():
    print(f'Loguei ai: {client.user.name}') 

@client.event
async def on_message(message):
    global paused
    channel = client.get_channel(int(chat))
    if message.channel.id == int(chat):
        if message.author.id == pokeone:
            if message.embeds:
                embed_desc = message.embeds[0].description
                if embed_desc and 'You have won the Wild Battle!' in embed_desc:
                    await asyncio.sleep(1)
                    await message.channel.send(f'{prefixo}s')
            if message.embeds:
                embed_title = message.embeds[0].title
                embed_footer = message.embeds[0].footer
                if embed_title and 'Shiny Wild Pokémon' in embed_title:
                    await message.channel.send(f'{prefixo}master')
                else:
                    if embed_footer and 'Send 1' in embed_footer.text:
                        await asyncio.sleep(1)
                        await message.channel.send('1')
            if message.embeds:
                embed_inbatle = message.embeds[0].description
                if "You're already in a battle." in embed_inbatle:
                    await asyncio.sleep(1)
                    await channel.send('1')
            if 'Keep the calm!' in message.content:
                await asyncio.sleep(2)
                await message.channel.send(f'{prefixo}s')

async def parar():
    analize_loop.stop()

async def iniciar():
    analize_loop.start()
print(colored(f'Bot iniciado com sucesso •\nCom prefixo: {prefixo}', 'green'))
keep_alive.keep_alive()
client.run(f"{token}")
