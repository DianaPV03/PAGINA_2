import dash
import xlwings as xw
import os
from dash import html, dcc, callback, Input, Output, State

dash.register_page(__name__,
                   name="CARGAS MAXIMAS")

layout = html.Div([
        html.H1("CARGAS MAXIMAS"),
        html.Div([
            html.Label('Selecione un rango de carga maxima', style={'margin-right': '10px'}),
            dcc.Dropdown(
                id='dropdown',
                options=[
                    {'label': 'Menores de 800 kN', 'value': '800'},
                    {'label': 'Entre 801 y 4000 kN', 'value': '801-4000'},
                    {'label': 'Entre 4001 y 8000 kN', 'value': '4001-8000'},
                    {'label': 'Mayores de 8000kN', 'value': '8001'}
                ],
                value='Elige la carga',
                style={'width': '300px'}
            )
        ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),
        html.Button('Consultar', id='mi-boton', n_clicks=0),
        html.Div(id='mi-output')       
    ])

@callback(
    Output('mi-output', 'children'),
    [Input('dropdown', 'value'),
     Input('mi-boton', 'n_clicks')]
)

def update_output(dropdown, n_clicks):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if n_clicks is not None and n_clicks > 0:
        if dropdown == '800':
            file_path = os.path.join(current_dir, 'SUELOS.xlsx')
            return consultar_bd(file_path, 'C.BAJA')

def consultar_bd(file_path, page):
    ws = xw.Book(file_path).sheets[page]
    v1 = ws.range("A1:A2").value
    return f'You selected: {v1}'