from flask import Blueprint, render_template, redirect, \
    url_for, request, flash
#from flask import session 

from flask_login import login_user, logout_user, \
    login_required, current_user
from .models import User
from .. import db
from .utils_db import find_dashboardlist

auth = Blueprint('auth', __name__,
        template_folder='templates',
        static_folder='static')

@auth.route('/')
def index():
    return render_template('index.html')

# ================
@auth.route('/login', methods=['GET'])
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    # =====
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    # check if the user actually exists
    user = User.query.filter_by(email=email).first()

    # compare user-supplied password to the hashed password in the database
    if user and user.check_password(password=password):
        # create session to remember user
        login_user(user, remember=remember)
        #session['name'] = current_user.name
        return redirect(url_for('auth.profile'))
        #return redirect(url_for('/profile',username=current_user.name))

    # if the user doesn't exist or password is wrong, reload the page
    flash('Please check your login details and try again.','is-danger')
    return redirect(url_for('auth.login')) 
 
# ================   
@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    #=====
    # 1- get the form data.
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # 2- verify if this user already exist
    user = User.query.filter_by(email=email).first() 
    if user: 
        # if a user is found, redirect back to signup page to try again
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # 3- create a new user with the form data.
    # note : password is hashed inside User class method
    new_user = User(email=email, name=name, 
        password=password) 

    # 4- add the new user to the database
    db.session.add(new_user)
    db.session.commit()
    
    #=====
    flash('New user signed up ! Now, log in please.','is-success')
    return redirect(url_for('auth.login'))

# ================ 
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.index'))

# ================ 
@auth.route('/profile')
@login_required
def profile():
    # get personnal dashboard lists from SQLtable UserDashboard
    dashlist = find_dashboardlist(current_user)

    return render_template('profile.html',
        name=current_user.name, dashlist=dashlist)