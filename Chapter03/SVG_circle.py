import plotly as py
import plotly.graph_objs as go

# ----------pre def
pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1.5, 3.5],
    y=[0.75, 2.5],
    text=['无填充圆',
          '有填充圆'],
    mode='text',
)
data = [trace0]

layout = {
    'xaxis': {
        'range': [0, 4.5],
        'zeroline': False,
    },
    'yaxis': {
        'range': [0, 4.5]
    },
    'width': 800,
    'height': 800,
    'shapes': [
        # 无填充圆
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'x0': 1,
            'y0': 1,
            'x1': 3,
            'y1': 3,
            'line': {
                'color': 'rgba(50, 171, 96, 1)',
            },
        },
        # 有填充圆
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'rgba(50, 171, 96, 0.7)',
            'x0': 3,
            'y0': 3,
            'x1': 4,
            'y1': 4,
            'line': {
                'color': 'rgba(50, 171, 96, 1)',
            },
        },
    ]
}

fig = {
    'data': data,
    'layout': layout,
}
pyplt(fig, filename='tmp/SVG_circle.html')
