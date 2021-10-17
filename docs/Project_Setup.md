# Project setup

## Prepare your bot on your Discord server
<a id="prepare_discord_bot_appl"></a>

  1. Create a new Discord server (called a _guild_ in Discord wording) or use an existing
     one that you own.
  1. Go to https://discord.com/developers/applications and create a new Discord _application_.
  1. Go to menu item _Bot_ and add a _bot_ to the application.
  1. Go to section _OAuth2_: 
     1. Select _SCOPES_:
        - `applications.commands`
        - `bot`
          - `Use Slash Commands`
          - `Send Messages`
     1. Copy the URL and open it in the browser to authorize the application to be used 
        in the Discord server/guild.
  1. Take the Bot token: _Bot | Token_ and press the button _Copy_ or _Click to Reveal Token_.
     The Bot token needs to be provided as `BOT_TOKEN` to the file [.env.dev](#env_vars), 
     see below.


## Setting up your development environment

### Alternative A: SAP Business Application Studio (BAS) with workshop account
<a id="proj_setup_use_workshop_account"></a>

  The BAS is an online development environment that runs in the browser and does not 
  required any local software installation.

  This alternative is for you if you have participated in the workshop and already 
  received an SAP BTP trial account.

  1. Login to the [SAP Business Technology Platform (BTP)](https://account.hanatrial.ondemand.com/cockpit/)
     and sign in using the email address and password provided to you by the trainer.
  1. On the _Welcome to SAP BTP Trial_ screen, click on _SAP Business Application Studio_ 
     (top left element under _Quick Tool Access_).
  1. You see a Dev Space __python_discord_bot__. Click the _"Play"_ button right next to 
     it and wait 30 seconds until it says _RUNNING_. Click on the Dev Space. This will 
     start up the development environment.

  __Note__: After he workshop has finished, you can create your own BTP trial account and
  set up the project from scratch. The BTP trial account is free for one year and can be 
  terminated at any time. [This is the guide how to set up the project on your own](Project_Setup.md).


### Alternative B: SAP Business Application Studio (BAS)
<a id="proj_setup_bas"></a>

  The BAS is an online development environment that runs in the browser and does not 
  required any local software installation.

  __Prerequisite:__ A free BTP trial acoount is required.
  Go [here](https://www.sap.com/products/business-technology-platform/trial.html#individual-users)
  to create an account.

  1. Sign in to the [BTP](https://account.hanatrial.ondemand.com/cockpit/) using your 
     trial acoount. 

     __Note__: When signing-in for the first time, select the region that is nearest to your 
     location and wait until the account is set up for.

  1. On the _Welcome to SAP BTP Trial_ screen, click on _SAP Business Application 
     Studio_ (top left element under _Quick Tool Access_).
  1. Click the button _Create Dev Space_.
  1. On the top left corner, provide a name for your Dev Space. In our workshop, we 
     used __python_discord_bot__.
  1. On the left hand side under _What kind of application do you want to create_, 
     select _Basic_.
  1. On the right hand side under _Additional SAP Extensions_ select __MTA Tools__. It
     is required such that we can deploy our application to the [Clound Foundry Environment](#cf_setup)
     later.
  1. Click the button _Create Dev Space_.

     __Note__: The Dev Space is automatically stopped when you are not using it. When its
     status is _STOPPED_ press the _Play_ button right next to your Dev Space if it is 
     stopped and wait until it has started up again.

  1. In the BAS, __clone__ the 'getting started' source code from the _GitHub repo_:
     1. Click the button _Clone Repository_ and provide the URL to the GitHub 
        project repository: https://github.com/simachri/discord-bot-techlearn-sapcloud
     1. Once cloning has finished, open the folder where the files have been cloned to: 
        Go to _File | Open Workspace | discord-bot-techlearn-sapcloud_. On the left 
        hand side under _Explorer_ you now see all the project files.

  1. The BAS Dev Space currently does not have a _Python runtime environment_ installed 
     for being able to develop and run our Bot coding. So, install the _Python runtime 
     environment_:
     1. On the toolbar on the left hand side, click the button _Extensions: Open VSX 
        Registry_.
     1. In the search field, search for _'python'_, select __SAP BAS Python 
        Installer__ and click the button _Install_ right next to it and wait until it 
        is installed (the button changes to _Uninstall_).
     1. Execute the command to install Python: Go to _View | Find Command..._, search 
        for _'BAS'_ and select _BAS: Install Python 2.9.0_.

        __Note__ It will install __Python 3.9.0__ although the command says _2.9.0_.

     1. Wait half a minute or so until it is installed. Unfortunately, there is no 
        notification that the installation has finished.

        __Note__: If no folder `user/python_*` is created and Python is not available, restart the 
        Dev Space and run the command again.

     1. Install _pipenv_ which is used to manage the dependencies of the 
        application such as the Discord library:
        1. Open a terminal through _Terminal | New Terminal_.
        1. Run `pip install pipenv`.

  1. Install all our project dependencies that are defined in the `Pipfile`: 
     1. Create a folder `.venv` such that `pipenv` installs the dependencies into this 
        folder.
     1. Open a terminal through _Terminal | New Terminal_.
     1. Run `pipenv install`.

  1. Install the _Python_ extension:
     1. On the toolbar on the left hand side, click the button _Extensions: Open VSX 
        Registry_.
     1. In the search field, search for _'python'_, select __Python__ and click the button 
        _Install_ right next to it and wait until it is installed (the button changes to 
        _Uninstall_).

  1. In the `.env.dev` file replace the `Bot token` with the actual Bot token.

  1. Verify that everything works:
     1. On the toolbar on the left hand side, click the button _Debug_.
     1. In the dropdown menu select the run configuration _Python: Discord Bot_.
     1. Start the application by clicking the _"Play"_ button.

  1. If a message _Linter pylint is not installed._ pops up when running the application, 
     select _Install_. A linter is a helper tool for analyzing your source code to find 
     errors and provide style guides.


### Alternative C: Local development
<a id="proj_setup_local"></a>

  You can develop the Bot locally on your machine using your favorite IDE/coding editor. 
  This requires some additional setup steps.

  1. Install your favorite __IDE/coding editor__. Here are some examples:
     - [Visual Studio Code (VSCode)](https://code.visualstudio.com/)
     - [PyCharm](https://www.jetbrains.com/pycharm/)
     - [Neovim](https://neovim.io/))

     __Note__: The steps below contain information on how to set up the project using 
     _VSCode_ but can be adapted to any other editor:

  1. Install [Python](https://www.python.org/downloads/).
  1. Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).
  1. Install the commandline Interface to deploy the application to the SAP BTP Cloud Foundry 
     environment: [cf7 CLI](https://github.com/cloudfoundry/cli/blob/master/doc/installation-instructions/installation-instructions-v7.md#installers-and-compressed-binaries) 
  1. Launch your __IDE/editor__ and clone the GitHub project. 
     1. Open the _Explorer_ view (topmost button on the left hand side toolbar).
     1. Click _Clone Repository_ and provide the GitHub repo: 
        https://github.com/simachri/discord-bot-techlearn-sapcloud
     1. Once the clone process has finished, make VSCode open the project folder.
     1. Install the _Python extension_, available under _Extensions_ on the toolbar on 
        the left hand side.

  1. Install _pipenv_ which is used to manage the dependencies of the bot 
     application such as the Discord library:
     1. Open a terminal _Terminal | New Terminal_.
     1. Run `pip install pipenv`.

  1. Install all our project dependencies that are defined in the `Pipfile`: 
     1. Create a folder `.venv` in the project folder such that `pipenv` installs the 
        dependencies into this folder.
     1. Open a terminal through _Terminal | New Terminal_.
     1. Run `pipenv install`.

  1. In the `.env.dev` file replace the `Bot token` with the actual bot token that has 
     been generated when you set up the bot in Discord, see 
     [here](#prepare_discord_bot_appl).

  1. Verify that everything works:
     - _VSCode_:
       1. On the toolbar on the left hand side, click the button _Debug_.
       1. In the dropdown menu select the run configuration _Python: Discord Bot_.
       1. Start the application by clicking the _"Play"_ button.

     - alternatively, using the commandline:
       `python app/bot.py --env-file .env.dev`


## Deployment to the BTP Cloud Foundry runtime environment
<a id="deployment_cf"></a>

  The BTP provides a runtime environment called _Cloud Foundry_ (CF) to run your Bot without 
  having to interactively start and stop it in the BAS. 

  __Prerequisite:__ A free BTP trial acoount is required.
  Go [here](https://www.sap.com/products/business-technology-platform/trial.html#individual-users)
  to create an account.

### One-time setup: Connect your project with the CF environment
<a id="cf_setup"></a>

  Open your Dev Space in the BAS:
  1. Go back to https://account.hanatrial.ondemand.com/cockpit/
  1. Launch the _SAP Business Application Studio_ and open your Dev Space 
     __python_discord_bot__.
  1. Login to the SAP Cloud Foundry Environment:
     - In _BAS or VSCode_: Go to _View | Find command... | CF: Login to Cloud Foundry_
     - Alternatively, using the commandline: `cf login`

  1. Provide the _API endpoint_ URL of your CF environment. You can finde it using the 
     following steps:
     1. Sign in to your BTP account: https://account.hanatrial.ondemand.com/cockpit/
     1. Click the button _Enter Your Trial Account_.
     1. The _SAP BTP Cockpit_ opens and shows the _Subaccounts_ page.
     1. Click on the large tile _trial_ to enter your trial subaccount.
     1. The trial subaccount opens and shows the _Overview_ page.
     1. On the tab _Cloud Foundry Environment_ see the value of _API Endpoint_. If the CF 
        is running in Frankfurt, Germany, it looks like this 
       `https://api.cf.eu10.hana.ondemand.com`. This is the URL you need.

  1. Provide the same login credentials that you use when logging in to the BTP.
  1. For _Organization_ select the proposed one.
  1. For _Space_ select the proposed one.

### One-time setup: Prepare the deployment

  1. If you have added new Python modules/dependencies to your application by using 
     `pipenv install <module>`, update the `requirements.txt` from the `Pipfile`: 
     `pipenv lock --keep-outdated -r > requirements.txt`

  1. Create a `manifest.yml`. The file is evaluated by the CF environment and contains all the information
     how to deploy your Bot as application on the CF. Make sure to adjust the value for 
     `BOT_TOKEN`
     ```yaml
      ---
      applications:
      - name: discord-slash-cmd
        buildpacks:
          - python_buildpack
        host: learningfestival
        path: .
        memory: 128M
        env:
          BOT_TOKEN: '<insert the Bot token from the Discord developer portal>'
          LOG_LEVEL: '30'
        command: python app/bot.py
        health-check-type: none
     ```
  1. Create a `runtime.txt` containing the Python version that is required to run the 
     application. Available versions are listed in the CF buildpack release 
     [notes](https://github.com/cloudfoundry/python-buildpack/releases).
     ```
     python-3.9.x
     ```

  1. Provide the dependencies as "vendor dependencies" such that no network calls are 
     required during build time:
     `pip download -d vendor -r requirements.txt --platform manylinux1_x86_64 --platform manylinux2014_x86_64 --only-binary=:all:`

### Push your Bot coding as containerized application to the Cloud Foundry runtime environment

  Open up a terminal (in BAS and VSCode go to _Terminal | New Terminal_) and run:
  `cf push`

   __Note__: The following warnings can be __ignored__:
   - _WARNING:  The script %s is installed in '%s' which is not on PATH._
   - _No start command specified by buildpack or via Procfile._
   - _App will not start unless a command is provided at runtime._
