import plotly as py
import plotly.graph_objs as go


# ----------pre def
pyplt = py.offline.plot


trace0 = go.Scatter(
    x=[1.5, 4,1.5,4],
    y=[3.75, 3.75,2.2,2.2],
    text=['矩形', '矩形（填充）','矩形（相对于plot+填充）','矩形（相对于轴+填充）'],
    mode='text',
)
data = [trace0]
layout = {
    'xaxis': {
        'range': [0, 8],
        'showgrid': False,
    },
    'yaxis': {
        'range': [0, 6.5]
    },
    'shapes': [
        # 普通的矩形
        {
            'type': 'rect',
            'x0': 1,
            'y0': 4,
            'x1': 2,
            'y1': 6,
            'line': {
                'color': 'rgba(128, 0, 128, 1)',
            },
        },
        # 填充颜色的矩形
        {
            'type': 'rect',
            'x0': 3,
            'y0': 4,
            'x1': 5,
            'y1': 6,
            'line': {
                'color': 'rgba(128, 0, 128, 1)',
                'width': 2,
            },
            'fillcolor': 'rgba(128, 0, 128, 0.7)',
        },
        # 相对于plot的矩形 + 填充颜色
        {
            'type': 'rect',
            'xref': 'paper',
            'yref': 'paper',
            'x0': 0.125,
            'y0': 0,
            'x1': 0.25,
            'y1': 0.3,
            'line': {
                'color': 'rgb(50, 171, 96)',
                'width': 3,
            },
            'fillcolor': 'rgba(50, 171, 96, 0.6)',
        },
        # 相对于轴的矩形 + 填充颜色
        {
            'type': 'rect',
            'xref': 'x',
            'yref': 'y',
            'x0': 3,
            'y0': 0,
            'x1': 5,
            'y1': 2,
            'line': {
                'color': 'rgb(55, 128, 191)',
                'width': 3,
            },
            'fillcolor': 'rgba(55, 128, 191, 0.6)',
        },

    ]
}
fig = {
    'data': data,
    'layout': layout,
}
pyplt(fig, filename='tmp/SVG_rectangle.html')