import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
from assets import patient_demographics, patient_med_readmit

import pandas as pd
import plotly.figure_factory as ff
import numpy as np

import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

colors = {"background": "#F3F6FA", "background_div": "white", 'text': '#009999'}

app.config['suppress_callback_exceptions']= True


app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('Patient Re-admissions Dashboard', style={
            'textAlign': 'center',
            'color': colors['text']
        }),


    dcc.Tabs(id="tabs", className="row", style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='dem_tab', children=[
        dcc.Tab(label='Demographics', value='dem_tab'),
        dcc.Tab(label='Medical Speciality And Re-Admission', value='med_tab')
        # dcc.Tab(label='Re-admissions', value='readmit_tab')
    ]),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'dem_tab':
        return patient_demographics.tab_1_layout
    elif tab == 'med_tab':
        return patient_med_readmit.tab_2_layout

if __name__ == '__main__':
    app.run_server(debug=True)