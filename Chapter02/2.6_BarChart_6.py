# -*- coding: utf-8 -*-
# 2.6-6 应用案例
import plotly as py
import plotly.graph_objs as go

pd.set_option('display.width', 450)
pyplt=py.offline.plot
df=pd.read_csv('dat/tk01_m15.csv')
df2= df[:10]
xtr = go.Bar(
    x=df2['time'],
    y=df2['volume'],
    
)
xdat = go.Data([xtr])
layout = go.Layout(
    title = '成交量volume--15分钟分时数据',
    xaxis = go.XAxis(tickangle=-15),
)
fig = go.Figure(data=xdat, layout=layout)
pyplt(fig, filename='tmp/barchart_apply.html')
