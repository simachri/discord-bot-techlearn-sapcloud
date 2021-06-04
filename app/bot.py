import os, sys, getopt
import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
from dotenv import load_dotenv

# Read environment variables from a .env-file. The filepath is provided
# to commandline parameter --env-file.
# - The bot token is the bot's "password"/authentication token that
#   grants access to our Discord application/guild.
BOT_TOKEN = ''
# - Our bot commdands can be defined globally or for a specific
#   guild (= specific Discord server) only.
guild_ids = None
try:
    opts, _ = getopt.getopt(sys.argv[1:], "--env-file:", ["env-file="])
    for opt, arg in opts:
        if opt == '--env-file':
            load_dotenv(dotenv_path=arg)
            BOT_TOKEN = os.environ['BOT_TOKEN']
            GUILD_ID = int(os.environ['GUILD_ID'])
            if GUILD_ID:
                guild_ids = [GUILD_ID]
            break
except:
    print("BOT_TOKEN and GUILD_ID are required as environment variables.")
    quit()



bot = commands.Bot(command_prefix="")
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print("Bot is up and running.")

@slash.slash(name="ping",
             guild_ids=guild_ids)
async def test(ctx: SlashContext):
    embed = discord.Embed(title="embed test")
    await ctx.send(content="test", embeds=[embed])



bot.run(BOT_TOKEN)

