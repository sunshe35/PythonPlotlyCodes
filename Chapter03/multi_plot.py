
import plotly as py
import plotly.graph_objs as go

# ----------pre def
pyplt = py.offline.plot

x = list('ABCDEF')
trace1 = go.Scatter(
    x=x,
    y=[1.5, 1, 1.3, 0.7, 0.8, 0.9],
    name='line'
)
trace2 = go.Bar(
    x=x,
    y=[1, 0.5, 0.7, -1.2, 0.3, 0.4],
    name = 'bar'
)

data = [trace1, trace2]

layout = dict(title = 'Bar-Line Demo')

fig = dict(data=data,layout=layout)


pyplt(data, filename='tmp/bar-line.html', show_link=False)