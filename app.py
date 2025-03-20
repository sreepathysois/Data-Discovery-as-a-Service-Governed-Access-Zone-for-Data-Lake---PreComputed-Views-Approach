import dash
app = dash.Dash(__name__, suppress_callback_exceptions=True)
#app = dash.Dash(__name__)
server = app.server
app.title = 'Plotly Dash Multipage Template App'
