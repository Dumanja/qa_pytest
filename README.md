# Tools

Install `PyCharm Community edition` - [Download here](https://www.jetbrains.com/pycharm/download/#section=windows)

Install `Python` - [Download here](https://www.python.org/downloads/)

Install `Git` - [Download here](https://git-scm.com/downloads)

# Install pipenv tool

Open CMD in Windows or Powershell

Check python version
`python --version`

Check pip version
`pip -V`

**If everything is installed, proceed to the Pipenv tools install.**

Install Pipenv tool
`pip install pipenv`

# How to setup project for the first time

1. Pull code from Git repo

   `git clone HTTPS_CODE_OF_THE_REPO`
   
    When code is stored some
    
    `Open PyCharm and click on Open, than find your project folder and click OK`
      
   Open Terminal inside your project from PyCharm and type:
    
          `pipenv --venv`
      
          `pipenv shell`
           
          `pipenv install`

          `pipenv install -d`


# How to have virtual environments inside project root

You should add `PIPENV_VENV_IN_PROJECT=1 and PIPENV_IGNORE_VIRTUALENVS=1` to the Windows 10 User variable.
<p align="center">  <img src="https://i.stack.imgur.com/fmUgt.png">  </p>

**Step 2:** Type “environ..” in the Windows Search Textbox. You will see “Edit the system environment variables” as a result of the Best match list. Select this option.

<p align="center">  <img src="https://i.stack.imgur.com/9vt3m.png"> </p>

**Step 3:** This will launch the System Properties window. In this window, we can review `Computer Name, Hardware, and other Advanced properties`.
 <p align="center">  <img src="https://i.stack.imgur.com/aDvFJ.png">  </p>
 
* On the `Advanced tab`, we can see `Performance`, `User Profiles`, and `Startup and Recovery` options. The last button is the `Environment Variables`. Click on this button.

**Step 4:** It will launch the Environment Variables window where you can see all variables and their values. As you can see from the following window, there are User variables and System variables. and Click on `New`
<p align="center">  <img src="https://i.stack.imgur.com/prehM.png"></p>

**Step 5:** Add `PIPENV_VENV_IN_PROJECT=1`
 <p align="center">  <img src="https://i.stack.imgur.com/schyz.png"></p>

**Step 6:** Click `OK` and Save it

**Repeat steps from 4 to 5:** Add `PIPENV_IGNORE_VIRTUALENVS=1`

**Last step:** Click `OK` and Save it

That's it's finished!

# Setup .env variables inside your project

Install dotenv:

`pipenv install python-dotenv`

Load .env file using:

Execute inside `pipenv run python` following commands:

`from dotenv import load_dotenv`

`load_dotenv()`

Use the variable with:

`import os`

`os.getenv("ACCESS_KEY")` - "ACCESS_KEY - variable name from the .env file"

When you add something in the .env file, you have to deactivate VENV and activate it again.
Do it with following commands:

Check if it's already activated with `pipenv shell`
If it's activated, deactivate with:

`deactivate`

`exit`

`pipenv shell` - to activate venv again and reload .env file