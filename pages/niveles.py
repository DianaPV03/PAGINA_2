import dash
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__,
                   name="NIVELES DE CONSTRUCCIÓN")

layout = html.Div([
        html.H1("NIVELES DE CONSTRUCCIÓN"),
        html.Div([
            html.Label('Selecione un rango de nivel de construccion', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Hasta 3 niveles', 'value': '3'},
                    {'label': 'Entre 4 y 10 nivles', 'value': '4-10'},
                    {'label': 'Entre 11 y 20 niveles', 'value': '11-20'},
                    {'label': 'Mayor a 20 niveles', 'value': '21'}
                ],
                value='Elige el nivel',
                style={'width': '300px'}
            )
        ], style={'display': 'inline-flex', 'margin-bottom': '30px'})
    ])

