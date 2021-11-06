import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext
import logging
from requests import HTTPError
from config import read_from_env
from superheroes import fetch_random_superhero_avatar

# Read the configuration from environment variables.
# - bot_token: Our authorization key/"password" for the bot to be able
#              to communicate with Discord.
# - guild_ids: List of Discord Guild/Server IDs that will use the bot.
#              The datatype is a list of IDs as the API requires a list (see below),
#              but in fact we only provide one single ID here.
# - log_level: Not used here - defines the "threshold/criticality" of messages that 
#              shall be printed to the log.
bot_token, guild_ids, _ = read_from_env()

# Create a basic bot.
bot = commands.Bot(command_prefix="")
# Make the bot handle slash commands.
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    """Show log message when Bot has connected to Discord."""
    logging.info("Bot is up and running.")

@bot.event
async def on_message(message: discord.Message):
    """Reply to any 'Hello bot' message in the channel."""
    logging.info(f"Received message '%s' from user %s.", message.content, message.author.display_name)
    # Ignore any message that has been sent by the bot.
    if message.author == bot.user:
        return

    if message.content == 'Hello bot':
        channel = message.channel
        await channel.send('Hi there, hope you are doing well.')


@slash.slash(name="ping", # The name of our slash command. It will become available as '/<name>' in Discord.
             description="Check if the Bot responds.", # Description what the slash command does.
                                                       # It will be visible in Discord.  
             guild_ids=guild_ids # See the explanation above regarding guild_ids.
             )
async def pong(ctx: SlashContext):
    """Respond to the /ping command"""
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
        
        if bot.user == None:
            logging.error("User is not logged in.")
            return 
        await bot.user.edit(avatar=bytearray(avatar_bytes.getvalue()))
        # Optional: Embed a larger image of the super hero into the Bot's reply.
        file = discord.File(avatar_bytes, filename="newAvatar.png")
        embed = discord.Embed()
        embed.set_image(url="attachment://newAvatar.png")
        await ctx.send(content=f'Bot became {hero_name}.',
                      file=file, embed=embed)
        #await ctx.send(content=f'Bot became {hero_name}.')
        #logging.info(f"Changed the bot's avatar to {hero_name}.")
    except HTTPError as err:
        logging.exception(f"Superhero API returned an error {err.response.text}.")
        await ctx.send("Calling the superhero API failed. See the console log for details.")


# Start the bot.
bot.run(bot_token)
