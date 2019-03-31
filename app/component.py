import dash_html_components as html
import dash_core_components as dcc

def mf_navbar():
    """
    Return the navigation bar layout for the musicfox.io application.
    """
    return html.Nav(
        className="navbar sticky-top navbar-expand navbar-light bg-light",
        children=[
            html.Div(
                className="col-xs-1 mr-auto",
                children=[
                    html.Button(
                        type="button",
                        id="sidebarCollapse",
                        className="btn",
                        children=[html.I(className="fas fa-align-left")],
                    )
                ],
            ),
            html.Div(
                className="col-xs-9",
                children=[
                    html.Div(
                        className="row no-gutters align-items-center",
                        children=[
                            html.Div(
                                className="col-xs-10",
                                children=dcc.Input(
                                    id="navbar-search",
                                    placeholder="Artist search",
                                    type="search",
                                    value="",
                                    className="form-control",
                                ),
                            ),
                            html.Div(
                                className="col-xs-2",
                                children=html.Button(
                                    className="btn",
                                    type="submit",
                                    id="navbar-search-button",
                                    children=html.I(className="fas fa-search"),
                                ),
                            ),
                        ],
                    )
                ],
            ),
            html.Div(
                className="col-xs-1 ml-auto",
                children=[
                    html.Button(
                        className="btn",
                        type="button",
                        id="userButton-navbar",
                        children=html.I(className="fas fa-user"),
                    )
                ],
            ),
        ],
    )
