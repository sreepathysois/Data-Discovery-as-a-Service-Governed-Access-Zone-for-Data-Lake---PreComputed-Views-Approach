import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect, discoveryorgoverned, governedzone, creategovernedzone
#app = dash.Dash(__name__, suppress_callback_exceptions=True)
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    dcc.Store(id='session', storage_type='session'), 
    dcc.Store(id='session_seldata', storage_type='session'), 
    dcc.Store(id='session_dataset', storage_type='session'), 
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/exploreview':
        return exploreview.layout
    elif pathname == '/':
        return homepage.layout
    elif pathname == '/overallstat':
        return overallstat.layout
    elif pathname == '/datasetselect':
        return datasetselect.layout
    elif pathname == '/statselection':
        return statselection.layout
    elif pathname == '/overviewstat':
        return overviewstat.layout
    elif pathname == '/univariatestat':
        return univariatestat.layout
    elif pathname == '/bivariatestat':
        return bivariatestat.layout
    elif pathname == '/completestat':
        return completestat.layout
    elif pathname == '/datastat':
        return datastat.layout
    elif pathname == '/discoveryorgoverned':
        return discoveryorgoverned.layout
    elif pathname == '/creategovernedzone':
        return creategovernedzone.layout
    elif pathname == '/governedzone':
        #return governedzone.layout
        return governedzone.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True,host='0.0.0.0')
