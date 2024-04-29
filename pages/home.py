import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H2('TIPO DE ESTUDIO DE SUELO SEGUN SU CATEGORIA', style={'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Label('La clasificación de las unidades de construcción por categorías es esencial para determinar aspectos del diseño y la seguridad de una edificación. Estas categorías, que abarcan desde Baja hasta Especial, se definen según el número total de niveles y las cargas máximas de servicio que la estructura debe soportar.'),
            html.Br(),
            html.Br(),
            html.Label('Para calcular correctamente estas variables, se considera la combinación de carga muerta más carga viva debida al uso y ocupación de la edificación. Además, se incluyen todos los pisos del proyecto, desde sótanos hasta terrazas y pisos técnicos, para definir el número de niveles'),
            html.Br(),
            html.Br(),
            html.Label('La cantidad y profundidad de los sondeos geotécnicos varían según la categoría de construcción. En proyectos de baja categoría, son esenciales para evaluar la estabilidad del suelo y la cimentación. En categorías medias, adquieren mayor relevancia para detectar posibles problemas geotécnicos. Para proyectos de alta categoría, como rascacielos, son imprescindibles para comprender la complejidad del subsuelo y garantizar una cimentación segura y duradera. En proyectos de categoría especial, como estructuras críticas o de gran envergadura, los sondeos alcanzan un nivel máximo de importancia, ya que su precisión puede ser determinante para la seguridad y estabilidad de la construcción.')
        ], style={'flex': '1'}),  # El texto se expandirá para ocupar el espacio restante
        html.Div([
            html.Img(src='https://www.geotechnicsingenieria.com.co/wp-content/uploads/2017/07/ASESORIA-ESPECIALIZADA-EN-GEOTECNIA-1-1080x675.jpg', style={'width': '100%', 'height': 'auto'})
        ], style={'flex': '1', 'margin-left': '20px'})  # La imagen ocupará el 100% del espacio disponible y habrá un margen a la izquierda
    ], style={'display': 'flex', 'align-items': 'center'})
])

