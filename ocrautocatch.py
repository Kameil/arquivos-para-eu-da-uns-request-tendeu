import re, os, asyncio, random, keep_alive, requests
from discord.ext import commands
from PIL import Image, ImageEnhance
from OCR_SPACE import ocr

ocr = ocr(lang='eng', api_key=os.environ['a'], overlay=False)
catch_id = [1088793731924230184]
token = os.environ['token']
catch_id2 = '1277'
paused = False
poketwo = '716390085896962058'
pokename = '0'
unidentified_image = 'original_image.png'
prefix = '|||'
embed_count = '1'
image_url = None

with open('data/pokemon', 'r', encoding='utf8') as file:
    pokemon_list = file.read()

# Configuração do bot
bot = commands.Bot(command_prefix='|||', self_bot=True)

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
    global paused
    global embed_count
    pokename = int(pokename)
    embed_count = int(embed_count)
    if message.author.id == int(poketwo) and str(message.channel.id) in map(str, catch_id):
        if message.embeds:
            embed_title = message.embeds[0].title
            if 'wild pokémon has appeared!' in embed_title:
                await message.channel.typing()
                
                pokename = 0
                print(f'pokemons spawnados: {embed_count}')
                embed_count += 1
                await asyncio.sleep(10)
                if pokename == 0:
                    if not paused:
                        timesleep = 3
                        await asyncio.sleep(1)
                        if pokename == 0:  # Adicionando uma verificação extra aqui
                            print(f'{pokename}')
                            await message.channel.send('<@716390085896962058> h')
                        
    # Verifica se a mensagem é do autor específico e está no canal correto
    if message.author.id == 874910942490677270 and str(message.channel.id) in map(str, catch_id):
        global image_url

        # Verifica se a mensagem contém uma embed
        if len(message.embeds) > 0:
            embed = message.embeds[0]
            
            # Verifica se a embed contém uma imagem
            if embed.image:
                if not paused:
                    pokename += 1
                    image_url = embed.image.url
                    try:
                        
                        text = ocr.image(image_url=image_url, timeout=9)
                        text_filtered = ''.join(char for char in text if char.isupper() or char.isspace())
                        words = [word.lower() for word in text_filtered.split() if len(word) >= 3]

                        if len(words) > 0:
                            if len(words) == 1:
                                words = words[0]
                            else:
                                words = ' '.join(words)
                        
                            await message.channel.send(f'<@716390085896962058> c {words}')
                        else:
                            r = requests.get(image_url)
                            with open('original_image.png', 'wb') as f:
                                f.write(r.content)
                            await buscar_unidentified_image(message.channel)
                    except requests.RequestException:
                        await message.channel.send('<@716390085896962058> h')


    # Verifica se a mensagem contém o texto "The pokémon is" no canal correto
    if str(message.channel.id) in map(str, catch_id) and 'The pokémon is ' in message.content:
        if message.author.bot:
            if not len(solve(message.content)):
                print('Pokemon not found.')
            else:
                for i in solve(message.content):
                    iu = i.lower()
                    timesleep = random.uniform(0.8, 2.5)
                    await asyncio.sleep(0)
                    if not paused:
                        typing_channel = bot.get_channel(int(catch_id2))
                        await asyncio.sleep(timesleep)
                        await message.channel.send(f'<@716390085896962058> c {iu}')
    if str(message.channel.id) in map(str, catch_id) and 'That is the wrong pokémon!' in message.content:
        if message.author.bot:
            timesleep = random.uniform(0.8, 2.5)
            await asyncio.sleep(0)
            if not paused:
                if pokename == 1:
                    r = requests.get(image_url)
                    with open('original_image.png', 'wb') as f:
                        f.write(r.content)
                    await buscar_unidentified_image(message.channel)
                else:
                    typing_channel = bot.get_channel(int(catch_id2))
                    await asyncio.sleep(timesleep)
                    await message.channel.send('<@716390085896962058> h')
    if str(message.channel.id) in map(str, catch_id) and 'human' in message.content: 
        typing_channel = bot.get_channel(int(catch_id2))
        if message.author.bot:
            await asyncio.sleep(2)
            if not paused:
                await message.channel.send(f'captcha detectado bot pausado.')
                paused = True
                
    if str(message.channel.id) in map(str, catch_id) and 'human' in message.content: 
        typing_channel = bot.get_channel(int(catch_id2))
        
    if str(message.channel.id) in map(str, catch_id):
        if not message.author.bot:
            await bot.process_commands(message)

def increase_resolution(image, scale_factor):
    width, height = image.size
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)
    resized_image = image.resize((new_width, new_height), resample=Image.BICUBIC)
    return resized_image

def preprocess_image(image):
    # Aumenta o contraste da imagem
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(1.0)

    # Converte para escala de cinza
    grayscale_image = enhanced_image.convert('L')

    # Aplica binarização
    threshold = 127
    binarized_image = grayscale_image.point(lambda p: p > threshold and 255)

    return binarized_image

async def buscar_unidentified_image(channel):
    global unidentified_image
    if unidentified_image is not None:
        directory = 'infos/image'  # Substitua pelo caminho do diretório onde as imagens estão armazenadas
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
            await channel.send(f'<@716390085896962058> c {identified_words_str}')
        else:
            await channel.send('Nenhuma imagem idêntica encontrada.')
            await channel.send('<@716390085896962058> h')
    else:
        await channel.send('Não há imagem não identificada para buscar.')

def compare_images(image_path1, image_path2):
    image1 = Image.open(image_path1)
    image2 = Image.open(image_path2)
    return image1 == image2



@bot.command()
async def oping(ctx):
    bot_ping = bot.latency * 1000  # Convertendo de segundos para milissegundos
    if bot_ping <= 300:
        await ctx.send(f'ping do ocr é: {bot_ping:.2f}ms :green_circle:')
    else:
        await ctx.send(f'ping do ocr è: {bot_ping:.2f}ms :red_circle:')
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
@bot.command()
async def pn(ctx):
    if ctx.author.id == bot.user.id:
        global paused
        global pokename
        if not paused:
            await ctx.send(f'{pokename}')
        else:
            await ctx.send(f'{pokename}')
# Token do seu bot (acessado pela variável de ambiente)
keep_alive.keep_alive()
bot.run(token)
  
