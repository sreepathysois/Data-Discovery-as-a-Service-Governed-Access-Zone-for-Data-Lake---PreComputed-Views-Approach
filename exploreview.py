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

conn = mysql.connector.connect(host="172.16.51.28", user="sois", password="Msois@123", database="weatherdata")
c = conn.cursor()
c.execute(" SHOW TABLES ") 	
tables = c.fetchall() 

#app = dash.Dash()
#app = dash.Dash(__name__)

#trends = ['python', 'flask', 'java']

exploreview = html.Div(
    html.Div(
        className="trend",
        children=[
            #html.Ul(id='my-list', children=[html.Li(i) for i in tables])
            dcc.Link(id='my-list', children=[html.Li(i) for i in tables], href='/dataexplore')
        ],
    )
)

if __name__=='__main__':
    app.run_server(debug=True,host='0.0.0.0') 

