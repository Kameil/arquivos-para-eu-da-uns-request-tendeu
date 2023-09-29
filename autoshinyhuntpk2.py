import re, os, asyncio, random, keep_alive, tracemalloc, aiohttp, aiofiles
import discord
from discord.ext import commands
import requests
from PIL import Image, ImageEnhance


catch_id = []
for i in range(101):
    try:
        numero = str(i)
        if numero == '0':
            catch_id.append(str(os.environ['catch_id']))
        else:
            catch_id.append(str(os.environ[f'catch_id{numero}']))
    except KeyError:
        pass


poketwo, pokename, paused, token = '716390085896962058', '0', False, os.environ['token']
unidentified_image = 'original_image.png'

with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()

# Configuração do bot
bot = commands.Bot(command_prefix='.', self_bot=True, help_command=None)

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

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}') 

@bot.event
async def on_message(message):
    global pokename
    global buscar_unidentified_image
    pokename = int(pokename)
    if message.author.id == 874910942490677270 and str(message.channel.id) in catch_id:
        if len(message.embeds) > 0:
            embed = message.embeds[0]
            if embed.image:
                pokename += 1
                image_url = embed.image.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(image_url) as response:
                        if response.status == 200:
                            async with aiofiles.open('original_image.png', mode='wb') as file:
                                await file.write(await response.read())
                        else:
                            raise
                await buscar_unidentified_image(message.channel)
    if not message.author.bot:
        if str(message.channel.id) == catch_id:
            await bot.process_commands(message)


async def buscar_unidentified_image(channel):
    global unidentified_image
    if unidentified_image is not None:
        directory = 'data/image'
        identified_words = []
        unidentified_filename = os.path.basename(unidentified_image)
        for filename in os.listdir(directory):
            if filename.endswith('.png'):
                filepath = os.path.join(directory, filename)
                if compare_images(unidentified_image, filepath):
                    identified_word = os.path.splitext(filename)[0]
                    identified_words.append(identified_word)
                    os.rename(filepath, os.path.join(directory, f'{identified_word}.png'))
        if identified_words:
            identified_words_str = ', '.join(identified_words)
            await asyncio.sleep(1)
            await channel.typing()
            pegar = random.randint(3,6)
            await asyncio.sleep(pegar)
            await channel.send(f'<@716390085896962058> c {identified_words_str}')
            print('peguei um sh ai')
    else:
        raise RuntimeError('Nao a imagem para buscar')

def compare_images(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    return image1 == image2



@bot.command()
async def oping(ctx):
    bot_ping = bot.latency * 1000  # Convertendo de segundos para milissegundos
    if bot_ping <= 300:
        await ctx.send(f'ping do autosh é: {bot_ping:.2f}ms :green_circle:')
    else:
        await ctx.send(f'ping do autosh è: {bot_ping:.2f}ms :red_circle:')
    print('Comando !ping executado')

@bot.command()
async def start(ctx):
    global paused
    if paused:
        paused = False
        await ctx.send('Bot started.')
    else:
        await ctx.send('Bot is already runninhg.')

@bot.command()
async def stop(ctx):
    global paused
    if not paused:
        paused = True
        await ctx.send('Bot stopped.')
    else:
        await ctx.send('Bot is already stopped.')
# Token do seu bot (acessado pela variável de ambiente) 
keep_alive.keep_alive()
bot.run(token) 
