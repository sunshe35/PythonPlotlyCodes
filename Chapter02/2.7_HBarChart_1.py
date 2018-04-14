# 2.7-1 基本示例
import plotly as py
import plotly.graph_objs as go
# Horizontal Bar Charts in Python
pyplt = py.offline.plot
data = [go.Bar(
            x=[29.41, 34.62, 30.16],
            y=['万科A', '国农科技', '世纪星源'],
            orientation = 'h'
)]
layout = go.Layout(
            title = '净资产收益率对比'
    )
figure = go.Figure(data = data, layout = layout)
pyplt(figure, filename='tmp/horizontal-bar.html')