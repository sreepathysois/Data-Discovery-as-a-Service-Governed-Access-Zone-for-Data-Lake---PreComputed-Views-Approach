import io
import socket
import paramiko
import pandas as pd
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import mysql.connector
import os
import cryptography
from cryptography.fernet import Fernet
from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect, discoveryorgoverned, governedzone, creategovernedzone 
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
            html.H1('Welcome to Creation of Governed Access Zone of Data lake to explore critical Data of Organization'),
            html.P('Privacy Data of Orzanization is Described Using Encryption and Pilocy are Implemented'),
            html.Br(),
            html.Button('Click to Create Self Destructive  Governed Zone Environment', id='stackcreate'),
            html.Button('Check the status of Create Environment', id='stackstatus'),
            html.Button('Acess Governed zone and Prepare data', id='myenv'),
                  
                
        html.Div(id='creategovernedzone'), 
  ]) 


@app.callback(
              Output('creategovernedzone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('stackcreate','n_clicks'), 
               Input('stackstatus','n_clicks'), 
               Input('myenv','n_clicks')] 
              )
def selectionresult(dataset,tabledata,dbdata,n_stackcreate, n_stackstatus,n_myenv):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    print(table)
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]  
    if 'stackcreate' in changed_id:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        #servername = "sree" + "_" + dataset + "_" + tabledata 
        servername = "pathy" + "_" + "governed_zone_data_lake"  
        #create_comd = "source keystonerc_admin && openstack stack create -t UpdatedQtInstanceDockerNovnc.yaml " + "  " + "--parameter" + " " + "name=" + servername  
        #create_comd = "source keystonerc_admin && openstack stack create -t UpdateQtInstanceDockerQtEncrypt.yaml " + "  " + "--parameter" + " " + "name=" + servername  
        create_comd = "source keystonerc_admin && openstack stack create -t UpdateQtInstanceDockerQtViews.yaml " + "  " + "--parameter" + " " + "name=" + servername  
        #stackname = "sree" + '_' + dataset + '_' +  tabledata 
        stackname = "pathy" + "_" + "governed_zone_data_lake"  
        print(create_comd + ' ' +stackname) 
        #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin && openstack stack create -t QtInstaceDockerNovnc.yaml qtdash  ")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(create_comd + ' ' + stackname)
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 
        output = ssh_stdout.read().decode()
        print(output)
        return html.Span('Output of command is "{}"'.format(output)) 


    #if n_status is None:
        #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    elif 'stackstatus' in changed_id:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        status_comd = "source keystonerc_admin && openstack stack list | grep "
        #stackname = "sree" +  dataset +  tabledata 
        #stackname = "sree" + '_' + dataset + '_' +  tabledata 
        stackname = "pathy" + "_" + "governed_zone_data_lake"  
        
        #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin && openstack stack list | grep qtdash  ")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(status_comd + ' ' + stackname)
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 
        output = ssh_stdout.read().decode()
        print(output)

        #for line in ssh_stdout:
        #    print(line.strip())
        #    output = line.strip()
        #return 'Category of Data Selected is  "{}"'.format(dbdata)
        #return 'Database Selected is "{}"'.format(tabledata)  
        #return 'Dataset Selected is "{}"'.format(dataset) 
        #return 'Category of Data Selected is  "{}"'.format(dbdata) + '\n' + 'Database Selected is "{}"'.format(tabledata) + '\n' +   'Dataset Selected is "{}"'.format(dataset) +  '\n' + 'Output of command is "{}"'.format(line) 
        return html.Span('Output of command is "{}"'.format(output)) 
        #return "Elephants are the only animal that can't jump"



     
    #if n_envlink is None:
        #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    elif 'myenv' in changed_id:
         return  html.Div([html.H1('Welcome to Explore Private Data Set and Make Sure you Create Your Governed Zone Environment before you try to access it'),
                 html.Br(),
                   dcc.Link(
                   html.Button('Acess your Environment'),
                   href='/governedzone')
               ])


