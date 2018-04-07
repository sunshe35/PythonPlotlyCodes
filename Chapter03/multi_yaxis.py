import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[40, 50, 60],
    name='yaxis 数据'
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[4, 5, 6],
    name='yaxis2 数据',
    yaxis='y2'
)
data = [trace1, trace2]
layout = go.Layout(
    title='Y轴双轴示例',
    yaxis=dict(
        title='yaxis 标题'
    ),
    yaxis2=dict(
        title='yaxis2 标题',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)
fig = go.Figure(data=data, layout=layout)
plot_url = pyplt(fig, filename='tmp/multi_yaxis.html')
