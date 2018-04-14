# 2.5-1 基本示例
import plotly as py
import plotly.graph_objs as go

# Basic Line
pyplt = py.offline.plot
# 600000浦发银行20170301-20170428涨跌幅度数据，数据来源Wind
profit_rate = [-0.001, -0.013, -0.004, 0.002, 0.003, -0.001, -0.009, 0.0, 0.007,\
    -0.005, 0.0, 0.001, -0.006, -0.006, -0.009, -0.013, 0.005, 0.007,\
    0.004, -0.006, -0.009, -0.004, 0.015, 0.007, 0.001, 0.003, -0.009,\
    -0.005, 0.001, -0.008, -0.016, 0.002, -0.013, -0.009, -0.014, 0.009,\
    -0.003, 0.002, -0.001, 0.011, 0.004]
date = pd.bdate_range(start = '3/1/2017', end = '4/30/2017') 
trace = [go.Scatter(
    x = date,
    y = profit_rate
)]
layout = dict(
    title = '浦发银行20170301-20170428涨跌幅变化',
    xaxis = dict(title = 'Date'),
    yaxis = dict(title = 'profit_rate')
)

fig = dict(data = trace, layout = layout)
pyplt(fig, filename='tmp/basic-line.html')
