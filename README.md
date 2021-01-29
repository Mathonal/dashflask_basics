# dashflask_basics
dash and flask basic integration and exemples.

### 00_Dash : 
basics components to display a DASH app via JUPYTERLAB or server.

this folder is supposed to help to set up the correct framework to be able to code and use DASH.

**JupyterLab files** : 
show lines to display dashboard directly on jupyterlab page.

few things need to be checked before running dash app in jupyter lab :

- **1** Having docker and jupyter lab : the docker image of jupyter used is based on the jupyter/all-spark-notebook (https://hub.docker.com/r/jupyter/all-spark-notebook)

the command used to run it is (replace volume (-v) and working directory (-w): 
docker run -it --rm --name jupyter -p 8888:8888 -p 4040:4040 \
-v $HOME/work:$HOME/work -w $HOME/work \
jupyter/all-spark-notebook

- **2** Open the 8050 port in jupyter docker run command : add -p 8050:8050 to run command (careful with port conflict id another image uses this specific port)

- **3** Missing module jupyter_dash

module jupyter_dash (and dash libraries) can be added to the docker image or can be installed with pip inside a notebook 
(either way, it is recommended to update docker image in order to keep newly installed librairies next time you run jupyter lab)

to install a new library and update your jupyter image, follow instructions :
- copy the "requirements.txt" inside the volume directory used by Jupyter and the "Jupiterlab_DASH_update and test" notebook.
- run jupyter image
- open the notebook and run cells until the : pip install "requirements.txt"
- once libraries installed, restart kernel and run the notebook to be sure that dash apps are display correctly.
- open a terminal and run a save docker image command : 
    docker container commit 'containername' 'newimagename'
    docker container commit jupyter myjupyter

- close current server, run newly created jupyter image and rerun test notebook to verify that libraries are already installed at launch.

**app.py** :

dash layout for simple test application with dash server (docker image).
contains dash components listed in requirements.txt

to run the app, build DASH_server docker image from : https://github.com/Mathonal/mydockerfiles (careful to use the right entry point calling "app.py")

the docker run command to use is listed in the docker file.

### 01_DashnFlask_basic_integration : 

### 02_DashnFlask_authentification : 
