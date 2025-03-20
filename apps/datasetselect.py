import dash
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_extensions import Download
import dash_core_components as dcc
import dash_table
import pandas as pd
import mysql.connector 
import base64
import io, os, sys, time 
from app import app
from apps import homepage, overallstat, exploreview, datastat, statselection, datasetselect 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

"""
conn = mysql.connector.connect(host="172.16.51.38", user="sois", password="Msois@123", database="weatherdata")
global category 
#category=database 
#print(category)
#conn = mysql.connector.connect(host="172.16.51.28", user="sois", password="Msois@123",database=category)
c = conn.cursor()
c.execute(" SHOW TABLES ") 	
tables=c.fetchall() 
"""
"""
for (table_name,) in databases:
      print(db_name) 
      #mytables.append=table_name 
print(mytables) 
"""
#trends = ['python', 'flask', 'java']
"""
options = []
for (table_name,) in tables:
   options.append({'label':'{}'.format(table_name,table_name), 'value':table_name})
#print(options)

#app = dash.Dash()
#app = dash.Dash(__name__)
"""
#trends = ['python', 'flask', 'java']
layout= html.Div([
    #dcc.Link('Explore Dataset', href='/overallstat'), 
    html.H1(id='dataresults'),
    html.H1("Explore DataSets available  in Your Selected Category"), 
    #html.Div(id='page-content-explore'), 
    html.Div(
    dcc.RadioItems(
    id = 'datasets',
    #options= options, 
    labelStyle={'display': 'inline-block'}
    ), 


 
        

    ), 

    dcc.Link(html.Button("Explore Dataset in your Intrested Category"), href="/discoveryorgoverned", refresh=True),
    ]) 

@app.callback( 
              Output('datasets', 'options'),
              [Input('session', 'data'), 
               Input('session_seldata', 'data')],
              )
def result(db,table):
    #global category
    category=db 
    #return category
    #return 'Welcome to Explore Data Selected in Category "{}"'.format(data)
    print(category)
    print(table)
    #database=   
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123",database=str(db))
    c = conn.cursor()
    querry="SELECT TableName FROM" + ' ' + str(table) 
    c.execute(querry) 	
    tablesname=c.fetchall() 
    options = []
    for (table_name,) in tablesname:
       options.append({'label':'{}'.format(table_name,table_name), 'value':table_name})
    return options
    #return 'Welcome to Explore Data Selected in Category "{}"'.format(data) 
    #return data



@app.callback(
    Output('session_dataset', 'data'),  # whatever this will be
    [Input('datasets', 'value')]) 
def select_dataset(value):
    data=value   
    return data  


"""
@app.callback(
    Output('my-output', 'value'),  # whatever this will be
    [Input('results', 'children')]) 
def use_df_callback(data):
    global category
    category=data 
    print(category)
    return category  
"""
