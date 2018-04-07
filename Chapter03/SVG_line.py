
import plotly as py
import plotly.graph_objs as go

# ----------pre def
pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1.2, 3.5, 5,0.5,7],
    y=[1, 1.8, 1.2,0.5,0.6],
    text=['垂直线(破折号)', '水平线（点+破折号）', '对角线（点）','对角线（相对于plot）','对角线（相对于轴）'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 8]
    },
    'yaxis': {
        'range': [0, 2.5]
    },
    'shapes': [
        # 画垂直线
        {
            'type': 'line',
            'x0': 1,
            'y0': 0,
            'x1': 1,
            'y1': 2,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
                'dash':'dash',
            },
        },
        # 水平线
        {
            'type': 'line',
            'x0': 2,
            'y0': 2,
            'x1': 5,
            'y1': 2,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 4,
                'dash': 'dashdot',
            },
        },
        # 对角线
        {
            'type': 'line',
            'x0': 4,
            'y0': 0,
            'x1': 6,
            'y1': 2,
            'line': {
                'color': 'rgb(128, 0, 128)',
                'width': 4,
                'dash': 'dot',
            },
        },
        # 相对于轴绘图
        {
            'type': 'line',
            'xref': 'x',
            'yref': 'y',
            'x0': 4,
            'y0': 0,
            'x1': 8,
            'y1': 1,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
        },
        # 相对于plot绘图
        {
            'type': 'line',
            'xref': 'paper',
            'yref': 'paper',
            'x0': 0,
            'y0': 0,
            'x1': 0.5,
            'y1': 0.5,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 3,
            },
        },
    ]
}

fig = {
    'data': data,
    'layout': layout,
}

pyplt(fig, filename='tmp/SVG_line.html')