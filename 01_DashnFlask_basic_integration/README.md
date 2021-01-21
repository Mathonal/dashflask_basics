## goal
Aim is to have a flask app that integrates Dash apps

(long term goal is to be able to integrate several dashboard 
in one flask app with access and authentifications)

This is the most basic setup possible :
- app is run in WSGI
- flask is run in __init__, dashboard is imported in app_context
- dashboard is encapsulated in init_dashboard function
(can compare difference with "stand alone" dashapp in dashboard folder)

## Credits for tutorials on this subject
dash and flask embedded : https://hackersandslackers.com/plotly-dash-with-flask/
flask factory : https://hackersandslackers.com/flask-application-factory/