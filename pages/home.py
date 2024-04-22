import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Pagina de inicio'),
    html.Label('La clasificación de las unidades de construcción por categorías es esencial para determinar aspectos del diseño y la seguridad de una edificación. Estas categorías, que abarcan desde Baja hasta Especial, se definen según el número total de niveles y las cargas máximas de servicio que la estructura debe soportar.'),
    html.Br(),
    html.Label('Para calcular correctamente estas variables, se considera la combinación de carga muerta más carga viva debida al uso y ocupación de la edificación. Además, se incluyen todos los pisos del proyecto, desde sótanos hasta terrazas y pisos técnicos, para definir el número de niveles'),
    html.Br(),
    html.Label('Por favor indique el número de pisos de una construcción, para determinar el nivel de categoría correspondiente y la cantidad de sondeos necesarios para realizar una evaluación precisa de la estructura.')
])