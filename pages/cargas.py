import dash
import pandas as pd
import os
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__, name="CARGAS MAXIMAS")

# Cargar los datos al iniciar la aplicación
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, 'SUELOS.csv')
data = pd.read_csv(file_path).to_dict('records')

layout = html.Div([
    html.H2("CARGAS MÁXIMAS"),
    html.Label('Las cargas máximas de servicio son cruciales para garantizar la seguridad y estabilidad de una estructura según la NSR-10.'),
    html.Br(),
    html.Br(),
    html.Div([
        html.Label('Seleccione un rango de carga máxima', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Menores de 800 kN', 'value': '800'},
                {'label': 'Entre 801 y 4000 kN', 'value': '801-4000'},
                {'label': 'Entre 4001 y 8000 kN', 'value': '4001-8000'},
                {'label': 'Mayores de 8000 kN', 'value': '8001'}
            ],
            value='Elige la carga',
            style={'width': '300px'}
        )
    ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),
    html.Button('Consultar', id='mi-boton', n_clicks=0),
    html.Div(id='mi-output'),

    html.P("Un aspecto importante según la NSR-10 para determinar las cargas máximas de servicio en una estructura es considerar adecuadamente las condiciones climáticas y ambientales locales. Esto incluye evaluar la posible acción de vientos, sismos, y otras cargas externas que puedan afectar la estabilidad y seguridad de la edificación a lo largo de su vida útil. Además, es crucial tener en cuenta el uso previsto de la estructura y las cargas móviles o dinámicas que pueda experimentar durante su operación normal, como la carga de personas, muebles, equipos, entre otros."),

    html.P("NSR-10", style={'color': '#003BFF'}),
    html.A("Click aqui para leer la norma", href="https://www.scg.org.co/Titulo-H-NSR-10-Decreto%20Final-2010-01-14.pdf", target="_blank")
], style={'backgroundColor': '#C6C4C9'})  # Fondo azul claro


@callback(
    Output('mi-output', 'children'),
    [Input('dropdown', 'value'),
     Input('mi-boton', 'n_clicks')]
)

def update_output(dropdown, n_clicks):
    if n_clicks is not None and n_clicks > 0:
        if dropdown == '800':
            if data:
                return validar_salida(data[0])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '801-4000':
            if data:
                return validar_salida(data[1])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '4001-8000':
            if data:
                return validar_salida(data[2])
               
            else:
                return "No se encontraron datos."
        elif dropdown == '8001':
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
        
def consultar_bd(file_path, sheet_name):
    df = pd.read_csv(file_path)
    return df.to_dict('records')


