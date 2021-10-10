# Workshop: Create your first Discord bot running on SAP Business Technolgy Platform

  This repo is the basis of the workshop to create your first Discord bot using the 
  programming language Python and the SAP Business Technology Platform (BTP) for deployment.

## Recap

  Three steps are required to get your first Discord bot up and running:
  1. [Prepare your bot on your Discord server](docs/Project_Setup#prepare_discord_bot_appl).

  1. Set up your __development environment__ to write the bot coding. There are multiple 
     alternatives:
     - [Alternative A](docs/Project_Setup#proj_setup_use_workshop_account): __SAP 
      Business Application Studio__ used in the __workshop__ and suitable for the workshop 
      participants who have gathered a BTP trial account.

     - [Alternative B](docs/Project_Setup#proj_setup_bas): Use the 
       __SAP Business Application Studio__, an online development environment that runs 
       in the browser and does not required any local software installation.

     - [Alternative C](docs/Project_Setup#proj_setup_local): Develop the bot __locally on 
       your machine__. This requires more preparation.

  1. [Deploy](docs/Project_Setup#deployment_cf) the bot coding in a container to the 
     __SAP Cloud Foundry runtime environment__.


## Docs

  - Python Discord Bot Library: 
    - Extended library providing __Slash Commands__: `discord-py-interactions`
      - [GitHub](https://github.com/goverfl0w/discord-interactions)
      - [Docs](https://discord-interactions.readthedocs.io/en/latest/)
      - [Discord Server](https://discord.gg/J93paqGK)
    - Core library that is used by `discord-py-interactions`: `discord.py`
      - [GitHub](https://github.com/Rapptz/discord.py)
      - [Docs](https://discordpy.readthedocs.io/en/latest/)
      - [Discord Server](https://discord.gg/dpy)

  - Discord Slash Commands reference: 
    https://discord.com/developers/docs/interactions/slash-commands

  - Superhero database API: https://akabab.github.io/superhero-api/api/


## Final coding example

  See the branch `final_coding` the get an idea how the final coding after the workshop 
  can look like.
