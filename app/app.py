"""
app.py

Main Dash/Flask application code.
"""

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
#app.config['suppress_callback_exceptions']=True
def navbar_layout():
    return html.Nav(className='navbar navbar-expand navbar-light bg-dark',
            children=[
                html.Div(id='navbar-button-container', 
                    className='container-fluid',
                    children=[
                        html.Button(type='button', id='sidebarCollapse',
                            className='btn', children=[
                                html.I(className='fas fa-align-left'),
                            ],
                        ),
                        html.Form(className='form-inline my-2', 
                            children=[
                                dcc.Input(id='navbar-search',
                                    placeholder='Artist search',
                                    type='text',
                                    value='',
                                ),
                            ],
                        ),
                    ],
                ),
            ],
    )
app.layout = html.Div(id='dash-hell', children=[
    html.Nav(className='navbar navbar-expand navbar-light bg-light',
            children=[
                html.Div(id='navbar-button-container', 
                    className='container-fluid',
                    children=[
                        html.Button(type='button', id='sidebarCollapse',
                            className='btn', children=[
                                html.I(className='fas fa-align-left'),
                            ],
                        ),
                        html.Form(className='form-inline my-2', 
                            children=[
                                dcc.Input(id='navbar-search',
                                    placeholder='Artist search',
                                    type='text',
                                    value=None,
                                ),
                                html.Button('Submit', id='button-search'),
                            ],
                        ),
                    ],
                ),
            ],
    ),
    html.P(id='search-submit'),
    dcc.Graph(id='test-graph',
              figure = {
                  'data': [
                      {
                          'y': [1.4, 1.3, 1.45, 1.6],
                          'x': [0, 1, 2, 3],
                          'type': 'scatter',
                          'name': 'Test Line Graph',
                      },
                  ],
                  'layout': {
                       'title': 'Test Line Graph Visualization',
                  },
              },
    ),
])
@app.callback(
    Output('search-submit', 'children'),
    [
        Input('button-search', 'n_clicks'),
        #Input('navbar-search', 'n_blur'),
    ],
    [
        State('navbar-search', 'value'),
    ]
)
def update_search_output(nsub, nblur, val):
    if val is not None and nsub:
        return f"You searched for {val}"


if __name__ == '__main__':
    app.run_server(debug=True)
