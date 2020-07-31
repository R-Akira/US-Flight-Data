import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


# import pages
from pages.header import f_header
from pages.content_1 import content1
from pages.content_2 import content2
from pages.about_us import aboutus

# Initiating Dash
app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"},
    ],external_stylesheets=[dbc.themes.BOOTSTRAP]
)
server = app.server

# Layouts


tabs_styles = {
    'height': '40px',
    'width' : '50%',
    'justify-content': 'space-between',
    'align-items' : 'center',
    'margin-left': 'auto',
    'margin-right': 'auto'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'font-family':'Candara',
    'justify-content': 'center',
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
    'font-family':'Candara',
    'align-items' : 'center',
    'justify-content': 'center',
}

app.layout = html.Div([
    html.Div(
        f_header(app),
        id = "header",
        className="row flex-display",
        style = {"margin-bottom": "25px", 'margin-left': 'auto', 'margin-right': 'auto'},
    ),
    dcc.Tabs([
        dcc.Tab(label="Overview", children = content1(app),style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="Analysis", children = content2(app),style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label="About Us", children = aboutus(app),style=tab_style, selected_style=tab_selected_style),
    ], 
    className="row flex-display",
    style = tabs_styles
    )
],
style =  {
    "display":"flex", 
    "flex-direction":"column"
}
)


if __name__ == "__main__":
    app.run_server(debug=True)
