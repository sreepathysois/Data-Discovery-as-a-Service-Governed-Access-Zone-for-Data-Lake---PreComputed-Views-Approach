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
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect, discoveryorgoverned 
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
        html.Div(id='mydecisionzone'), 
  ]) 


@app.callback(
              Output('mydecisionzone', 'children'),
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
    querry = "SELECT Access FROM " + ' ' + str(table) + ' ' + cond + '"' +dataset + '"'
    print(querry)
    c=conn.cursor()    
    c.execute(querry)
    #tables = c.fetchall()
    accesspolicy = c.fetchall()
    print(accesspolicy)

    accessrules = []
    for (access,) in accesspolicy:
       accessrules.append(access)
    print(accessrules[0])

    myaccess = accessrules[0]
    print(myaccess)
    if(myaccess == "Public"):
        #data = " Dataset Selected is Public Date, You can Explore this data by click on the button" 
        return  html.Div([html.H1('Welcome to Explore Public Data Set '),
                html.Br(),
                   dcc.Link(
                   html.Button('Explore Data Description and Overall Statistics'),
                   href='/statselection')
               ]) 
        
     
    else:
        data = " Dataset Selected is Private Date, You can Explore this data by Accepting  I agree Button to Governed Acess Zone of Data Lake " 
        return  html.Div([html.H1('Welcome to Governed Data Zone of Data Lake to view Private Dataset or Secure view of Critical Datatset '),
                html.Br(),
                   dcc.Link(
                   html.Button('I agree to privacy and move to Governed Zone'),
                   href='/governedzone')
               ])
        
   #return 'Welcome to Explore Data Selected in Category "{}"'.format(data)



