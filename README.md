# rick-and-morty-django
This is a django application that provides details on all rick and morty characters.
Below, you can see a step by step tutorial showing how to run it on your computer (this tutorial assumes you have python,docker and venv already installed in your machine).

first, download the repo on the following link, then extract the project folder to the directory you want it to be located. -> https://github.com/pedromussi0/rick-and-morty-django/tree/main

if you have github CLI, run the command on your preferred directory :

```shell 
gh repo clone pedromussi0/rick-and-morty-django
```

After completing the first step, you should cd into the project directory. open up your terminal of choice and type :

```shell
cd path/to/rick-and-morty-django
```

Alternatively, you can click on the rick-and-morty-django folder,then, right click on any empty space inside the folder and then select 'open on terminal'.

now, you need to create your venv for this project. for that, run the command :

```shell
python -m venv <name-of-your-venv>
```

to activate your new venv,cd into the venv 'activate' folder, typing : 

```shell
<name-of-your-venv>\Scripts\activate
```

if you get an error, make sure to run terminal as an administrator, and then run this command : 

```shell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

after successfully activating your venv, your need to download the required dependencies for this project. To do so, simply run the command :

```shell
pip install -r requirements.txt
```

after downloading the dependencies, we are going to populate our database through a [sequence] of commands:

1st:

```shell
python manage.py update_chars
```
// This command is going to retrieve data (characters and their details) from the Rick and Morty show API and populate our database with them.
It is also going to check if a character already exists. If it does, The character won't be added. If the command runs successfully, you should get the message "DADOS SALVOS NA DB".

2nd:

```shell
python manage.py update_episodes_info
```
// This command is going to retrieve the episodes from the Rick and Morty show API, also populating the DB with them.
It is also going to prevent duplicate episodes by checking if there is already an episode with the same ID. If the command runs successfully, you should get the message "Episodes successfully populated".


After populating the database, we are going to build an image of the current project and then run that image in a docker container:

run the following commands (in sequence):

```shell
docker build -t  <name-of-your-build> 
```
//this will build the image in your remote environment,and run the necessary dependencies for the project.

after successfully running the previous command, it's time to put your image in a container. For that, run this command:

```shell
docker run -p 8000:8000 <name-of-your-build> 
```

// note that you can choose whatever port you want, if this one is already being used, switch to another one of your choice.

after running the container, you should choose your preferred browser and type 'localhost:8000'.





<h1>Now you're all set!<h1>
