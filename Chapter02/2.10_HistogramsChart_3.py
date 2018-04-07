# # 2.10-3 Stacked Histograms
import plotly as py
import plotly.graph_objs as go
import numpy as np
pyplt = py.offline.plot

s1 = np.random.RandomState(1)
x0 = s1.randn(1000)
x1 = s1.randn(1000)

trace0 = go.Histogram(
    x=x0
)
trace1 = go.Histogram(
    x=x1
)
data = [trace0, trace1]
layout = go.Layout(barmode='stack')
fig = go.Figure(data=data, layout=layout)

pyplt(fig, filename='tmp/stacked_histogram.html')
