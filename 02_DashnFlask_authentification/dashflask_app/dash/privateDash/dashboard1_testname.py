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
dashid = ['testname','dashtest1']

#DASH CONTENT
def dashlayout(app):
    """PERSONALIZED LAYOUT DEFINITION """
    df = pd.DataFrame({
        "CDs": ["Rap", "R&B", "Rap", "R&B" ],
        "Amount": [41, 15, 24, 2],
        "City": ["SF", "SF","Montreal", "Montreal"]
    })

    fig = px.bar(df, x="CDs", y="Amount", color="City", barmode="group")

    # Create Dash Layout
    app.layout = html.Div(children=[
    html.H1(children='PERSONALISED DASHBOARD testname'),

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
    #for view_func in app.view_functions:
        if view_func.startswith(app.config["url_base_pathname"]):
            #print(app.server.view_functions[view_func])
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
        #routes_pathname_prefix='/mydash&user=testname/',
        #requests_pathname_prefix='/mydash&user=testname/',
        #url_base_pathname=url_base,
        url_base_pathname=urlbase,
        external_stylesheets=[
            'https://codepen.io/chriddyp/pen/bWLwgP.css',
            '/static/dist/css/styles.css'
        ]
    )
    #auth = dash_auth.BasicAuth(
    #    app,
    #   VALID_USERNAME_PASSWORD_PAIRS)

    dashlayout(app)

    app = protect_views(app)
    return app.server

    # CALLBACKS
    # Update the index


    # Update the index
    # @app1.callback(
    #     Output('Div', 'children'),
    #     [Input('div3', 'children')])
    # def update_intervalCurrentTime(children):
    #     return session.get('username', None)

    # @app.callback(dash.dependencies.Output('page-content', 'children'),
    #               [dash.dependencies.Input('url', 'pathname')])
    # def display_page(pathname):
    #     if pathname == '/page-1':
    #         return page_1_layout
    #     elif pathname == '/page-2':
    #         return page_2_layout
    #     else:
    #         return index_page
        # You could also return a 404 "URL not found" page here


