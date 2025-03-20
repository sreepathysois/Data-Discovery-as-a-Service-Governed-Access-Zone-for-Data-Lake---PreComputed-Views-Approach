import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from dash_extensions import Download
import pandas as pd
import mysql.connector 
import base64
import io, os, sys, time 

from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)


def write_file(data, filename):
    with open(filename, 'wb') as f:
        f.write(data)


"""
conn = mysql.connector.connect(host="172.16.51.38", user="sois", password="Msois@123", database="weatherdata")
c = conn.cursor()
c.execute('SELECT OverallStat FROM weather WHERE Id=200' )
query_results = c.fetchall() 
myfile = query_results[0][0]
mypdf = base64.b64decode(myfile)
write_file(mypdf, 'assets/overall.pdf')
c.execute('SELECT AttributeStat FROM weather WHERE Id=200' )
query_results1 = c.fetchall() 
myfile1 = query_results1[0][0]
mypdf1 = base64.b64decode(myfile1)
write_file(mypdf1, 'assets/graph.pdf')
"""


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server



layout = html.Div([
        html.Div([
        html.H1('Overall Statistics'),
        html.H1(id='mycompletestat'),
        dcc.RadioItems(
        id='completestat',
        options=[{'value': x, 'label': x}
                 for x in ['overallstat', 'graphstat', 'metadatastat']],
        #value='overallstat',
        labelStyle={'display': 'inline-block'}
        ),
         html.Iframe(id='overstat',
        style={'width': '80%',
          'height': '567px',
          'textAlign': 'center',
          'margin-left':'12.5%',
          'margin-right':'0'
         }),
        """ 
        html.ObjectEl(id='overstat', 
            # To my recollection you need to put your static files in the 'assets' folder
            #data="assets/overall.pdf",
            type="application/pdf",
            style={"width": "800px", "height": "600px"}
        
       ),
       """
        ], className="six columns"),

])

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})

@app.callback(
    Output('overstat', 'src'),
    [Input('completestat', 'value')]

    )
def update_dropdown(value):
   if(value=='overallstat'):
     data = 'assets/overall.pdf' 
     return data 

   elif(value=='graphstat'):
     data = 'assets/graph.pdf' 
     return data 
   
   elif(value=='metadatastat'):
     data = 'assets/meta.txt' 
     return data 





@app.callback(
              Output('mycompletestat', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'),
               Input('session','data')]
              )
def selectionresult(dataset,tabledata,dbdata):
    database = dbdata
    table=tabledata
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    c=conn.cursor()
    cond="WHERE TableName="
    querry = "SELECT OverallStat FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()
    c.execute(querry)
    #tables = c.fetchall()
    query_results = c.fetchall() 
    myfile = query_results[0][0]
    mypdf = base64.b64decode(myfile)
    write_file(mypdf, 'assets/overall.pdf')

    cond="WHERE TableName="
    querry = "SELECT AttributeStat FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()
    c.execute(querry)
    #tables = c.fetchall()
    query_results = c.fetchall() 
    myfile = query_results[0][0]
    mypdf = base64.b64decode(myfile)
    write_file(mypdf, 'assets/graph.pdf')

    cond="WHERE TableName="
    querry = "SELECT Metadata FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()
    c.execute(querry)
    #tables = c.fetchall()
    query_results = c.fetchall() 
    myfile = query_results[0][0]
    mypdf = base64.b64decode(myfile)
    write_file(mypdf, 'assets/meta.txt')
    data="CompleteStatistics" 
    return 'Welcome to Explore Dataset Selected by You "{}"'.format(data)
