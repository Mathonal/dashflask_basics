import dash
from dash.dependencies import Input, State, Output
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px

import pandas as pd
from flask_login import current_user,login_required

import hashlib

def getHashDashURL(s, char_length=32):
    """
        Geneate hexadecimal string with given length from a string
        >>> short_str("hello world", 8)
        '309ecc48'
    """
    if char_length > 128:
        raise ValueError("char_length {} exceeds 128".format(char_length))
    hash_object = hashlib.sha512(s.encode())
    hash_hex = hash_object.hexdigest()

    return hash_hex[0:char_length]


# DOES NOT WORK AS DASHBOARDS ARE LOADED WHEN RUNNING SERVER
# USER NOT CONNECTED AT LAUNCH so it loads the generic layout
# @login_required
# def choosinglayout_auth(app):
#     print('currentuser :'+str(current_user))
#     if current_user and current_user.is_authenticated:
#         #PERSONNAL LAYOUT
#         df = pd.DataFrame({
#             "CDs": ["Rap", "R&B", "Rap", "R&B" ],
#             "Amount": [41, 15, 24, 2],
#             "City": ["SF", "SF","Montreal", "Montreal"]
#         })

#         fig = px.bar(df, x="CDs", y="Amount", color="City", barmode="group")

#         # Create Dash Layout
#         app.layout = html.Div(children=[
#         html.H1(children='PERSONALISED DASHBOARD 1'),

#         html.Div(children='''
#             Dash: A web application framework for Python.
#         '''),

#         dcc.Graph(
#             id='example-graph',
#             figure=fig
#         )
#         ])

#     else : #GENERIC LAYOUT
#         # Load DataFrame
#         # assume you have a "long-form" data frame
#         # see https://plotly.com/python/px-arguments/ for more options
#         df = pd.DataFrame({
#             "CDs": ["Rap", "R&B", "Rap", "R&B", "Rap", "R&B" ],
#             "Amount": [4, 1, 2, 2, 4, 5],
#             "City": ["SF", "SF", "Seatle", "Seatle", "Montreal", "Montreal"]
#         })

#         fig = px.bar(df, x="CDs", y="Amount", color="City", barmode="group")

#         # Create Dash Layout
#         app.layout = html.Div(children=[
#         html.H1(children='GENERAL DASHBOARD 1'),

#         html.Div(children='''
#             Dash: A web application framework for Python.
#         '''),

#         dcc.Graph(
#             id='example-graph',
#             figure=fig
#         )
#         ])    