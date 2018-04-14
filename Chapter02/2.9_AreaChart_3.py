# 2.9-3 应用案例
import plotly as py
import plotly.graph_objs as go
# Data
data_1 = go.Scatter(
    x = ['基金1', '基金2', '基金3', '基金4','基金5'],
    y = [32.52, 43.12, 43.47, 44.36, 33.11],
    name = '股票投资',
    mode = 'lines',
    line = dict(width=0.5,
              color = 'rgb(184, 247, 212)'),
    fill = 'tonexty'
)

data_2 = go.Scatter(
    x = ['基金1', '基金2', '基金3', '基金4','基金5'],
    y = [63.24, 54.33, 74.28, 63.91, 63.11],
    name = '其它投资',
    mode = 'lines',
    line = dict(width=0.5,
              color = 'rgb(111, 231, 219)'),
    fill = 'tonexty'
)

data_3 = go.Scatter(
    x = ['基金1', '基金2', '基金3', '基金4','基金5'],
    y = [83.24, 74.33, 93.91, 79.22, 83.11],
    name='债券投资',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(127, 166, 238)'),
    fill='tonexty'
)

data_4 = go.Scatter(
    x = ['基金1', '基金2', '基金3', '基金4','基金5'],
    y = [100, 100, 100, 100, 100],
    name='银行存款',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(131, 90, 241)'),
    fill='tonexty'
)

data = [data_1, data_2, data_3, data_4]

# Layout
layout = go.Layout(
    title = '基金资产配置比例图',
    showlegend = True,
    xaxis = dict(
        type = 'category',
    ),
    yaxis = dict(
        type = 'linear',
        range = [1, 100],
        dtick = 20,
        ticksuffix = '%'
    )
)

# Figure
fig = go.Figure(data = data, layout = layout)
pyplt(fig, filename = 'tmp/stacked-area-plot.html')