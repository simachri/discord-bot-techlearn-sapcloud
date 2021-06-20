# How to set up the project from scratch

  1. Create a Business Technolgy Platform (BTP) trial account. 
     1. Go to https://www.sap.com/products/business-technology-platform/trial.html
     1. Click on button _Start your free trial_.
     1. Finalize the account creation through the link in the email that is sent to 
        you.

  1. Sign in to your BTP account: https://account.hanatrial.ondemand.com/cockpit/

     __Note__: When signing-in for the first time, select the region that is nearest to your 
     location and wait until the account is set up for.

  1. Launch the _SAP Business Application Studio_ (BAS) which is SAP's online development
     environment to create cloud applications. 
     1. On the _Welcome to SAP BTP Trial_ screen, click on _SAP Business Application 
        Studio_ (top left element under _Quick Tool Access_).
     1. Click the button _Create Dev Space_.
     1. On the top left corner, provide a name for your Dev Space. In our workshop, we 
        used __python_discord_bot__.
     1. On the left hand side under _What kind of application do you want to create_, 
        select _Basic_.
     1. No _Additional SAP Extensions_ (right hand side) are required. Click the button 
        _Create Dev Space_.

     __Note__: The Dev Space is automatically stopped when you are not using it. When its
     status is _STOPPED_ press the _Play_ button right next to your Dev Space if it is 
     stopped and wait until it has started up again.

  1. In the BAS, clone the project source code to start the project:
     1. Click the button _Clone Repository_ and provide the URL to the GitHub 
        project repository: https://github.com/simachri/sap-learnfest-discord-bot-starter
     1. In the popup _Open_ select the folder _projects_ and click button _Select 
        Repository Location_. This is where the files from the GitHub repository are 
        copied to.
     1. Once cloning has finished, open the folder where the files have been cloned to: 
        Go to _File | Open Workspace | sap-learnfest-discord-bot-starter_. On the left 
        hand side under _Explorer_ you now see all the project files.

  1. The BAS Dev Space currently does not have a _Python runtime environment_ installed 
     for being able to run our bot coding.
     1. Install the _Python runtime environment_:
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
        1. Tell the Dev Space the location of the installed Python: Go to _View | Find 
            Command..._ search for _'python'_ and select _

     1. Install the _Python_ extension:
        1.  On the toolbar on the left hand side, click the button _Extensions: Open VSX 
            Registry_.
        1. In the search field, search for _'python'_, select __Python__ and click the button 
            _Install_ right next to it and wait until it is installed (the button changes to 
            _Uninstall_).
        1. Tell the BAS the location of our Python runtime environment: Go to _View | Find Command..._, search 
           for _'python'_ and select _Python: Select Interpreter_.
           - [ ] Is this really required?

     1. Install _pipenv_ which is used to manage the dependencies of the application such
        as the Discord library:
        1. Open a terminal through _Terminal | New Terminal_.
        1. Run `pip install --user pipenv`.


