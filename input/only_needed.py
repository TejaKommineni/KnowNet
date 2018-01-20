import csv
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas
import matplotlib.pyplot as plt
from matplotlib import mlab

def only_needed():    
    out = csv.writer(open("essential-flows-2017-12-05.csv","w"), delimiter=',',quoting=csv.QUOTE_ALL)
    out.writerow('source_ip,destination_ip,source_port,destination_port,protocol,tcp_flags,duration,packets,bytes'+"\n")
    i =0
    with open('features-flows-2017-12-05.csv', 'rU') as f:
        reader = csv.reader(f)
        for rec in csv.reader(f, delimiter=','):
            print(i)
            i = i +1
            with open('clustered-aggregated-features-flows-2017-12-05.csv', 'rU') as f1:
                reader1 = csv.reader(f1)
                for rec1 in csv.reader(f1, delimiter=','):
                    temp = rec1[0] 
                    temp = temp[1:]
                    temp = temp[:len(temp)-1]
                    if temp== rec[0]:
                        out.writerow(rec)
                        print(rec)
                       
            f1.close()            
    f.close()
    out.close()
 
def hist_bytes_distribution():
    colnames = ['byte_count']
    d =  pandas.read_csv('test.csv', names=colnames)
    x = d.byte_count.tolist()
    #===========================================================================
    # cumsum = np.cumsum(x)
    # trace = go.Scatter(x=[i for i in range(len(cumsum))], y=10*cumsum/np.linalg.norm(cumsum),
    #                  marker=dict(color='rgb(150, 25, 120)'))
    # layout = go.Layout(
    #     title="Cumulative Distribution Function"
    # )
    # fig = go.Figure(data=go.Data([trace]), layout=layout)
    # #data = [go.Histogram(x=x,cumulative=dict(enabled=True))]
    # py.sign_in('u1072593', 'yrM7OvBmoOsaIB56gQuB')
    # #fig = go.Figure(data=data)  
    # url = py.plot(fig, filename = 'hist-comp',auto_open=False,fileopt='overwrite')  
    # print(url)
    # mu = 200
    #===========================================================================
        
    n, bins, patches = plt.hist(x, 50, normed=1,
                                histtype='step', cumulative=True)
    
    
    plt.title('cumulative step')
    
    plt.show()
    
hist_bytes_distribution()                    
#only_needed()    