# # 2.10-2 Overlaid Histgram
import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot
s1 = np.random.RandomState(1)
x0 = s1.randn(1000)
x1 = s1.chisquare(5,1000)

trace1 = go.Histogram(
    x = x0,
    histnorm = 'probability',
    opacity = 0.75
)
trace2 = go.Histogram(
    x = x1,
    histnorm = 'probability',
    opacity = 0.75
)

data = [trace1, trace2]
layout = go.Layout(barmode='overlay')
fig = go.Figure(data = data, layout = layout)
pyplt(fig, filename='tmp/overlaid_histogram.html')
