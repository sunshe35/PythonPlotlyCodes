# 2.11-1 Basic Pie Chart
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
labels = ['股票','债券','现金','衍生品','其它']
values = [33.7,20.33,9.9,8.6,27.47]
trace = [go.Pie(labels=labels, values=values)]
layout = go.Layout(
    title = '基金资产配置比例图',
)
fig = go.Figure(data = trace, layout = layout)
pyplt(fig, filename='tmp/basic_pie_chart.html')
