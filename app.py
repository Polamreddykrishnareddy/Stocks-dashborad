# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import ibm
import dash_bootstrap_components as dbc

app = Dash(__name__)

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active=True, href="#")),
        dbc.DropdownMenu(
            [dbc.DropdownMenuItem("IBM"), 
            dbc.DropdownMenuItem("GOOGLE")],
            label="Stocks",
            nav=True,
        ),
    ]
)
ibm_open = ibm.open_stocks_of_ibm()
fig = px.bar(ibm_open)
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
