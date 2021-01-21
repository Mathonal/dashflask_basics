import dash
from dash.dependencies import Input, State, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

import pandas as pd

url_base = '/dash/app2/'

def Add_Dash(server):
    app = dash.Dash(
        server=server,
        url_base_pathname=url_base,
        external_stylesheets=[
            'https://codepen.io/chriddyp/pen/bWLwgP.css',
            '/static/dist/css/styles.css'
        ]
    )
    # Load DataFrame
    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame({
        "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
        "Amount": [20, 10, 16, 30, 25, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


    # Create Dash Layout
    app.layout = html.Div(children=[
    html.H1(children='GENERAL DASHBOARD 2'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ])
    return app.server