from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import logging
from requests import HTTPError
from config import read_from_env
from superheroes import fetch_random_superhero_avatar

# Read the configuration from environment variables.
bot_token, guild_ids, log_level = read_from_env()

# Activate application logging.
logging.basicConfig(level=log_level)

# Start the bot and make it connect to the Discord guild/server
# through the bot_token.
bot = commands.Bot(command_prefix="")


@bot.event
async def on_ready():
    """Show log message when Bot has connected to Discord."""
    logging.info("Bot is up and running.")


bot.run(bot_token)
