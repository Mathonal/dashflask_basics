import dash
from dash.dependencies import Input, State, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

import pandas as pd

#from ..utils_dashboard import choosinglayout_auth

url_base = '/dash/app1/'

def dashlayout(app):
    # Load DataFrame
    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "CDs": ["Rap", "R&B", "Rap", "R&B", "Rap", "R&B" ],
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "Seatle", "Seatle", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="CDs", y="Amount", color="City", barmode="group")

    # Create Dash Layout
    app.layout = html.Div(children=[
    html.H1(children='GENERAL DASHBOARD 1'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ])    

def Add_Dash(server):
    app = dash.Dash(
        server=server,
        #routes_pathname_prefix='/mydash&user=testname/',
        #requests_pathname_prefix='/mydash&user=testname/',
        url_base_pathname=url_base,
        external_stylesheets=[
            'https://codepen.io/chriddyp/pen/bWLwgP.css',
            '/static/dist/css/styles.css'
        ]
    )
    dashlayout(app)
    #choosinglayout_auth(app)

    return app.server

    # CALLBACKS

    # Update the index
    @app.callback(dash.dependencies.Output('page-content', 'children'),
                  [dash.dependencies.Input('url', 'pathname')])
    def display_page(pathname):
        if pathname == '/page-1':
            return page_1_layout
        elif pathname == '/page-2':
            return page_2_layout
        else:
            return index_page
        # You could also return a 404 "URL not found" page here