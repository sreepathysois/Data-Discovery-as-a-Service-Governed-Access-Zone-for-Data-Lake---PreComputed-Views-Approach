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
import paramiko

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
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin &&  openstack stack list | grep pathy_governed_zone_data_lake")
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error
        stackname = "pathy" + "_" + "governed_zone_data_lake"
        result = ssh_stdout.read().decode()
        if(result == ""):
             status = "NO_STACK"
             print(status)
        else: 
             status = result.split("|")[4]
             status = status.split(" ")[1]
             print(status)
        if(status== "CREATE_COMPLETE"):
             print("status up")
             data = " Dataset Selected is Private Date, You can Explore this data by Accepting  I agree Button to Governed Acess Zone of Data Lake " 
             return  html.Div([html.H1('Welcome to Governed Data Zone of Data Lake to view Private Dataset or Secure view of Critical Datatset '),
                   html.Br(),
                   dcc.Link(
                   html.Button('I agree to privacy and move to Governed Zone'),
                   href='/governedzone')
                   ])
        else:
            print("status down")
            data = " Dataset Selected is Private Date, You can Explore this data by Creating Self Destructive Stack " 
            return  html.Div([html.H1('Welcome to Governed Data Zone of Data Lake to view Private Dataset or Secure view of Critical Datatset '),
                    html.Br(),
                    dcc.Link(
                    html.Button('I agree to privacy and move to Governed Zone'),
                    href='/creategovernedzone')
                    ])
        """ 
        data = " Dataset Selected is Private Date, You can Explore this data by Accepting  I agree Button to Governed Acess Zone of Data Lake " 
        return  html.Div([html.H1('Welcome to Governed Data Zone of Data Lake to view Private Dataset or Secure view of Critical Datatset '),
                html.Br(),
                   dcc.Link(
                   html.Button('I agree to privacy and move to Governed Zone'),
                   href='/governedzone')
               ])
        
   #return 'Welcome to Explore Data Selected in Category "{}"'.format(data)

      """

