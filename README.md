# Create a Discord bot running on SAP Business Technolgy Platform

## Getting started

  1. Login to the SAP Business Technology Platform (BTP): Go to 
     https://account.hanatrial.ondemand.com/cockpit/ and sign in using the email address 
     and password provided to you by the trainer.
  1. On the _Welcome to SAP BTP Trial_ screen, click on _SAP Business Application Studio_ 
     (top left element under _Quick Tool Access_).
  1. You see a Dev Space __python_discord_bot__. Click the _"Play"_ button right next to 
     it and wait 30 seconds until it says _RUNNING_. Click on the Dev Space. This will 
     start up the development environment.

  __Note__: After he workshop has finished, you can create your own BTP trial account and
  set up the project from scratch. The BTP trial account is free for one year and can be 
  terminated at any time. [This is the guide how to set up the project on your own](Project_Setup.md).


## Business Application Studio (BAS)

  1. In BAS, clone the repo and provide the access token.
  1. Install Python by following this 
     [guide](https://blogs.sap.com/2020/12/12/xtending-business-application-studio-3-of-3/).
  1. Install extension _Python_.
  1. `pip`should be available on `PATH`. Install `pipenv`:
     `pip install pipenv`
  1. Start the virtual environment and install the project dependencies:
     - `pipenv shell`
     - `pipenv install`
  1. Install the extension _Python_. __Ignore__ the error that there is no Python 
     installed.
  1. Set the Python interpreter such that the extension works:
     - _File | Settings | Open Preferences... | User | Python | Default Python Interpreter_
     - Set `/home/user/<Python version>/bin/python`
     - Do the same in the _Preferences_ under _Workspace_.
     - To set the Python environment for the concrete project folder, 
       create/edit file `.vsocde/settings.json` and add an entry 
       `"python.pythonPath": "/home/user/.local/share/virtualenvs/<virtual env>/bin/python"`

  1. If _Linter pylint is not installed._ pops up, select _Install_. This will install it
     using `pip`.

  1. Create a _run and debug configuration_:
     1. _Run | Add Configuration..._
     1. Provide the following contentn to `launch.json`:
        ```json
          "version": "0.2.0",
          "configurations": [
              {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal"
              },
              {
                "name": "Python: Discord Bot",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/app/main.py",
                "console": "integratedTerminal",
                "envFile": "${workspaceFolder}/.env.dev"
              }      
            ]
        }
        ```

## Deploy the Bot coding as application to the Cloud Foundry runtime environment

  1. Go to _Terminal | New Terminal_.
  1. In the terminal run: `cf push`

     __Note__: The following warnings can be __ignored__:
     - _WARNING:  The script %s is installed in '%s' which is not on PATH._
     - _No start command specified by buildpack or via Procfile._
     - _App will not start unless a command is provided at runtime._


## Docs of the Python libraries/modules

  - Official Discord Slash Commands docs: 
    https://discord.com/developers/docs/interactions/slash-commands
  - Library `discord.py`: https://discordpy.readthedocs.io/en/stable/api.html
  - Library `discord-py-slash-command`, that extends `discord.py`: 
    https://pypi.org/project/discord-py-slash-command/
  - Superhero database API: https://akabab.github.io/superhero-api/api/
