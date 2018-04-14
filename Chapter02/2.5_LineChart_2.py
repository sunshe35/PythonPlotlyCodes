# 2.5-2 应用案例
import plotly as py
import plotly.graph_objs as go

# Average High and Low Temperatures in New York
# Add data
pyplt = py.offline.plot
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December'] # x轴坐标
high_2000 = [32.5, 37.6, 49.9, 53.0, None, 75.4, 76.5, 76.6, 70.7, 60.6, 45.1, 29.3]
low_2000 = [13.8, 22.3, 32.5, 37.2, None, 56.1, 57.7, 58.3, 51.2, 42.8, 31.6, 15.9]
high_2007 = [36.5, 26.6, 43.6, 52.3, None, 81.4, 80.5, 82.2, 76.0, 67.3, 46.1, 35.0]
low_2007 = [23.6, 14.0, 27.0, 36.8, None, 57.7, 58.9, 61.2, 53.3, 48.5, 31.0, 23.6]
high_2014 = [28.8, 28.5, 37.0, 56.8, None, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9]
low_2014 = [12.7, 14.3, 18.6, 35.5, None, 58.0, 60.0, 58.6, 51.7, 45.2, 32.2, 29.1]
# 6组数据
# Create and style traces
trace0 = go.Scatter(
    x = month,
    y = high_2014,
    name = 'High 2014',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4),
    connectgaps = True
)
trace1 = go.Scatter(
    x = month,
    y = low_2014,
    name = 'Low 2014',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,),
    connectgaps = False
)
trace2 = go.Scatter(
    x = month,
    y = high_2007,
    name = 'High 2007',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dash'),
    connectgaps = False
)
# dash虚线（短线），dot虚线（点），dashdot （）
trace3 = go.Scatter(
    x = month,
    y = low_2007,
    name = 'Low 2007',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dash'),
    connectgaps = False
)
trace4 = go.Scatter(
    x = month,
    y = high_2000,
    name = 'High 2000',
    line = dict(
        color = ('rgb(205, 12, 24)'),
        width = 4,
        dash = 'dot'),
    connectgaps = False
)
trace5 = go.Scatter(
    x = month,
    y = low_2000,
    name = 'Low 2000',
    line = dict(
        color = ('rgb(22, 96, 167)'),
        width = 4,
        dash = 'dot'),
    connectgaps = False
)
data = [trace0, trace1, trace2, trace3, trace4, trace5]

# Edit the layout
layout = dict(title = 'Average High and Low Temperatures in New York',
              xaxis = dict(title = 'Month'),
              yaxis = dict(title = 'Temperature (degrees F)'),
              )

fig = dict(data=data, layout=layout)
pyplt(fig, filename='tmp/styled-line.html')
