import os, sys, getopt
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv
import logging

# Read environment variables from a .env-file. The filepath is provided
# to commandline parameter --env-file.
# - The bot token is the bot's "password"/authentication token that
#   grants access to our Discord application/guild.
BOT_TOKEN = ''
# - Our bot commdands can be defined globally or for a specific
#   guild (= specific Discord server) only.
guild_ids = None
# - Log level
LOG_LEVEL = logging.WARN
try:
    opts, _ = getopt.getopt(sys.argv[1:], "--env-file:", ["env-file="])
    for opt, arg in opts:
        if opt == '--env-file':
            load_dotenv(dotenv_path=arg)
            # Bot token is mandatory, so use os.environ as it raises an exception when 
            # the environment variable is undefined.
            BOT_TOKEN = os.environ['BOT_TOKEN']
            # Guild ID is optional.
            guild_id_str = os.getenv('GUILD_ID')
            if guild_id_str:
                guild_ids = [int(guild_id_str)]
            # Log level is optional.
            log_lvl = os.getenv('LOG_LEVEL')
            if log_lvl:
                LOG_LEVEL = int(log_lvl)
            break
except:
    print("BOT_TOKEN and GUILD_ID are required as environment variables.")
    quit()

# Setup logging.
logging.basicConfig(level=LOG_LEVEL)

bot = commands.Bot(command_prefix="")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Bot is up and running.")

@slash.slash(name="ping",
             description="Check if the Bot is available.",
             guild_ids=guild_ids)
async def test(ctx: SlashContext):
    embed = discord.Embed(title="Hello World!")
    await ctx.send(content="Bot is up and running.", embeds=[embed])

@slash.slash(name="getSuperhero",
             description="Send a superhero to the channel.",
             guild_ids=guild_ids)
async def post_superhero(ctx: SlashContext):
    logging.info("Received slash command /getSuperhero.")
    file = discord.File("testAvatar.png", filename="testAvatar.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://testAvatar.png")
    await ctx.send(file=file, embed=embed)

@slash.slash(name="makeSuperhero",
             description="Make the bot become a superhero.",
             guild_ids=guild_ids)
async def change_avatar(ctx: SlashContext):
    logging.info("Received slash command /makeSuperhero.")
    with open("testAvatar.png", "rb") as img:
      logging.info(f"Fetching image {img}.")
      img_bytearr = bytearray(img.read())
    # Change the bot's avatar.
    await bot.user.edit(avatar=img_bytearr)
    await ctx.send('Avatar changed.')

bot.run(BOT_TOKEN)

