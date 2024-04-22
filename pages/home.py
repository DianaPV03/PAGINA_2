import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Pagina de inicio'),
    html.Div([
        html.Div([
            html.Label('La clasificación de las unidades de construcción por categorías es esencial para determinar aspectos del diseño y la seguridad de una edificación. Estas categorías, que abarcan desde Baja hasta Especial, se definen según el número total de niveles y las cargas máximas de servicio que la estructura debe soportar.'),
            html.Br(),
            html.Label('Para calcular correctamente estas variables, se considera la combinación de carga muerta más carga viva debida al uso y ocupación de la edificación. Además, se incluyen todos los pisos del proyecto, desde sótanos hasta terrazas y pisos técnicos, para definir el número de niveles'),
            html.Br(),
            html.Label('Por favor indique el número de pisos de una construcción, para determinar el nivel de categoría correspondiente y la cantidad de sondeos necesarios para realizar una evaluación precisa de la estructura.')
        ], style={'flex': '1'}),  # El texto se expandirá para ocupar el espacio restante
        html.Div([
            html.Img(src='https://www.geotechnicsingenieria.com.co/wp-content/uploads/2017/07/ASESORIA-ESPECIALIZADA-EN-GEOTECNIA-1-1080x675.jpg', style={'width': '100%', 'height': 'auto'})
        ], style={'flex': '1', 'margin-left': '20px'})  # La imagen ocupará el 100% del espacio disponible y habrá un margen a la izquierda
    ], style={'display': 'flex', 'align-items': 'center'})
])

