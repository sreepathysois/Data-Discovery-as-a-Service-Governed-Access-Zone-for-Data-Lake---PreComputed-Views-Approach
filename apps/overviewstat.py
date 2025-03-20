import io
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import mysql.connector
import os
from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

global df
#app = dash.Dash()   #initialising dash app
#df = pd.read_csv("rainfall_flood.csv") 
"""
options = []
for col in df.columns:
   options.append({'label':'{}'.format(col, col), 'value':col}) 
"""
layout = html.Div([
        html.H1(id='myresults1'), 
        html.Label("Select a feature from drop-down to Explore Statistics "),
        html.P("Select Overall Statistics of your Interest:"),
        dcc.RadioItems(
        id='overallstats', 
        options=[{'value': x, 'label': x} 
                 for x in ['describe', 'count', 'head', 'info', 'etc']],
        #value='describe', 
        labelStyle={'display': 'inline-block'}
        ),
        html.Iframe(id='myhtml1', 
        style={'width': '80%',
          'height': '567px',
          'textAlign': 'center',
          'margin-left':'12.5%',
          'margin-right':'0'
         }), 
        #html.Graph(id='my_label1'),
  ]) 

@app.callback(
    Output('myhtml1', 'src'),
    [Input('overallstats', 'value')] 
   
    
    )
def update_dropdown(value):
   if(value=='describe'):
     desc=df.describe() 
     desc.to_html('assets/desc.html')
     path='assets/desc.html'
     return path

   elif(value=='head'):
     head=df.head(20) 
     head.to_html('assets/head.html')
     path='assets/head.html'
     return path

   elif(value=='count'):
     count=df.count()
     count.to_csv('assets/count.txt', sep=',', index=True) 
     path='assets/count.txt'
     return path 

   elif(value=='info'):
     buffer=io.StringIO()
     info=df.info(buf=buffer)
     s=buffer.getvalue()
     with open("assets/info.txt", "w", encoding="utf-8") as f:
        f.write(s)
     path='assets/info.txt'
     return path 

@app.callback(
              Output('myresults1', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data')]
              )
def selectionresult(dataset,tabledata,dbdata):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    print(table)
    global df
    # Code for version 1 for direct fetch of table data
    """ `
    querry = "SELECT * FROM " + table 
    c = conn.cursor()
    #c.execute(querry)
    #tables = c.fetchall()
    #c.execute(" SELECT * FROM rainfalldata ")
    global df
    #df = pd.DataFrame(c.fetchall())
    df=pd.read_sql(querry,con=conn) 
    options = []
    #for col in df.columns:
    #   options.append({'label':'{}'.format(col, col), 'value':col}) 
    #df = pd.DataFrame(c.fetchall())
    #options=[{'value': x, 'label': x} 
    #  for x in ['describe', 'count', 'head', 'info', 'etc']],
    return df 

    """
    cond="WHERE TableName="
    querry = "SELECT Location FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()    
    c.execute(querry)
    #tables = c.fetchall()
    locationpath = c.fetchall()
    print(locationpath)

    filepath = []
    for (location,) in locationpath:
       filepath.append(location)
    print(filepath[0])


    querry='sshpass -p "university" scp' + ' '  + str(filepath[0]) + ' ' + 'assets/data.csv'
    print(querry)
    os.system(querry )
    df=pd.read_csv('assets/data.csv') 
    return df


