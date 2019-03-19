"""
app.py

Main Dash/Flask application code.
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from static.index import index_string

external_stylesheets = None
external_scripts = None

app = dash.Dash(__name__,
                external_stylesheets = external_stylesheets,
                external_scripts = external_scripts,)

app.index_string = index_string

app.layout = html.Div(children=[
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

if __name__ == '__main__':
    app.run_server(debug=True)
