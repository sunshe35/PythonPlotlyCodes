# -*- coding: utf-8 -*-
"""
She35 Editor
# 演示plotly使用的第一个示例
# 该代码是在线绘图，需要使用官方的username和api_key，本书提供的一个测试账号使用如下,这两行代码只需要运行一次即可：
import plotly 
plotly.tools.set_credentials_file(username='PlotlyBookTest', api_key='ECmqAy8kLE5Qk7h29trH')

"""
import plotly.plotly as py
from plotly.graph_objs import *

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.plot(data, filename = 'first_start')

