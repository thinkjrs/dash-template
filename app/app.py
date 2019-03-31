"""
app.py

Main Dash/Flask application code.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from static.index import MFDash

external_stylesheets = None
external_scripts = None
nav = '''
<nav class="navbar navbar-expand-lg navbar-light"> 
    <div class="container-fluid", id="navbar-button-container">

        <button type="button" id="sidebarCollapse" class="btn ">
            <i class="fas fa-align-left"></i>
        </button>
        <form class="form-inline my-2 my-lg-0">
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
def navbar():
    return html.Nav(className='navbar navbar-expand-lg navbar-light bg-dark',
            children=[
                html.Div(id='navbar-button-container', 
                    className='container-fluid',
                    children=[
                        html.Button(type='button', id='sidebarCollapse',
                            className='btn', children=[
                                html.I(className='fas fa-align-left'),
                            ],
                        ),
                    ],
                ),
            ],
    )
app.layout = html.Div(children=[
    navbar(),
#    dcc.Graph(id='test-graph',
#              figure = {
#                  'data': [
#                      {
#                          'y': [1.4, 1.3, 1.45, 1.6],
#                          'x': [0, 1, 2, 3],
#                          'type': 'scatter',
#                          'name': 'Test Line Graph',
#                      },
#                  ],
#                  'layout': {
#                       'title': 'Test Line Graph Visualization',
#                  },
#              },
#    ),
])

if __name__ == '__main__':
    app.run_server(debug=True)
