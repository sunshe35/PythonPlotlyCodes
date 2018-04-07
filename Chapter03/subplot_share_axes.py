import plotly as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
    xaxis='x2',
    yaxis='y'
)
trace3 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
    xaxis='x',
    yaxis='y3'
)
trace4 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
    xaxis='x4',
    yaxis='y4'
)
data = [trace1, trace2, trace3, trace4]
layout = go.Layout(
    xaxis=dict(
        domain=[0, 0.45]
    ),
    yaxis=dict(
        domain=[0, 0.45]
    ),
    xaxis2=dict(
        domain=[0.55, 1]
    ),
    xaxis4=dict(
        domain=[0.55, 1],
        anchor='y4'
    ),
    yaxis3=dict(
        domain=[0.55, 1]
    ),
    yaxis4=dict(
        domain=[0.55, 1],
        anchor='x4'
    )
)
fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename='tmp/subplot_shared_axes.html')