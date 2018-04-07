# -*- coding: utf-8 -*-
import pandas as pd
import plotly as py
import plotly.graph_objs as pygo

trace0 = pygo.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = pygo.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = pygo.Data([trace0, trace1])
#
py.offline.plot(data, filename = 'tmp/first_start_introduction.html')
# py.offline.plot(data)  #temp-plot.html
# py.offline.plot(data, filename = 'tmp/first_start_introduction.html',image='png')
#
print('ok')



