import io
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
from app import app
from apps import exploreview, homepage 
#app = dash.Dash()   #initialising dash app
df = pd.read_csv("rainfall_flood.csv") 
options = []
for col in df.columns:
   options.append({'label':'{}'.format(col, col), 'value':col}) 

layout = html.Div([
        html.Label("Select a feature from drop-down to Explore Statistics "),
        html.P("Select Overall Statistics of your Interest:"),
        dcc.RadioItems(
        id='overallstat', 
        options=[{'value': x, 'label': x} 
                 for x in ['describe', 'count', 'head', 'info', 'etc']],
        value='describe', 
        labelStyle={'display': 'inline-block'}
        ),
        html.Iframe(id='myhtml', 
        style={'width': '80%',
          'height': '567px',
          'textAlign': 'center',
          'margin-left':'12.5%',
          'margin-right':'0'
         }), 
        #html.Graph(id='my_label1'),
  ]) 
@app.callback(
    Output('myhtml', 'src'),
    [Input('overallstat', 'value')]) 
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
