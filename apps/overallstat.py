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
from apps import homepage, overallstat, exploreview, datastat, statselection, datasetselect, overviewstat, univariatestat, bivariatestat, completestat 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)

"""
conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database="weatherdata")
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
     html.H1("Data Lake  Data Discovery Service",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
),

    html.H1(id='results'),
    html.H2("Explore Databases related to Category selected" ,style={
            'textAlign': 'center',
            #'color': colors['text']
        }
), 
    #html.Div(id='page-content-explore'), 
    html.Div(
    dcc.RadioItems(
    id = 'mydatasets',
    #options= options, 
    labelStyle={'display': 'block',  'margin-right': '20px',
                    'font-weight': 300}
    #),
    #labelStyle={'display': 'inline-block'}
    ), 


 
        

    ), 

    dcc.Link(html.Button("Explore Dataset in your Intrested Category"), href="/datasetselect", refresh=True),
    ]) 

@app.callback( 
              Output('mydatasets', 'options'),
              [Input('session', 'data')],
              )
def result(data):
    global category
    category=data 
    #return category
    #return 'Welcome to Explore Data Selected in Category "{}"'.format(data)
    print(category)
    #database=   
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123",database=str(data))
    c = conn.cursor()
    c.execute(" SHOW TABLES ") 	
    tables=c.fetchall() 
    options = []
    for (table_name,) in tables:
       table_name_str = table_name.decode('utf-8')  # Decode bytearray to string
       options.append({'label': table_name_str, 'value': table_name_str})
       #options.append({'label':'{}'.format(table_name,table_name), 'value':table_name})
    return options
    #return 'Welcome to Explore Data Selected in Category "{}"'.format(data) 
    #return data



@app.callback(
    Output('session_seldata', 'data'),  # whatever this will be
    [Input('mydatasets', 'value')]) 
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
