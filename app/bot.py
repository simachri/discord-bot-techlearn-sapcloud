import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content == 'hi':
        await message.channel.send('Hello, hello, hello. Welcome to the channel!')

client.run("ODM2NTM2MjQ0NzYyNDQzNzk2.YIfbFg.mY-0y-wo3bfJqQWDFDMqPTnULC0")
