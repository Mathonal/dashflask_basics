## goal
Aims is to have a Demonstrator Flask app that integrate several dashboards
and handle users/authentification to have "private dashboard"

## architecture
- run flask app in wsgi

in dashflask_app : 
* __init__ :
    * flask core app with authentification (login manager) and userDataBase in
    * in app_context dashboards import

* in baseauth folder :
    * authroutes : blueprint/routes for core pages : index, home, login, signup
    * models : user database manipulations
    * utils_db : specific request functions on database

and statics/templates folders

* in dash folder :
    * dashroutes : blueprint/routes for dashboards
    utils_dashboard : common utilities calles from all dashboards

    * genericDash folder : presentation dashboards that do not require specific user logged in (open url)

    * private dashboard folder : dashboards that requires specific users logged in to be consulted. (loginuser required and dashurl is encrypted at launch from ids in dashboard and user DB)

## things to consider / improve :
* duplicate between private dash ID and UserDashboard database (will be a source of error and not found URL down the line)
* still a security problem : another registered user who would have the exact encrypted url of another user dashboard could consult it ...
* UserDashboard should use User e-mail as it is the KEY in User DB
* any UserDashboard PRODUCTION database should be create and populate before app launch

* configuration file and variable are not correctly set up for cloudapp (this is a demo)

## Credits for tutorials/infos on this subject
dash and flask embedded
https://hackersandslackers.com/plotly-dash-with-flask/

https://community.plotly.com/t/flask-multiple-dash-apps-html-templates-together/14858

https://github.com/jimmybow/Flask_template_auth_with_Dash

https://github.com/plotly/dash/issues/221

https://stackoverflow.com/questions/59627976/integrating-dash-apps-into-flask-minimal-example

https://community.plotly.com/t/how-protect-dash-routes-with-login-after-dash-1-0-release/25114

https://community.plotly.com/t/forcing-dash-app-to-be-called-through-flask-route/25833

https://stackoverflow.com/questions/58379772/passing-current-user-from-flask-login-to-plotly-dash-app

https://community.plotly.com/t/get-username-for-authenticated-user-with-dash-basic-auth/6450/5

flask factory
https://hackersandslackers.com/flask-application-factory/

flash authent
https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login-fr

CSS html framework
https://bulma.io/
https://bulma.io/documentation/