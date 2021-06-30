import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import logging
from requests import ConnectionError
from config import read_from_env
from superheroes import fetch_random_superhero_avatar

# Read the configuration from environment variables.
bot_token, guild_ids, log_level = read_from_env()

bot = commands.Bot(command_prefix="")
slash = SlashCommand(bot, sync_commands=True)

# Setup logging.
logging.basicConfig(level=log_level)


@bot.event
async def on_ready():
    """Show log message when Bot has connected to Discord."""
    print("Bot is up and running.")


@slash.slash(name="ping",
             description="Check if the Bot is available.",
             guild_ids=guild_ids)
async def pong(ctx: SlashContext):
    logging.info("Received slash command /ping.")
    embed = discord.Embed(title="Hello World!")
    await ctx.send(content="Bot is up and running.", embeds=[embed])


@slash.slash(name="superhero",
             description="Make the bot become a superhero.",
             guild_ids=guild_ids)
async def change_avatar(ctx: SlashContext):
    """Change the bot's avatar to a random superhero."""
    logging.info("Received slash command /superhero.")
    try:
        hero_name, avatar_bytes = await fetch_random_superhero_avatar()
        await bot.user.edit(avatar=bytearray(avatar_bytes.getvalue()))
        file = discord.File(avatar_bytes, filename="newAvatar.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://newAvatar.png")
        await ctx.send(content=f'Bot became {hero_name}.',
                       file=file, embed=embed)
        logging.info(f"Changed the bot's avatar to {hero_name}.")
    except ConnectionError:
        logging.exception("Superhero API returned an error.")
        await ctx.send("Calling the superhero API failed.")


bot.run(bot_token)
