import dash
from dash.dependencies import Input, Output
import dash_table
import dash_html_components as html
import pandas as pd

import dash_core_components as dcc
import plotly.express as px

urlbase = '/dashapp/' #same url as in html template

def init_dashboard(server):
    """Create a Plotly Dash dashboard."""

    # routes_pathname_prefix in dash_app object
    # dont need to create a route for Dash in main __init__
    app = dash.Dash(
        server=server,
        routes_pathname_prefix=urlbase,
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
        "Amount": [4, 1, 2, 2, 4, 5],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
    })

    # Dash figure
    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    # Create Dash Layout
    app.layout = html.Div(children=[
    html.H1(children='Hello Dash test'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
    ])

    #========
    return app.server

    # callback part, for actualisation, link inside dashboard, etc
    def init_callbacks(dash_app):
        @app.callback(
        # Callback input/output
        # ...
        )
        def update_graph(rows):
            # Callback logic
            pass