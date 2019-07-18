import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

tab_2_layout = html.Div([
            html.Div([
                html.Div([
                    html.H6('Medical Specialty'),
                    dcc.Graph(
                        id='med-graph-1',
                        figure={
                            'data': [

                            ],
                            'layout': {
                                'title': 'Graph-1'
                            }
                        }
                    )
                ], className="six columns"),

                html.Div([
                    html.H6('Readmission'),
                    dcc.Graph(
                        id='med-graph-2',
                        figure={
                            'data': [

                            ],
                            'layout': {
                                'title': 'Graph-2'
                            }
                        }
                    )
                ], className="six columns"),

            ], className="row", style={"margin": "1% 3%"})
    ])


