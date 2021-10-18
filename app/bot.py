from discord.ext import commands
import logging
from config import read_from_env

# Read the configuration from environment variables.
bot_token, guild_ids, _ = read_from_env()

# Enable basic logging to the console.
logging.basicConfig(level=logging.INFO)

# Set up a new bot instance.
bot = commands.Bot(command_prefix="")


@bot.event
async def on_ready():
    """Show log message when Bot has connected to Discord."""
    logging.info("Bot is now online in the Discord channel.")


# Start the bot and make it connect to the Discord guild/server
# through the bot_token.
bot.run(bot_token)
