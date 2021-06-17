from discord.ext import commands
import logging
from config import read_from_env

# Read the configuration from environment variables.
bot_token, guild_ids, log_level = read_from_env()

# Activate application logging.
logging.basicConfig(level=log_level)

# Start the bot and make it connect to the Discord guild/server
# through the bot_token.
bot = commands.Bot(command_prefix="")
bot.run(bot_token)
