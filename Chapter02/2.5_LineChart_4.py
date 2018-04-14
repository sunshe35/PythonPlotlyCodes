# 2.5-4 应用案例
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x_rev = x[::-1]

# Line 1 002104恒宝股份20170518-20170602
y1 = [8.86, 8.85, 8.69, 8.4, 8.62, 9, 8.99, 8.85, 8.59, 9.31]
y1_upper = [9.05, 9.03, 9.08, 8.76, 8.63, 9.04, 9.09, 9.16, 8.9, 9.45]
y1_lower = [8.86, 8.85, 8.64, 8.36, 8.33, 8.43, 8.93, 8.84, 8.53, 8.52]
y1_lower = y1_lower[::-1] # 逆序

# Line 2 002125湘潭电化20170518-20170602
y2 = [10.39, 10.35, 9.85, 9.73, 9.77, 9.8, 9.75, 9.65, 9.16, 9.34]
y2_upper = [10.58, 10.52, 10.34, 10.14, 9.87, 9.87, 9.94, 9.6, 9.42, 9.5]
y2_lower = [10.15, 10.21, 9.72, 9.68, 9.24, 9.48, 9.62, 9.12, 9.12, 9.34]
y2_lower = y2_lower[::-1]

# Line 3 002077大港股份20170518-20170602
y3 = [11.88, 13.07, 12.75, 12.02, 12.1, 12.61, 12.42, 12.42, 11.18, 10.72]
y3_upper = [11.98, 13.07, 13.4, 12.91, 12.45, 13.1, 12.61, 12.65, 12.45, 11.16]
y3_lower = [11.6, 11.75, 12.75, 12.02, 11.8, 11.92, 12.17, 12.29, 11.18, 10.35]
y3_lower = y3_lower[::-1]

trace1 = go.Scatter(
    x = x + x_rev,
    y = y1_upper + y1_lower,
    fill = 'tozerox',
    fillcolor = 'rgba(0,0,205,0.2)',
    line = go.Line(color = 'transparent'),
    showlegend = False,
    name = '恒宝股份',
)
trace2 = go.Scatter(
    x = x + x_rev,
    y = y2_upper + y2_lower,
    fill = 'tozerox',
    fillcolor = 'rgba(30,144,255,0.2)',
    line = go.Line(color = 'transparent'),
    name = '湘潭电化',
    showlegend = False,
)
trace3 = go.Scatter(
    x = x+x_rev,
    y = y3_upper+y3_lower,
    fill = 'tozerox',
    fillcolor = 'rgba(112,128,144,0.2)',
    line = go.Line(color = 'transparent'),
    showlegend = False,
    name = '大港股份',
)
trace4 = go.Scatter(
    x = x,
    y = y1,
    line = go.Line(color = 'rgb(0,0,205)'),
    mode = 'lines',
    name = '恒宝股份',
)
trace5 = go.Scatter(
    x = x,
    y = y2,
    line = go.Line(color='rgb(30,144,255)'),
    mode = 'lines',
    name = '湘潭电化',
)
trace6 = go.Scatter(
    x = x,
    y = y3,
    line = go.Line(color='rgb(112,128,144)'),
    mode = 'lines',
    name = '大港股份',
)

data = go.Data([trace1, trace2, trace3, trace4, trace5, trace6])

layout = go.Layout(
    paper_bgcolor = 'rgb(255,255,255)',
    plot_bgcolor = 'rgb(229,229,229)',
    xaxis = go.XAxis(
        gridcolor = 'rgb(255,255,255)',
        range = [1,10],
        showgrid = True,
        showline = False,
        showticklabels = True,
        tickcolor = 'rgb(127,127,127)',
        ticks = 'outside',
        zeroline = False
    ),
    yaxis = go.YAxis(
        gridcolor = 'rgb(255,255,255)',
        showgrid = True,
        showline = False,
        showticklabels = True,
        tickcolor = 'rgb(127,127,127)',
        ticks = 'outside',
        zeroline = False
    ),
)
fig = go.Figure(data = data, layout = layout)
pyplt(fig, filename = 'tmp/shaded_lines.html')
