import numpy as np
import pandas as pd

import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot


class Chart_Plot:
    def __init__(self):
        pass

    def bar_graph(self):
        # Data
        data_1 = go.Bar(
            x=["上海物贸", "广东明珠", "五矿发展"],
            y=[4.12, 5.32, 0.60],
            name="201609"
        )

        data_2 = go.Bar(
            x=["上海物贸", "广东明珠", "五矿发展"],
            y=[3.65, 6.14, 0.58],
            name="201612"
        )

        data_3 = go.Bar(
            x=["上海物贸", "广东明珠", "五矿发展"],
            y=[2.15, 1.35, 0.19],
            name="201703"
        )

        Data = [data_1, data_2, data_3]

        # Layout
        layout = go.Layout(
            title='国际贸易板块净资产收益率对比图'
        )

        # Figure
        figure = go.Figure(data=Data, layout=layout)

        div = pyplt(figure, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div

    def line_graph(self):
        #####################################
        #########      面积图          ######
        #####################################

        # 随机生成100个交易日的收益率
        s1 = np.random.RandomState(8)  # 定义局部种子
        s2 = np.random.RandomState(9)  # 定义局部种子
        rd1 = s1.rand(100) / 10 - 0.02
        rd2 = s2.rand(100) / 10 - 0.02

        # 设定初始资金
        initial1 = 100000
        initial2 = 100000
        total1 = []
        total2 = []
        for i in range(len(rd1)):
            initial1 = initial1 * rd1[i] + initial1
            initial2 = initial2 * rd2[i] + initial2
            total1.append(initial1)
            total2.append(initial2)

        trace1 = go.Scatter(
            y=total1,
            fill=None,
            mode='lines',  # 无边界线
            name="策略1"
        )
        trace2 = go.Scatter(
            y=total2,
            fill='tonexty',
            mode='lines',  # 无边界线
            name="策略2"
        )

        data = [trace1, trace2]

        layout = dict(title='策略净值曲线',
                      xaxis=dict(title='交易天数'),
                      yaxis=dict(title='净值'),
                      )
        fig = dict(data=data, layout=layout)

        div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div

    def pie_graph(self):
        #####################################
        #########      饼图         ######
        #####################################

        labels = ['股票', '债券', '现金', '衍生品', '其它']
        values = [33.7, 20.33, 9.9, 8.6, 27.47]
        trace = [go.Pie(labels=labels, values=values)]
        layout = go.Layout(
            title='基金资产配置比例图',
        )
        fig = go.Figure(data=trace, layout=layout)
        div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div

    def twoline_graph(self):
        #####################################
        #########      线条图         ######
        #####################################

        # 600000浦发银行20170301-20170428涨跌幅度数据，数据来源Wind
        profit_rate = [-0.001, -0.013, -0.004, 0.002, 0.003, -0.001, -0.009, 0.0, 0.007, -0.005, 0.0, 0.001, -0.006,
                       -0.006, -0.009, -0.013, 0.005, 0.007, 0.004, -0.006, -0.009, -0.004, 0.015, 0.007, 0.001, 0.003,
                       -0.009, -0.005, 0.001, -0.008, -0.016, 0.002, -0.013, -0.009, -0.014, 0.009, -0.003, 0.002,
                       -0.001, 0.011, 0.004]
        date = pd.bdate_range(start='3/1/2017', end='4/30/2017')
        trace = [go.Scatter(
            x=date,
            y=profit_rate
        )]
        layout = dict(
            title='浦发银行20170301-20170428涨跌幅变化',
            xaxis=dict(title='Date'),
            yaxis=dict(title='profit_rate')
        )

        fig = dict(data=trace, layout=layout)

        div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
        return div
