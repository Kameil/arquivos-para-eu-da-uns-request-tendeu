import re, os, asyncio, random, string, keep_alive, random, time
from discord.ext import commands, tasks
from termcolor import colored

pokeone = 473020399060385792
prefixo = os.environ['prefix']
paused = False
token = os.environ['user_token']
chat = os.environ['chat_id']
send_s = time.time()

client = commands.Bot(command_prefix='&', help_command=None)
esperar = [60.0, 120.0, 90.0]

@tasks.loop(seconds=random.choice(esperar))
async def analize_loop():
    global send_s
    agora = time.time()
    espera = agora - send_s
    if int(espera) >= 30:
        pode = True
    else:
        pode = False
    if not paused and pode:
        fast = random.randint(3,6)
        numero = 1
        channel = client.get_channel(int(chat))
        await channel.trigger_typing()
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
    global send_s
    fast = random.randint(1,3)
    channel = client.get_channel(int(chat))
    if message.channel.id == int(chat) and not paused:
        if message.author.id == pokeone:
            if message.embeds:
                embed_desc = message.embeds[0].description
                embed_title = message.embeds[0].title
                embed_footer = message.embeds[0].footer
                if embed_desc and 'You have won the Wild Battle!' in embed_desc:
                    await channel.trigger_typing()
                    await asyncio.sleep(fast)
                    dangoro = random.randint(1,10)
                    if dangoro == 5:
                        await message.channel.send(f'{prefixo}spawn')
                    else:
                        await message.channel.send(f'{prefixo}s')
                    send_s = time.time()
                
                if embed_title and 'Shiny Wild Pokémon' in embed_title:
                    await channel.trigger_typing()
                    await message.channel.send(f'{prefixo}master')
                    send_s = time.time()
                else:
                    if embed_footer and 'Send 1' in embed_footer.text:
                        await channel.trigger_typing()
                        await asyncio.sleep(fast)
                        await message.channel.send('1')
                        send_s = time.time()
                if embed_desc and "You're already in a battle." in embed_desc:
                    await channel.trigger_typing()
                    await asyncio.sleep(fast)
                    await channel.send('1')
                    send_s = time.time()
                    
            else:
                if 'Keep the calm!' in message.content:
                    await channel.trigger_typing()
                    await asyncio.sleep(2)
                    await message.channel.send(f'{prefixo}s')
                    send_s = time.time()
                    
    if message.author.id == client.user.id:
        await client.process_commands(message)
    elif not message.author.bot:
        await client.process_commands(message)
    else:
        pass


@client.command(name='start')
async def start_cmd(ctx):
    if ctx.channel.id == int(chat):
        global paused
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        if paused:
            paused = False
            await ctx.send("Bot Iniciado")
        else:
            await ctx.send("Bot ja esta em Execuçao.")
        
@client.command(name="stop")
async def stop_cmd(ctx):
    global paused
    if ctx.channel.id == int(chat):
        await ctx.trigger_typing()
        await asyncio.sleep(1)
        if not paused:
            paused = True
            await ctx.send("Bot pausado.")
        else:
            await ctx.send("Bot ja esta pausado.")

async def pokeoneautospawn():
    await asyncio.sleep(1)
    print(colored(f'iniciando autospawn com prefix: "{prefixo}"...', 'black', 'on_white'))
    
keep_alive.keep_alive()
asyncio.run(pokeoneautospawn())
try:
    print(discord.__version__)
except:
    pass
client.run(f"{token}")
