# How to setup Pipenv project

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
