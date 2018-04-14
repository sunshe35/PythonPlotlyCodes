# -*- coding: utf-8 -*-
# 2.6.1 基本示例
import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot

# Trace
trace_basic = [go.Bar(
            x = ['Variable_1', 'Variable_2', 'Variable_3','Variable_4','Variable_5'],
            y = [1, 2, 3, 2, 4],
    )]

# Layout
layout_basic = go.Layout(
            title = 'The Graph Title',
            xaxis = go.XAxis(range = [-0.5,4.5], domain = [0,1])
    )

# Figure
figure_basic = go.Figure(data = trace_basic, layout = layout_basic)

# Plot
pyplt(figure_basic, filename='tmp/Basic_BarChart.html')