import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def f_header(app):
    header = [
        html.Div(children=[
            html.Img(src=app.get_asset_url("plane.png"), 
            id = "plotly-image",
            style = {
                "height" : "60px",
                "width" : "auto",
                "margin-bottom" : "25px",
                'align-items' : 'center',
                'margin-left': 'auto',
                'margin-right': 'auto'
            })
        ]),

        html.Div(children=[
            html.H2("Plane Dashboard", 
            style = {
                'margin-bottom' : '0px', 
                'align-items' : 'center',
                'margin-left': 'auto',
                'margin-right': 'auto',
                'textAlign' : 'center'
            }),
            html.H5("Created by Dashboard", 
            style = {
                'margin-bottom' : '0px',
                'align-items' : 'center',
                'margin-left': 'auto',
                'margin-right': 'auto',
                'textAlign' : 'center'
            }),
        ])
    ]

    return header