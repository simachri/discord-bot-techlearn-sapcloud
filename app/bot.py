import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import logging
from requests import HTTPError
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
    logging.info("Bot is up and running.")


@slash.slash(# The name of our slash command. It will become available as '/<name>' in Discord.
             name="ping",
             # A short description what the slash command does. It will be visible in 
             # Discord.  
             description="Check if the Bot responds.",
             # We provide the guild_id of our Discord server. This is a little "trick"
             # within the Discord API to make our slash command become available in 
             # Discord right away.
             guild_ids=guild_ids)
async def pong(ctx: SlashContext):
    # Write an info log message to our console.
    logging.info("Received slash command /ping.")
    # ctx.send sends the text back to Discord.
    await ctx.send(content="Hey there, this is a message from your favourite Bot.")


@slash.slash(name="superhero",
             description="Change the bot's avatar to a random superhero image.",
             guild_ids=guild_ids)
async def change_avatar(ctx: SlashContext):
    """Change the bot's avatar to a random superhero."""
    logging.info("Received slash command /superhero.")
    try:
        # Send an initial response to Discord that the command has been received.
        # The initial response is required as the entire response might take longer
        # than three seconds for processing. If that is the case and no initial response
        # has been sent to Disocord, the interaction will fail.
        # Calling ctx.defer() shows a "bot ... is thinking." message in Discord.
        # See: https://discord.com/developers/docs/interactions/slash-commands#responding-to-an-interaction
        await ctx.defer()
        # Call the superhero API and receive a random superhero image.
        hero_name, avatar_bytes = await fetch_random_superhero_avatar()
        await bot.user.edit(avatar=bytearray(avatar_bytes.getvalue()))
        # # Optional: Embed a larger image of the super hero into the Bot's reply.
        # file = discord.File(avatar_bytes, filename="newAvatar.png")
        # embed = discord.Embed()
        # embed.set_image(url="attachment://newAvatar.png")
        # await ctx.send(content=f'Bot became {hero_name}.',
                       # file=file, embed=embed)
        await ctx.send(content=f'Bot became {hero_name}.')
        logging.info(f"Changed the bot's avatar to {hero_name}.")
    except HTTPError as err:
        logging.exception(f"Superhero API returned an error {err.response.text}.")
        await ctx.send("Calling the superhero API failed. See the console log for details.")


# Start the bot.
bot.run(bot_token)
