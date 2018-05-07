import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np

#===============================================================================
# x = np.random.randint(5, size=1159)+1
# print(x)
# data = [go.Histogram(x=x,
#                      cumulative=dict(enabled=True))]
# 
# layout = go.Layout(
#     showlegend=False,
#     annotations=[
#         dict(
#             x=3,
#             y=685,
#             xref='x',
#             yref='y',
#             text='(3,685)',
#             showarrow=True,
#             arrowhead=7,
#             ax=0,
#             ay=-40
#         )
#     ]
# )
# fig = go.Figure(data=data, layout=layout)
# py.sign_in('u1072593', 'yrM7OvBmoOsaIB56gQuB')
# py.plot(fig, filename='cumulative histogram')
#===============================================================================

N = 1139
random_x = np.random.randint(low = 30, high=100,size=1139)+1
random_y0 = np.random.randint(low = 1, high=5 , size=1139)+1

# Create traces
trace0 = go.Scatter(
    x = random_x,
    y = random_y0,
    mode = 'markers',
    name = 'markers'
)

data = [trace0]
py.sign_in('u1072593', 'yrM7OvBmoOsaIB56gQuB')
py.plot(data, filename='cumulative histogram')