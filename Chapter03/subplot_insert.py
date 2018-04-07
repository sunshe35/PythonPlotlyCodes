import plotly as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 3, 2]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[30, 40, 50],
    xaxis='x2',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    xaxis2=dict(
        domain=[0.6, 0.95],
        anchor='y2'
    ),
    yaxis2=dict(
        domain=[0.6, 0.95],
        anchor='x2'
    )
)
fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename='tmp/subplot_insert.html')