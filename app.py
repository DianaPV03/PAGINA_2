import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

# Diseño de la página
app.layout = html.Div(style={'background-color': '#C6C4C9'}, children=[
    html.H1("ESTUDIOS GEOTÉCNICOS", style={'text-align': 'center', 'color': '#000000', 'margin-bottom': '30px'}),
    html.Div([
        html.Div(
            html.Button(dcc.Link(f"{page['name']}", href=page["relative_path"])),
            style={'margin-right': '10px'}
        ) for page in dash.page_registry.values()
    ],
        style={'display': 'flex'}),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)
    