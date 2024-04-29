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

layout = html.Div(style={'backgroundColor': '#C6C4C9'}, children=[
    html.H2("NIVELES DE CONSTRUCCIÓN", style={'text-align': 'center'}),
    html.Label('Conocer los niveles de construcción es esencial para realizar un estudio de suelos efectivo. Esta información permite planificar adecuadamente la profundidad de las excavaciones, identificar los estratos geológicos presentes y diseñar cimentaciones apropiadas.'),
    html.Br(),
    html.Br(),
    html.Img(src='https://www.researchgate.net/profile/Alvaro-Toledo-Lopez-2/publication/322446619/figure/fig1/AS:582051855376384@1515783384288/Figura-3-Edificio-12-pisos-Figura-4-Edificio-18-pisos-Figura-5-Edificio-24-pisos-En-la.png', style={'width': '200px', 'height': '200px'}),
    html.Br(),
    html.Br(),
    html.Div([
        html.Label('Seleccione un rango de nivel de construcción', style={'margin-right': '10px'}),
        dcc.Dropdown(
            id='dropdown',
            options=[
                {'label': 'Hasta 3 niveles', 'value': '3'},
                {'label': 'Entre 4 y 10 niveles', 'value': '4-10'},
                {'label': 'Entre 11 y 20 niveles', 'value': '11-20'},
                {'label': 'Mayor a 20 niveles', 'value': '21'}
            ],
            value='Elige el nivel',
            style={'width': '300px'}
        )
    ], style={'display': 'inline-flex', 'margin-bottom': '30px'}),
    html.Button('Consultar', id='mi-boton', n_clicks=0, style={'border-radius': '60%'}),
    html.Div(id='mi-output-niveles'),
    
    # Párrafo adicional al final de la página
    html.P("Los sondeos con recuperación de muestras deben constituir como mínimo el 50% de los sondeos practicados en el estudio definitivo"),
    html.P("En los sondeos con muestreo se deben tomar muestras cada metro en los primeros 5 m de profundidad y a partir de esta profundidad, en cada cambio de material o cada 1.5 m de longitud del sondeo."),
    html.P("Al menos el 50% de los sondeos deben quedar ubicados dentro de la proyección sobre el terreno de las construcciones. "),
    html.P("Los sondeos practicados dentro del desarrollo del Estudio Preliminar pueden incluirse como parte del estudio definitivo - de acuerdo con esta normativa - siempre y cuando hayan sido ejecutados con la misma calidad y siguiendo las especificaciones dadas en el presente título del Reglamento."),
    html.P("El número de sondeos finalmente ejecutados para cada proyecto, debe cubrir completamente el área que ocuparán la unidad o unidades de construcción contempladas en cada caso, así como las áreas que no quedando ocupadas directamente por las estructuras o edificaciones, serán afectadas por taludes de cortes u otros tipos de intervención que deban ser considerados para evaluar el comportamiento geotécnico de la estructura y su entorno. "),
    html.P("En registros de perforaciones en ríos o en el mar, es necesario tener en cuenta el efecto de las mareas y los cambios de niveles de las aguas, por lo que se debe reportar la el levación (y no la profundidad solamente) del estrato, debidamente referenciada a un datum preestablecido."),

 
    html.P("NSR-10", style={'color': '#003BFF'}),
    html.A("Click aqui para leer la norma", href="https://www.scg.org.co/Titulo-H-NSR-10-Decreto%20Final-2010-01-14.pdf", target="_blank")
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


