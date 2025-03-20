import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px
from app import app, server
from apps import dashboard, dashboard2, exploreview 
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
df1 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')
def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

fig.update_layout(
    #plot_bgcolor=colors['background'],
    #paper_bgcolor=colors['background'],
    font_color=colors['text']
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(children=[
    html.H1(
        children='Welcome to MSIS Data Lake Discovery Portal',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.H4(children='Portal Describe Overall Statistics and List categories of Data', style={
        'textAlign': 'center',
        'color': colors['text']
 }),

    html.Div([
        html.Div(children=[
            html.H4(children='Discover your Data of Intrest',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }), 
        
            dcc.Link(
            children='Understand Overall Statistics of Data',
            href='/understanddata', 
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
            #html.H3('Column 1'),
            dcc.Graph(id='g1', figure=fig)
        ], className="six columns"),

        html.Div([
            html.Div(children=[
            html.H2(
            children='Explore Data of Different Domain',
            style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
            dcc.Link(
            children='Select Data from Different Category of your Intrest',
            href='/exploreview',
            style={
            'textAlign': 'center',
            'color': colors['text'] 

     }), 
    
           html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df1)
    ]),

           #dcc.Graph(id='g2', figure={'data': [{'y': [1, 2, 3]}]})
        ], className="six columns"),
    ], className="row")

])

])

])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/exploreview':
        return exploreview.layout 
    elif pathname == '/dashboard2':
         return dashboard2.get_dashboard2_layout(df)
    else:
        return dashboard.get_dashboard_layout(df)

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
