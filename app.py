import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

# Diseño de la página
app.layout = html.Div(style={'background-color': '#C6C4C9'}, children=[
    html.H1("ESTUDIOS GEOTÉCNICOS", style={'text-align': 'center', 'color': '#1A5276', 'margin-bottom': '30px'}),
    html.Div([
        html.Div(
            html.Button(dcc.Link(f"{page['name']}", href=page["relative_path"]), style={'text-align': 'center', 'margin-bottom': '30px'} ),
            style={'margin-right': '20px', 'text-align': 'center'}
        ) for page in dash.page_registry.values()
    ],
        style={'display': 'flex'}),
    dash.page_container,

    html.Footer(
        html.P("© 2024 Todos los derechos reservados", style={'text-align': 'center', 'color': '#1A5276', 'margin-top': '30px'})
    )
])

if __name__ == '__main__':
    app.run(debug=True)
    