import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

app.layout = html.Div([
    html.H1("ESTUDIOS GEOTECNICOS", style={'text-align': 'center'}),
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