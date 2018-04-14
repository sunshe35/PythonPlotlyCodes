# 2.7-2 应用案例
import plotly as py
import plotly.graph_objs as go
from plotly import tools
# Colored Horizontal Bar Chart
pyplt = py.offline.plot
trace1 = go.Bar(
    y = ['CU.SHF', 'AG.SHF', 'AU.SHF'],
    x = [21258, 30279, 8056],
    name = '中信期货',
    orientation = 'h',
    marker = dict(
        color = '#104E8B',
        line = dict(
            color = '#104E8B',
            width = 3)
    )
)
trace2 = go.Bar(
    y = ['CU.SHF', 'AG.SHF', 'AU.SHF'],
    x = [19853, 9375, 4063],
    name = '永安期货',
    orientation = 'h',
    marker = dict(
        color = '#1874CD',
        line = dict(
            color = '#104E8B',
            width = 3)
    )
)
trace3 = go.Bar(
    y = ['CU.SHF', 'AG.SHF', 'AU.SHF'],
    x = [4959, 13018, 8731],
    name = '海通期货',
    orientation = 'h',
    marker = dict(
        color = '#1C86EE',
        line = dict(
            color = '#104E8B',
            width = 3)
    )
)

data = [trace1, trace2,trace3]
layout = go.Layout(
    title = '贵金属期货持仓量对比图',
    barmode='stack'
)

fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename='tmp/marker-h-bar.html')