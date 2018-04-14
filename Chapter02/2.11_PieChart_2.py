# 2.11-2 Basic Pie Chart
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
labels = ['完成','未完成']
values = [0.7,0.3]
trace = [go.Pie(
    labels = labels, 
    values = values, 
    hole =  0.7,
    hoverinfo = "label + percent")]
layout = go.Layout(
    title = '工作进度图'
)
fig = go.Figure(data = trace, layout = layout)
pyplt(fig, filename='tmp/basic_pie_chart.html')
