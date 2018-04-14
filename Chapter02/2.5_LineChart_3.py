# 2.5-3 应用案例
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
trace1 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 3, 2, 3, 1],
    mode='lines+markers',
    name="'linear'",
    hoverinfo='name',
    line=dict(
        shape='linear'
    )
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[6, 8, 7, 8, 6],
    mode='lines+markers',
    name="'spline'",
    text=["tweak line smoothness<br>with 'smoothing' in line object"],
    hoverinfo='text+name',
    line=dict(
        shape='spline'
    )
)
trace3 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[11, 13, 12, 13, 11],
    mode='lines+markers',
    name="'vhv'",
    hoverinfo='name',
    line=dict(
        shape='vhv'
    )
)
trace4 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[16, 18, 17, 18, 16],
    mode='lines+markers',
    name="'hvh'",
    hoverinfo='name',
    line=dict(
        shape='hvh'
    )
)
trace5 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[21, 23, 22, 23, 21],
    mode='lines+markers',
    name="'vh'",
    hoverinfo='name',
    line=dict(
        shape='vh'
    )
)
trace6 = go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[26, 28, 27, 28, 26],
    mode='lines+markers',
    name="'hv'",
    hoverinfo='name',
    line=dict(
        shape='hv'
    )
)
data = [trace1, trace2, trace3, trace4, trace5, trace6]
layout = dict(
    legend=dict(
        y=0.5,
        traceorder='reversed',
        font=dict(
            size=16
        )
    )
)
fig = dict(data=data, layout=layout)
pyplt(fig, filename='tmp/line-shapes.html')
