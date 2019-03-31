"""
app.py

Main Dash/Flask application code.
"""
import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from static.index import MFDash
from component import mf_navbar

external_stylesheets = None
external_scripts = None

app = MFDash(
    __name__,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
)

app.layout = html.Div(
    id="dash-container-fluid",
    children=[
        mf_navbar(),
        html.Div(
            className="row no-gutters",
            children=[
                html.H2(className="col-xs text-center", id="search-submit")
            ],
        ),
    ],
)


@app.callback(
    Output("search-submit", "children"),
    [Input("navbar-search-button", "n_clicks")],
    state=[State("navbar-search", "value")],
)
def compute(n_clicks, query):
    if n_clicks is None:
        pass
    return f"{query}"


if __name__ == "__main__":
    app.run_server(debug=True)
