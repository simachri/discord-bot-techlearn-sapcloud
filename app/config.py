import os
import sys
import getopt
import logging
from dotenv import load_dotenv
from typing import Optional


def read_from_env() -> tuple[str, Optional[list[int]], int]:
    """ Read the application configuration from environment variables.

        If the program is invoced with commandline parameter --env-file <filepath>,
        the .env-file from the given filepath is read.

        :returns:
        - bot_token (str): The bot token is the bot's "password"/authentication token 
          that grants access to our Discord application/guild.

        - guild_ids (list[int] or None): The bot commdands can be defined globally or for a specific
            guild (= specific Discord server) only. Specifying it only for a specific guild
            makes the commands be updated/available much faster in the Discord channel.

        - log_lvl (int): Defines how detailed the log output of the application is.
    """
    # Set some defaults for fallback.
    bot_token = ''
    guild_ids: Optional[list[int]] = None
    log_lvl: int = logging.WARN

    # Parse the commandline parameter to read the path to the .env file..
    # This is optional. The environment variables might be already set in the system
    # environment.
    opts, _ = getopt.getopt(sys.argv[1:], "--env-file:", ["env-file="])
    for opt, arg in opts:
        if opt == '--env-file':
            # Load the environment variables from the .env-file.
            load_dotenv(dotenv_path=arg)
            break

    # Bot token is mandatory, so use os.environ as it raises an exception when
    # the environment variable is undefined.
    try:
        bot_token = os.environ['BOT_TOKEN']
    except KeyError:
        print("BOT_TOKEN is required as environment variable.")
        quit()

    # Guild ID is optional.
    guild_id_str = os.getenv('GUILD_ID')
    if guild_id_str:
        guild_ids = [int(guild_id_str)]

    # Log level is optional.
    log_lvl_str = os.getenv('LOG_LEVEL')
    if log_lvl_str:
        log_lvl = int(log_lvl_str)

    return bot_token, guild_ids, log_lvl
