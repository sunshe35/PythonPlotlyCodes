# -*- coding: utf-8 -*-
# 2.6-3 应用案例
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

# Stacked Bar Chart
trace_1 = go.Bar(
    x = ['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合','华泰柏瑞'],
    y = [0.7252, 0.9912, 0.5347, 0.4436, 0.9911],
    name = '股票投资'
)

trace_2 = go.Bar(
    x = ['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合','华泰柏瑞'],
    y = [0.2072, 0, 0.4081, 0.4955, 0.02],
    name='其它投资'
)

trace_3 = go.Bar(
    x = ['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合','华泰柏瑞'],
    y = [0, 0, 0.037, 0, 0],
    name='债券投资'
)

trace_4 = go.Bar(
    x = ['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合','华泰柏瑞'],
    y = [0.0676, 0.0087, 0.0202, 0.0609, 0.0087],
    name='银行存款'
)

trace = [trace_1, trace_2, trace_3, trace_4]
layout = go.Layout(
    title = '基金资产配置比例图',
    barmode='stack'
)

fig = go.Figure(data = trace, layout = layout)
pyplt(fig, filename='tmp/stacked-bar.html')