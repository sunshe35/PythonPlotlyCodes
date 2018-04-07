# 2.6-5 应用案例
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

# Customizing Individual Bar Colors
volume = [0.49,0.71,1.43,1.4,0.93]
width = [each*3/sum(volume) for each in volume]
trace0 = go.Bar(
    x = ['AU.SHF', 'AG.SHF', 'SN.SHF',
       'PB.SHF', 'CU.SHF'],
    y = [0.85, 0.13, -0.93, 0.46, 0.06],
    width = width,
    marker = dict(
        color=['rgb(205,38,38)', 'rgb(205,38,38)',
               'rgb(34,139,34)', 'rgb(205,38,38)',
               'rgb(205,38,38)'],
        line=dict(
            color='rgb(0,0,0)',
            width=1.5,
        )),
        opacity = 0.8,
)

data = [trace0]
layout = go.Layout(
    title = '有色金属板块主力合约日内最高涨幅与波动率图',
    xaxis=dict(tickangle=-45),
)

fig = go.Figure(data=data, layout=layout)
pyplt(fig, filename='tmp/highlight-bar.html')