import dash
import os
import pandas as pd
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__,
                name="NIVELES DE CONSTRUCCIÓN")

# Cargar los datos al iniciar la aplicación
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'SUELOS.csv')
data = pd.read_csv(file_path).to_dict('records')

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
        ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),
        html.Button('Consultar', id='mi-boton', n_clicks=0),
        html.Div(id='mi-output-niveles')   
    ])


@callback(
    Output('mi-output-niveles', 'children'),
    [Input('dropdown', 'value'),
     Input('mi-boton', 'n_clicks')]
)

def update_output(dropdown, n_clicks):
    if n_clicks is not None and n_clicks > 0:
        if dropdown == '3':
            if data:
                return validar_salida(data[0])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '4-10':
            if data:
                return validar_salida(data[1])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '11-20':
            if data:
                return validar_salida(data[2])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '21':
            if data:
                return validar_salida(data[3])
               
            else:
                return "No se encontraron datos."


def validar_salida(tipo):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in tipo.keys()])
        ),
        html.Tbody([
            html.Tr([
                html.Td(tipo[col]) for col in tipo.keys()
            ])
        ])
    ])


