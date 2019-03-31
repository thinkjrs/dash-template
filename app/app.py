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

external_stylesheets = None
external_scripts = None
nav = '''
<nav class="navbar navbar-expand navbar-light"> 
    <div class="container-fluid", id="navbar-button-container">

        <button type="button" id="sidebarCollapse" class="btn ">
            <i class="fas fa-align-left"></i>
        </button>
        <form class="form-inline my-2">
            <input id="navbar-search" class="form-control mr-sm-2" type="search" placeholder="Type an artist" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
        </form>
        <button type="button" id="userButton-navbar" class="btn btn-light">
            <i class="fas fa-user"></i>
        </button>
    </div>
</nav>'''
app = MFDash(__name__,
                external_stylesheets = external_stylesheets,
                external_scripts = external_scripts,)

app.layout = html.Div(id='dash-container-fluid', children=[
    html.Nav(className='navbar sticky-top navbar-expand navbar-light bg-light',
        children=[
            html.Div(className='col-xs-1 mr-auto',
                children=[
                    html.Button(type='button', id='sidebarCollapse',
                        className='btn', children=[
                            html.I(className='fas fa-align-left'),
                        ],
                    ),
                ],
            ),
            html.Div(className='col-xs-9',
                children=[
                    html.Div(className='row no-gutters align-items-center', 
                        children=[
                            html.Div(className='col-xs-10', 
                                children=dcc.Input(id='navbar-search',
                                    placeholder='Artist search',
                                    type='search',
                                    value='',
                                    className='form-control',
                                ),
                            ),
                            html.Div(className='col-xs-2',
                                children=html.Button(
                                    className='btn',
                                    type='submit', 
                                    id="navbar-search-button",
                                    children=html.I(className='fas fa-search'),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(className='col-xs-1 ml-auto',
                children=[
                    html.Button(className='button',
                        type='button', 
                        id='userButton-navbar',
                        children=html.I(className="fas fa-user"),
                    ),
                ],
            ),
        ],
    ),
    html.Div(className='row no-gutters',
        children=[
            html.H2(className='col-xs text-center', id='search-submit', ),
        ],
    ),
],)
@app.callback(
    Output('search-submit', 'children'),
    [Input('navbar-search-button', 'n_clicks')],
    state=[State('navbar-search', 'value')]
)
def compute(n_clicks, query):
    if n_clicks is None:
        pass
    return f"{query}"



if __name__ == '__main__':
    app.run_server(debug=True)
