import os
import sys
import getopt
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv
import logging
import requests
from io import BytesIO

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


async def fetch_random_superhero_avatar():
    """Fetch a random superhero avatar from https://akabab.github.io/superhero-api/api/.
      Returns:
        The avatar image binary data.
    """
    # Use the cached URL: https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api
    response = requests.get("https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/id/1.json")
    if response.status_code != 200:
        return
    hero_data = response.json()
    hero_avatar_url = hero_data["images"]["xs"]
    response = requests.get(hero_avatar_url, stream=True)
    if response.status_code != 200:
        return
    return BytesIO(response.content)


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
    # file = discord.File("testAvatar.png", filename="testAvatar.png")
    file = discord.File(await fetch_random_superhero_avatar(), filename="testAvatar.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://testAvatar.png")
    await ctx.send(file=file, embed=embed)


@slash.slash(name="makeSuperhero",
             description="Make the bot become a superhero.",
             guild_ids=guild_ids)
async def change_avatar(ctx: SlashContext):
    logging.info("Received slash command /makeSuperhero.")
    # with open("testAvatar.png", "rb") as img:
        # logging.info(f"Fetching image {img}.")
        # img_bytearr = bytearray(img.read())
    ## Change the bot's avatar.
    # await bot.user.edit(avatar=img_bytearr)
    # Change the bot's avatar.
    avatar_bytes = await fetch_random_superhero_avatar()
    await bot.user.edit(avatar=bytearray(avatar_bytes.getvalue()))
    await ctx.send('Avatar changed.')

bot.run(BOT_TOKEN)
