import io
import os
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import mysql.connector

from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

#app = dash.Dash()   #initialising dash app

global df 
#df = pd.read_csv("rainfall_flood.csv") 
"""
options = []
for col in df.columns:
   options.append({'label':'{}'.format(col, col), 'value':col}) 
"""
layout = html.Div([
        html.H1(id='myresults2'), 
        html.Label("Select a feature from drop-down to plot HISTOGRAM"),
        dcc.Dropdown(
            id = 'my_dropdown1',
            #options=options,
            #value='Choose columns'
        ),
        dcc.Graph(id='my_label1'),
  ]) 

@app.callback(
    Output('my_label1', 'figure'),
    [Input('my_dropdown1', 'value')]
    )
def update_dropdown(value):
   x=['{}'.format(value)]
   fig = px.histogram(df,x)
   #fig.show() 
   return fig


@app.callback(
              Output('my_dropdown1', 'options'),
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
    """
    querry = "SELECT * FROM " + table
    c = conn.cursor()
    #c.execute(querry)
    #tables = c.fetchall()
    #c.execute(" SELECT * FROM rainfalldata ")
    global df
    #df = pd.DataFrame(c.fetchall())
    df=pd.read_sql(querry,con=conn)
    #df=pd.read_csv("rainfall_flood.csv")   
    """
    c=conn.cursor()
    cond="WHERE TableName="
    querry = "SELECT Location FROM " + ' ' + str(tabledata) + ' ' + cond + '"' +dataset + '"'
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
    options = []
    for col in df.columns:
       options.append({'label':'{}'.format(col, col), 'value':col}) 
    print(options)
    print(df.head(2))
    return options 

