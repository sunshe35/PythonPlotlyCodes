# 2.11-3 Styled Pie Chart
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot
labels = ['上海国际集团有限公司', '中国移动通信集团',\
 '富德生命人寿-传统', '富德生命人寿-资本金', '上海上国投资产管理有限公司']
values = [4222533311, 4103763711, 2138028672, 1356332558, 1073516173]
colors = ['#104E8B', '#1874CD', '#1C86EE', '#6495ED']

trace = [go.Pie(labels = labels, 
                values = values,
                rotation = 30,
                opacity = 1,
                showlegend = False,
                pull = [0.1,0,0,0,0],
                hoverinfo = 'label+percent', 
                textinfo = 'percent', # textinfo = 'value',
                textfont = dict(size = 30, color = 'white'),
                marker = dict(colors = colors, 
                    line = dict(color = '#000000', width = 2)))]
fig = go.Figure(data = trace)
pyplt(trace, filename='tmp/styled_pie_chart.html')
