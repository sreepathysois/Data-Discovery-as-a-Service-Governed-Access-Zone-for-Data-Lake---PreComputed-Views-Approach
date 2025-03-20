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
from app import app
from apps import homepage, exploreview, overallstat, statselection, overviewstat,univariatestat, bivariatestat, completestat, datastat, datasetselect, discoveryorgoverned, governedzone 
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
            html.H1('Welcome to Governed Access Zone of Data lake to explore critical Data of Organization'),
            html.P('Privacy Data of Orzanization is Described Using Encryption and Pilocy are Implemented'),
            html.Br(),
            html.Button('I Agree Policy of Data Lake and Use Governed Zone ', id='agree'),
            html.Button('Click to Create Self Destructive  Governed Zone Environment', id='create'),
            html.Button('Check the status of Create Environment', id='status'),
            html.Button('View is Environment Accesable ', id='accesable'),
            html.Button('View the link to Access Environment', id='envlink'),
                  
                
        html.Div(id='governedzone'), 
        html.Div(id='createzone'), 
        html.Div(id='statuszone'), 
        html.Div(id='accesablezone'), 
        html.Div(id='envlinkzone'), 
  ]) 


@app.callback(
              Output('governedzone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('agree','n_clicks')] 
              )
def selectionresult(dataset,tabledata,dbdata,n_agree):
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
    location = c.fetchall()
    print(location)

    filepath = []
    for (loc,) in location:
       filepath.append(loc)
    print(filepath[0])

    myfilepath = filepath[0]
    #data = " Dataset Selected is Public Date, You can Explore this data by click on the button" 
    #if n_clicks is None:
        #raise "" 
    #    return "Please Click on Agree Button to Move to Governed Zone"
    if n_agree:
        """
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)

        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin && openstack server list")
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
        """ 
        return html.Span('Category of Data Selected is  "{}"'.format(dbdata) + '\n' + 'Database Selected is "{}"'.format(tabledata) + '\n' +   'Dataset Selected is "{}"'.format(dataset) +  '\n' + 'Select Create Button to Launch your Self Destructive Zone ') 
        #return "Elephants are the only animal that can't jump"
    
     

@app.callback(
              Output('createzone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('create','n_clicks')]  
              )
def selectionresult(dataset,tabledata,dbdata,n_create):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
       
    #if n_create is None:
    #    #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    if n_create :
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        create_comd = "source keystonerc_admin && openstack stack create -t  QtInstaceDockerNovnc.yaml "
        stackname = "qtdash"  + dataset +   tabledata 
        print(create_comd + ' ' +stackname) 
        #ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin && openstack stack create -t QtInstaceDockerNovnc.yaml qtdash  ")
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(create_comd + ' ' + stackname)
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error 
        output = ssh_stdout.read().decode()
        print(output)
        return html.Span('Output of command is "{}"'.format(output)) 


@app.callback(
              Output('statuszone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('status','n_clicks')]  
              )
def selectionresult(dataset,tabledata,dbdata,n_status):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    #if n_status is None:
        #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    if n_status:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        status_comd = "source keystonerc_admin && openstack stack list | grep "
        stackname = "qtdash" +  dataset +  tabledata 
        
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



@app.callback(
              Output('accesablezone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('accesable','n_clicks')]  
              )
def selectionresult(dataset,tabledata,dbdata,n_accesable):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    #if n_accesable is None:
        #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    if n_accesable:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin &&  openstack server  show qtviewappfloat | grep private_network")
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error
        result = ssh_stdout.read().decode()
        print(result)
        address = result.split("private_network")[1]
        floatip = address.split(",")[1]
        publicip = floatip.split("|")[0]
        serverip = publicip.split(" ")[1] 
        print(address)
        print(floatip)
        print(publicip)
        print(serverip)
        a_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        a_socket.settimeout(2)    
       	location = ( str(serverip), 6080)
        print(location)
        result_of_check = a_socket.connect_ex(location)

        if result_of_check == 0:
           status = "Environment is up and running open"
           a_socket.close()
           return html.Span('Status of Environment  is "{}"'.format(status)) 
        else:
           status = "Env is still under creation "
           a_socket.close()
           return html.Span('Status of Environment  is "{}"'.format(status)) 
 

@app.callback(
              Output('envlinkzone', 'children'),
              [Input('session_dataset', 'data'),
               Input('session_seldata','data'), 
               Input('session','data'), 
               Input('envlink','n_clicks')]  
              )
def selectionresult(dataset,tabledata,dbdata,n_envlink):
    database = dbdata 
    print(database)
    conn = mysql.connector.connect(host="mysql", user="sois", password="Msois@123", database=str(dbdata))
    table = tabledata
    #if n_envlink is None:
        #raise "" 
    #    return "Please Click on Create Button to Create Secure Governed Zone"
    if n_envlink:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_host_keys(os.path.expanduser('~/.ssh/known_hosts'))
        ssh.connect("172.16.51.22", username="root", password="openstack", port=22)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("source keystonerc_admin &&  openstack server  show qtviewappfloat | grep private_network")
        exit_code = ssh_stdout.channel.recv_exit_status() # handles async exit error
        result = ssh_stdout.read().decode()
        print(result)
        address = result.split("private_network")[1]
        floatip = address.split(",")[1]
        publicip = floatip.split("|")[0]
        serverip = publicip.split(" ")[1]
        link = "http://" + serverip + ":6080/vnc.html"
        return html.Span('Link of Environment  is "{}"'.format(link)) 
