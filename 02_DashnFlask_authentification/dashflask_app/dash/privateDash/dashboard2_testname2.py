#DASH DEPENDENCIES
import dash
from dash.dependencies import Input, State, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

#OTHER
from flask_login import login_required
from ..utils_dashboard import getHashDashURL

#IDENTIFIERS
dashid = ['testname2','dashtest2']

#DASHBOARD CONTENT
def dashlayout(app):
    """PERSONALIZED LAYOUT DEFINITION """
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [2, 2, 2, 3, 3, 3],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


    # Create Dash Layout
    app.layout = html.Div(children=[
    html.H1(children='GENERAL DASHBOARD testname2'),

    html.Div(children='''
        Dashboard with personnal business data
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ])


#========================================================================
# DASHBOARD INIT
# Function to protect dashboard view from unauthenticated users
# with direct URL
def protect_views(app):
    for view_func in app.server.view_functions:
        if view_func.startswith(app.config["url_base_pathname"]):
            app.server.view_functions[view_func] = login_required(app.server.view_functions[view_func])
    return app

def Add_Dash(server):
    """
        initialize dashboard app from global flaskappserver
        function called at global init
    """
    # GENERATE SPECIFIC URL
    urlbase = '/privatedash/'+getHashDashURL(dashid[0]+dashid[1])+'/'

    #CREATE APP
    app = dash.Dash(
        server=server,
        url_base_pathname=urlbase,
        external_stylesheets=[
            'https://codepen.io/chriddyp/pen/bWLwgP.css',
            '/static/dist/css/styles.css'
        ]
    )
    dashlayout(app)

    app = protect_views(app)
    return app