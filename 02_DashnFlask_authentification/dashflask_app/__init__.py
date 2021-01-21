"""Initialize Flask app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

from .baseauth.models import User
def register_extensions(app):
    # USERDATABASE
    db.init_app(app)

    # LOGIN MANAGEMENTS
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, 
        # use it in the query for the user
        return User.query.get(int(user_id))

def register_dashboards(app):
        # Import Dash applications from dash folder
        # generics Dash
        from .dash.genericDash import dashboard1,dashboard2
        app = dashboard1.Add_Dash(app)
        app = dashboard2.Add_Dash(app)
        # ...

        # Private Dash
        from .dash.privateDash import dashboard1_testname,dashboard2_testname2
        app = dashboard1_testname.Add_Dash(app)
        app = dashboard2_testname2.Add_Dash(app)
        # ...


def create_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # initialise plugins
    register_extensions(app)

    # vital section : "here are all the pieces of my program"
    with app.app_context():

        #RESET DB in dev env
        if app.config['FLASK_ENV'] == 'development':
            from .baseauth import models
            models.init_db()

        # blueprint for auth routes in our app
        from .baseauth.authroutes import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # blueprint for DASHAPPS of app
        from .dash.dashroutes import dashr as dash_blueprint
        app.register_blueprint(dash_blueprint)

        # Import Dash applications from dash folder
        register_dashboards(app)

        return app