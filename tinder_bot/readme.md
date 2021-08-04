# Tinderbot
Organic marketing through Tinders' platform.

## Requirements
* Python 3
* ChromeDriver 

## Installation and Organization

### Introduction and Conventions

Being organized with software projects can reduce headaches and confusion later
on by minimizing headaches from mismatched versions of files and packages. 
While your project organization is ultimately up to you, you may find this
example helpful as a starting point. 

*  Notes
    *  On Unix-based systems like macOS and Linux, the `~` character is 
shorthand for the home directory. For simplicity, we will maintain that
convention for Windows as well. 
    *  We will also denote values that should be changed by you, the end user, in 
brackets like this: `<insert_your_value_here>`
    *  Finally, we will be writing terminal commands as they apply to Unix-based
terminals. Windows users should either use the Windows Subsystem for Linux
in order to get a Unix-based terminal or adjust the commands appropriately for
their Windows environment. 

Home directory locations are typically like this

*  Windows: `C:\Users\<your_username>\`
*  macOS: `/Users/<your_username>/`
*  Linux: `/home/<your_username>/`

### Setup Steps

1. Decide where you want to keep the code and associated files. 
    *  Example: `~/Projects/`
   
2. Clone the git repository.
    *  Example
        *  cd `~/Projects`
        *  `git clone https://<bitbucket_username>@bitbucket.org/jigtalkteam/tinder_bot.git`
      
3. Create a new branch for your own work. 
   It should be based off the `onboarding` branch.
    *  `git checkout onboarding`
    *  `git checkout -b onboarding-<your_initials>`
      
4. Install ChromeDriver
    *  Start by downloading ChromeDriver for your OS from
       `https://chromedriver.chromium.org/downloads`
    *  Once downloaded, unzip the zip file and move the executable to your preferred location.
        *  Example: `~/Projects/tinder_bot/chromedriver`
    *  `chromedriver` and `chromedriver.exe` are in the `.gitignore` file
   
5. (Optional, but recommended) Create a virtual environment. 
   Virtual environments are useful for isolating project packages away from 
   system packages, so that everything can stay nicely self-contained.
   A descriptively named environment makes it easy to keep track of what 
   environment you are using, i.e. `<tinder_bot_env>` is more obvious than
   `venv` or `myenv`. This makes it easier to keep track of things when working
   on multiple projects. 
    *  `python3 -m venv <virtual_environment_name>`
    *  `source <virtual_environment_name>/bin/activate`
    
6. Install dependencies
    *  `pip install -r requirements-<operating_sysmtem>.txt`
   
7. Set the environment variables needed for using your Tinder account
    *  Copy `.env.example` into a new file called `.env`
    *  Edit `.env` to set the following environment variables:
        *  `FACEBOOK_USERNAME`
        *  `FACEBOOK_PASSWORD`
        *  `CHROME_DRIVE_LOCATION`
    *  Don't worry, the `.env` file is inluced in the `.gitignore` file

#### Note: - Disable Facebook's 2 Factor Authentication for the bot to work without any hiccups.

### Getting Started with Tinderbot 

In general, the bot can be run with

```
python3 main.py <number_of_swipes> <like_fraction>
```
Optionally, you may wish to use

```
python3 main.py <number_of_swipes> <like_fraction> --debug
```

*  `<number_of_swipes>` is the number of swipes to perform (duh)
*  `<like_fraction>` is the probability of each swipe being a like

Example: Perform 10 swipes with an 80% chance for each swipe to be a like

```
python3 main.py 10 0.8
```

However, the code you receive from the `onboarding` branch will not work right away.
There are tasks for you to complete in order to get the bot fully working. 
The tasks are to encourage you to get familiar with the code and other tools
for web development and analytics so that you can build you skill set.

Your first tasks:

1. Complete the `_set_notification_permission` and `_accept_cookies` methods
   in `TinderSession.py`
2. Update `main.py` to use the `process_permissions` method 
   from `TinderSession.py`
3. Start getting some initial swipes with the debug flag to step through things
   more slowly.
4. You will run into pop ups that are not currently handled. Update the 
   `_get_pop_up` method in `TinderSession.py` to handle these cases.
5. Once you're satisfied with the performance of the code, work on adding in
   radomization features to appear more human. For example, rather than running
   in one session that does all the specified swipes, you can have it split the
   total number of swipes among a random number of sessions, spaced apart by 
   random amounts of time.
   
You are of course free to change and tweak whatever you want on your own branch,
as well as to experiment with new ideas! We look forward to seeing what you all
come up with.
