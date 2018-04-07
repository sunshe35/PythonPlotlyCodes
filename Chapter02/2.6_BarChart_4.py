# -*- coding: utf-8 -*-
# 2.6-4 应用案例
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

x_data = ['流动负债', '非流动负债',
          '负债','所有者权益', '总资产']
y_data = [56000000, 65000000, 65000000, 81000000, 81000000]
text = ['57,999,848万元', '8,899,916万元', '66,899,764万元', '16,167,657万元', '83,067,421万元']

# Base
trace0 = go.Bar(
    x=x_data,
    y=[0, 57999848, 0, 66899764, 0],
    marker=dict(
        color='rgba(1,1,1, 0.0)',
    )
)
# Trace
trace1 = go.Bar(
    x=x_data,
    y=[57999848, 8899916, 66899764,16167657, 83067421],
    marker=dict(
        color='rgba(55, 128, 191, 0.7)',
        line=dict(
            color='rgba(55, 128, 191, 1.0)',
            width=2,
        )
    )
)

data = [trace0, trace1]
layout = go.Layout(
    title = '万科A资产负债结构图',
    barmode='stack',
    showlegend=False
)

annotations = []

for i in range(0, 5):
    annotations.append(dict(x=x_data[i], y=y_data[i], text=text[i],
                                  font=dict(family='Arial', size=14,
                                  color='rgba(245, 246, 249, 1)'),
                                  showarrow=False,))
    layout['annotations'] = annotations

fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename = 'tmp/waterfall-bar-profit.html')