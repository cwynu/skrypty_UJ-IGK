

from discord.ext import commands
TOKEN = "OTgwMDYwNzA2MzIzOTcyMTQ3.G1kUQD.YHrlVO_sPso0-pk0_vBq7MzXRBiKQ0ldlKCOSU"

# Initialize Bot and Denote The Command Prefix
bot = commands.Bot(command_prefix="!")

# Runs when Bot Succesfully Connects
@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'Czesc':
        await message.channel.send(f'Siemanko {message.author}')
    if message.content == 'Kim jestes?':
        await message.channel.send(f'Jestem BOTem, tutaj, na discordzie')
    if message.content == 'Pa':
        await message.channel.send(f'To do zoabczenia {message.author}')

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def square(ctx, arg):
    print(arg) 
    await ctx.send(int(arg) ** 2) 

bot.run(TOKEN)