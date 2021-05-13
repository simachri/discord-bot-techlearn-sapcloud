# Create a Discord slash command with a FastAPI server running on SAP BTP

## Docs

  - Discord Slash Commands: https://discord.com/developers/docs/interactions/slash-commands
  - Dispike - Python lib for http-based slash command server: https://github.com/ms7m/dispike


## Authorize Discord application

  1. Create a Discord server/guild.
  1. Create a new Discord application under https://discord.com/developers.
  1. Go to section _OAuth2_: 
     1. Select _SCOPES_ `applications.commands`
     1. Copy the URL and open it in the browser to authorize the application to be used 
        in the Discord server/guild.
  1. Add a _bot_ to the application.
  1. The following IDs and tokens are required:
     1. Bot token: _Bot | Click to Reveal Token_.
     1. Application ID: _General Information_
     1. Public key: _General Information_


## Create the Python app

  1. `pipenv install dispike`
  1. Create `app/main.py`.


## Deploy to BTP


## Provide the app URL to the Discord application

  Go to section _General information_ and provide the URL under _Interactions Endpoint 
  URL_ in format `<url>/interactions`.
