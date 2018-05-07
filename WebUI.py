'''
Created on Mar 6, 2017

@author: admin
'''
import collections
import json
from flask import Flask
from flask import render_template, request
from scipy.spatial import distance
from munkres import Munkres,print_matrix
import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from datetime import datetime, date, timedelta
app = Flask(__name__, static_url_path='/static')

@app.route('/')
def welcome(name=None):    
      
    return render_template('layout.html', name=name)

@app.route('/compareWeek', methods=['POST'])
def compareOverWeek():
    start_date = datetime.strptime(request.form['startDate'], '%d/%m/%Y')
    end_date  = datetime.strptime(request.form['endDate'], '%d/%m/%Y') 
    weekdays = {"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    day_of_week  = weekdays[request.form['dayOfWeek']]    
    delta = end_date - start_date  
    z = np.array([start_date + timedelta(days=i) for i in range(delta.days + 1)])
    yvals = {"T1":[],"T2":[],"C1":[],"C2":[],"S1":[],"S2":[],"A1":[]}
    count = 0
    for i in range(delta.days + 1):
        temp = start_date + timedelta(days=i)
        if  datetime.weekday(temp) == day_of_week:
            z[count] = temp     
            count = count+1   
            mapping, values1, values2, profiles = compare_clusters('01/03/2017',temp.strftime('%d/%m/%Y'))
            if len(mapping) != 0:
                for j in range(len(mapping)):
                     temp = yvals[profiles[mapping[j][0]]]
                     temp.append(values2[mapping[j][1]])
    content = []    
    for k,v in yvals.items():
        temp = go.Scatter(
                x=z.tolist(),
                y=v,
                name = k,                
                opacity = 0.8)
        content.append(temp)    

    layout = go.Layout(title='Clusters Time Series Plot', width=800, height=640)
    py.sign_in('u1072593', 'yrM7OvBmoOsaIB56gQuB')
    fig = go.Figure(data=content, layout=layout)  
    url = py.plot(fig, filename = 'cluster-comp',auto_open=False,fileopt='overwrite')  
    print(url)
    return json.dumps({'url':url});  
    
@app.route('/compareTimePeriod', methods=['POST'])
def compareOverTime():
    start_date = datetime.strptime(request.form['startDate'], '%d/%m/%Y')
    end_date  = datetime.strptime(request.form['endDate'], '%d/%m/%Y')   
    delta = end_date - start_date  
    z = np.array([start_date + timedelta(days=i) for i in range(delta.days + 1)])
    yvals = {"T1":[],"T2":[],"C1":[],"C2":[],"S1":[],"S2":[],"A1":[]}
    #yvals = {"DNS CLIENTS (Low Volume)":[],"Few Small Flows (TCP)":[],"DNS SERVERS (High Volume)":[],"DNS CLIENTS (High Volume)":[],"DNS SERVERS (Low Volume)":[],"Scanners":[],"Few Small Flows (UDP)":[]}
    #yvals = {"Small UDP Flows":[],"Low DNS Query Responses":[],"Medium TCP Flows":[],"Heavy Incoming DNS Queries":[], "Small TCP Flows":[],"Low Incoming DNS Queries":[],"Heavy DNS Query Responses":[],"Scanners":[]}
    for i in range(delta.days + 1):
        temp = start_date + timedelta(days=i)        
        mapping, values1, values2, profiles = compare_clusters('01/03/2017',temp.strftime('%d/%m/%Y'))
        if len(mapping) != 0:
            for j in range(len(mapping)):
                 temp = yvals[profiles[mapping[j][0]]]
                 temp.append(values2[mapping[j][1]])
    content = []    
    for k,v in yvals.items():
        temp = go.Scatter(
                x=z.tolist(),
                y=v,
                name = k,                
                opacity = 0.8)
        content.append(temp)    

    layout = go.Layout(title='Clusters Time Series Plot', width=800, height=640)
    py.sign_in('u1072593', 'yrM7OvBmoOsaIB56gQuB')
    fig = go.Figure(data=content, layout=layout)  
    url = py.plot(fig, filename = 'cluster-comp',auto_open=False,fileopt='overwrite')  
    print(url)
    return json.dumps({'url':url});  
    
@app.route('/compare', methods=['POST'])
def compare():    
    start_date = request.form['startDate']
    end_date = request.form['endDate']
    mapping, values1, values2, profiles = compare_clusters('01/03/2017',start_date)
    json_data = {}
    new_profiles= {}
    for i in range(len(profiles)):
        json_data[profiles[i]] = [] 
    for i in range(len(mapping)):   
        new_profiles[mapping[i][1]]=profiles[mapping[i][0]]      
        json_data[profiles[mapping[i][0]]].append({            
            'day1':values2[mapping[i][1]]            
            })   
    mapping, values1, values2, profile = compare_clusters(start_date,end_date)
    for i in range(len(mapping)):        
        json_data[new_profiles[mapping[i][0]]].append({            
            'day2':values2[mapping[i][1]]            
            })  
    
    return json.dumps({'output':json_data});

    

def addconnection(i,j,c):
  return [((-1,1),(i-1,j-1),c)]
def drawnodes(s,i,ax):
  
  if(i==1):
    color='r'
    posx=1
  else:
    color='b'
    posx=-1
  posy=0
  for n in s:
    plt.gca().add_patch( plt.Circle((posx,posy),radius=0.05,fc=color))
    if posx==1:
      ax.annotate(n,xy=(posx,posy+0.1))
    else:
      ax.annotate(n,xy=(posx-len(str(n))*0.1,posy+0.1))
    posy+=1
def compare_clusters(start_date,end_date):        
    centres1 = []
    centres2 = []
    set1={}
    set2={}
    with open('data.txt') as json_file:  
        data = json.load(json_file)    
    if end_date not in data:
        return centres1,centres2,set1,set2
    centres1 = data[start_date][0]['cluster_centers']
    centres2 = data[end_date][0]['cluster_centers']
    set1 = data[start_date][0]['cluster_sizes']
    set2 = data[end_date][0]['cluster_sizes']
    profiles = []
    if start_date == '01/03/2017':
        od = collections.OrderedDict(sorted(data[start_date][0]['cluster_mappings'].items()))   
        profiles = [v for k, v in od.items()] 
    matrix = distance.cdist(centres1, centres2, 'euclidean')
    matrix[0][0] = 1
    matrix[1][1] = 1
    matrix[2][2] = 1
    matrix[3][3] = 1
    matrix[4][4] = 1
    matrix[5][5] = 1
    matrix[6][6] = 1
    #print(matrix)
    
    m = Munkres()
    indexes = m.compute(matrix)
    #print(matrix) 
    
    temp_matrix = distance.cdist(centres1, centres2, 'euclidean')
    temp_matrix[0][0] = 1
    temp_matrix[1][1] = 1
    temp_matrix[2][2] = 1
    temp_matrix[3][3] = 1
    temp_matrix[4][4] = 1
    temp_matrix[5][5] = 1
    temp_matrix[6][6] = 1
    total = 0
    mapping=[]
    for row, column in indexes:        
        value = temp_matrix[row][column]
        total += value
        temp =[]
        temp.append(row)
        temp.append(column)
        #print( '(%d, %d) -> %f' % (row, column, value))        
        mapping.append(temp)
    print(total)
    ax=plt.figure().add_subplot(111)
    od = collections.OrderedDict(sorted(set1.items()))
    value1 = [v for k, v in od.items()]
    #print(value1)
    od = collections.OrderedDict(sorted(set2.items()))   
    value2 = [v for k, v in od.items()]
    #print(value2)
    plt.axis([-2,2,-1,max(len(value1),len(value2))+1])
    frame=plt.gca()
    frame.axes.get_xaxis().set_ticks([])
    frame.axes.get_yaxis().set_ticks([])
    drawnodes(value1,1,ax)
    drawnodes(value2,2,ax)
    connections=[]
    for i in range(len(mapping)):
        connections+=addconnection(mapping[i][1]+1,mapping[i][0]+1,'g') 
    for c in connections:
        plt.plot(c[0],c[1],c[2], label ='Numbers indicate Cluster Sizes')
    plt.title('Comparison of clusters formed on days '+start_date+' and '+end_date)    
    plt.xlabel('Numbers indicate cluster sizes')
    #plt.show()     
    #plt.savefig('result.png')  
    plt.close()   
    return  mapping, value1, value2, profiles
    
        
if __name__ == '__main__':  # Script executed directly?
    app.run()  # Launch built-in web server and run this Flask webapp