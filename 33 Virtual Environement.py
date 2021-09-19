# first install virtual Environment
# install "pip install virtualenv"
"""Steps-
 1. Create Folder after that in directory write powershell to open window powershell.

 2. Write a "virtualenv" here you get the details about the version and help command like that.
    Creates a new python based on python interpreter create new python virtual interpreter.

 3. To Create new virtual python means a new born of python:- command - virtualenv "name of folder."

 4. Now We Have To Activate the virtual Environment by writing - .\(name of the folder)\Scripts\activate
    If get the error then don't worry, follow steps-
    a. open window powershell administrator.
    b. write set-executionpolicy remotesigned

 5. If you want to deactivate virtual python then "deactivate". """


"""Note:-  a. If you want to install specific version then write "pip install numpy==1.15.4
           b. If you want to uninstall any package then write " pip uninstall package name(sklearn)". """

# NOW LEARN ABOUT requirement.txt

""" Lets talk about requirement.txt, let that we have made this file 5 years ago. Now we have to give somebody
    then in 5 years python got many updates that means package time was updated or removed if give to her
    then he unable to access to file. So we require a requirement.txt file. In this file all the versions of 
    package are given so that we can install any specific package with it version. Let's see how to install-
    
    a. "pip freeze > requirement.txt"
    
    b. Let that in requirement.txt has many package more than 500 than you cant install one by one. then the command is-
       firstly copy requirement.txt were your virtual folder is located. After that run command on powershell-
       "pip install -r .\requirement.txt """

# NOW

""" If we want to install same package in virtual python that packages which are installed in my system python
    then we have write a command on powershell (note :- it will create a new python virtual environment
    
    "virtual --system-site-packages (name of the folder your choice.)"""