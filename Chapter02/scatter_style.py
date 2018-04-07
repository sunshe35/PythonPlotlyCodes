import plotly as py
import plotly.graph_objs as go

import numpy as np

# ----------pre def
pyplt = py.offline.plot

# ----------code
N = 500
x = np.random.randn(N)

trace0 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N)+2,
    name = 'Above',
    mode = 'markers+lines',
    marker = dict(
        size = 10, # 设置点的宽度
        color = 'rgba(152, 0, 0, .8)', # 设置曲线的颜色
        line = dict(
            width = 2, # 设置线条的宽度
            color = 'rgb(0, 0, 0)' # 设置线条的颜色
        )
    )
)


trace1 = go.Scatter(
    x = np.random.randn(N),
    y = np.random.randn(N) - 2,
    name = 'Below',
    mode = 'markers',
    marker = dict(
        size = 10,
        color = 'rgba(255, 182, 193, .9)',
        line = dict(
            width = 2,
        )
    )
)

data = [trace0, trace1]

layout = dict(title = 'Styled Scatter',
              yaxis = dict(zeroline = True), # 显示y轴的0刻度线
              xaxis = dict(zeroline = False) # 不显示x轴的0刻度线
             )

fig = dict(data=data, layout=layout)
pyplt(fig, filename='tmp/scatter_style.html')
