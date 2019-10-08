# Learn Python
This git repo is the history of all the steps a had to do when i was learning python.  
This is not simply python the language but also the how to make a good dev environment.  
Sorry for my english...

I will work on windows platform, but will use cmder or gitbash for some commands,  
so there will be some unix commands also.

## First Steps
 First, create the folder for the project and make the python virtual env 
```
mkdir learnpython
cd learnpython
virtualenv pythonvenv
```
Then we activate the venv (here pythonvenv)
```
pythonvenv\Script\activate
```

(pythonvenv) should prompt on your command 

add your work folder to the pythonpath !
Find yout fullpath 
```
pwd
```
then it to the pythonpath
```
set PYTHONPATH=%PYTHONPATH%;C:\Users\fabas\Desktop\dev\git\learnpython
```  

if you want to see if the folder is in the PYTHONPATH you can invoke the python command, then import sys, and print sys.path

## pip command
 https://pypi.org/project/pip/
 pip is a python command, you can dowload with it a lot of package.  
 in a virtualenv you can found those packages in venv\site-packages\  
 We are going to install this packages first :
```
pip install black
pip install pylint
```
black : code formatter , more info https://pypi.org/project/black/  
pylint : linter , https://pypi.org/project/pylint/

### usefull links :
info on vscode/python : https://py-vscode.readthedocs.io/en/latest/index.html