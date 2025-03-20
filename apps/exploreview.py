import dash
import dash_html_components as html
#from dash import Dash, dash_table, dcc, html
from dash.dependencies import Input, Output
from dash_extensions import Download
import dash_core_components as dcc
import dash_table
import pandas as pd
import mysql.connector 
import base64
import io, os, sys, time 
from app import app
from apps import homepage, overallstat, statselection, exploreview,datastat, datasetselect, overviewstat, univariatestat, bivariatestat, completestat 
#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
colors = {
    'background': '#111111',
    'text': '#FFFFFF'
}


#conn = mysql.connector.connect(host="172.16.51.28", user="sois", password="Msois@123", database="weatherdata")
conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123")
c = conn.cursor()
c.execute(" SHOW DATABASES  ") 	
databases = c.fetchall() 
"""
for (table_name,) in tables:
      print(table_name) 
      #mytables.append=table_name 
print(mytables) 
"""
#trends = ['python', 'flask', 'java']
options = []
for (db_name,) in databases:
   db_name_str = db_name.decode('utf-8')  # Decode bytearray to string
   options.append({'label': db_name_str, 'value': db_name_str})
   #options.append({'label':'{}'.format(db_name,db_name), 'value':db_name})
#print(options)

#app = dash.Dash()
#app = dash.Dash(__name__)

#trends = ['python', 'flask', 'java']
layout = html.Div([
    #dcc.Link('Explore Dataset', href='/overallstat'), 
    html.H1("Data Lake  Data Discovery Service",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
), 
    html.H2("Select the Category or Domain of Data in DataLake of an Organization",  style={
            'textAlign': 'center',
            #'color': colors['text']
        }
), 

    #html.Div(id='page-content-explore'), 
    html.Div(
    dcc.RadioItems(
    id = 'mycategories',
    options= options, 
    #labelStyle={'display': 'inline-block'}
    labelStyle={'display': 'block',  'margin-right': '20px',
                    'font-weight': 300}
    ), 
      
        

), 

dcc.Link(html.Button("Explore Dataset Within Your Selected Catefory",), href="/overallstat", refresh=True)])


@app.callback(Output('session', 'data'),
              [Input('mycategories', 'value')]
)
def get_category_value(value):
     data = value
     return data
     #return {'database': value}

