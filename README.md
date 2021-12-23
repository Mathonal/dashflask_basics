# dashflask_basics

the goal of this project is to compile several progressive usecases of DASH by plotli and FLASK
basic integration and exemples.

Final aim is to be able to propose :
- access to several dashboards (coded with dash) and studies integrated in one app  
- access to private dashboard linked to logged users via flask integration and loggin management
- display this kind of app in cloud services like Heroku, azure, AWS, google.

## 00_Dash_startup : 
basics components to display a DASH app via JUPYTERLAB or with server (keep the server option in mind in order)

this folder is supposed to help to set up the correct framework to be able to code and use DASH.

**JupyterLab files** : 
show lines to display dashboard directly on jupyterlab page.

few things need to be checked before running dash app in jupyter lab :

- **1** Having docker and jupyter lab : the docker image of jupyter used is based on the jupyter/all-spark-notebook (https://hub.docker.com/r/jupyter/all-spark-notebook)

the command used to run it is : <br>
***docker run -it --rm --name jupyter -p 8888:8888 -p 4040:4040 -v $HOME/work:$HOME/work -w $HOME/work jupyter/all-spark-notebook*** (replace volume (-v) and working directory (-w))

- **2** Open the 8050 port in jupyter docker run command : add -p 8050:8050 to run command (careful with port conflict id another image uses this specific port)

- **3** Missing module jupyter_dash

module jupyter_dash (and dash libraries) can be added to the docker image or can be installed with pip inside a notebook 
(either way, it is recommended to update docker image in order to keep newly installed librairies next time you run jupyter lab)

to install a new library and update your jupyter image, follow instructions :
>- copy the "requirements.txt" inside the volume directory used by Jupyter and the "Jupiterlab_DASH_update and test" notebook.
>- run jupyter image
>- open the notebook and run cells until the : pip install "requirements.txt"
>- once libraries installed, restart kernel and run the notebook to be sure that dash apps are display correctly.
>- open a terminal and run a save docker image command : <br>
>    -docker container commit 'containername' 'newimagename' <br>
>    -docker container commit jupyter myjupyter
>- close current server, run newly created jupyter image and rerun test notebook to verify that libraries are already installed at launch.

**app.py** :

dash layout for simple test application with dash server (docker image).
contains dash components listed in requirements.txt

to run the app, build **"Dash_server"** docker image from dockerfile inside project folder (instructions to build and run container inside docker file itself, entry point is "app.py" for this test; **careful with open port** in the RUN command)

(all my docker files at https://github.com/Mathonal/mydockerfiles) 

## 01_DashnFlask_basic_integration :

### Goal
to have a flask app that integrate a Dash apps.

Here we focus on the project architecture and good practices. 

### Usage

to launch this app, a flask server container is needed, with WSGI.py as entry point.

Use Dockerfile inside project folder to build the right container, also use "requirements.txt".
(instructions to build and run the container are in the dockerfile itself, **careful with open port** in the RUN command)

### Architecture

This is the most basic setup possible in order to easily understand the integration :

- **1** First level : <br> 
    - app is run in WSGI and calls __init__ in dashflask_app folder.
    - dockerfile, requirements.txt are to be used when building docker image <br>
    - .env, .gitignore and config.py are mostly there for good practice habits (they are empty or not used here) <br>

- **2** dashflask_app folder : <br>
    - flask is run in __init__, dashboard is imported in app_context
    - routes.py defines url routing (here there is only one page to display)

- **3** dash folder : <br> 
    - dashboard is called from in init_dashboard function and encapsulated in flask app
    - the dashboard_stand alone is there to compare with the encapsulated version and see differences between the two way of using a dash app. <br> 
    (the main difference is that you have to encapsulate the dashboard (object, layout, callbacks) into an init function callable from flask app)

### Credits for tutorials on this subject
dash and flask embedded : https://hackersandslackers.com/plotly-dash-with-flask/ <br>
flask factory : https://hackersandslackers.com/flask-application-factory/

## 02_DashnFlask_authentification : 
