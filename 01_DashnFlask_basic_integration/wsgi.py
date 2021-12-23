"""Application entry point."""
from dashflask_app import init_app
import os

# THIS CONFIGURAION SETUP IS DESTINED TO HEROKU CLOUD

# to test prod env on heroku, uncomment next line
# os.environ['ISHEROKU'] = 'True' 
# note : cannot set boolean in environment variables

# it is mandatory to have SECRET_KEY environment variable :
# 1 - in local .env file (this file is not push in GIT)
# 2 - defined in Heroku application environment

# ENVIRONMENT CHECK
herokuflag = os.getenv('ISHEROKU', 'dontexist')
# normally give 'True', or 'dontexist' if not found

if herokuflag == 'True' : ENV_LEVEL = 'production'
else: ENV_LEVEL = 'development'
#confirmation on APP launch
print("App launch in {} mode because os.environ[ISHEROKU]: {}".format(
    ENV_LEVEL,herokuflag))

# APPLICATION LAUNCH
app = init_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)