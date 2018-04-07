import pandas as pd
import plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os

# ----------pre def
pyplt = py.offline.plot
CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))


class ChartPlot:
    def __str__(self):
        pass

    def range_slide(self):
        # ----------code
        df = pd.read_csv(CURRENT_PATH + r'/dat/day01.csv', index_col=[0])

        trace = go.Scatter(x=df.index, y=df.high)

        data = [trace]
        layout = dict(
            title='时间序列的滑块与选择器',
            xaxis=dict(
                rangeselector=dict(
                    buttons=list([
                        dict(count=1,
                             label='1m',
                             step='month',
                             stepmode='backward'),
                        dict(count=6,
                             label='6m',
                             step='month',
                             stepmode='backward'),
                        dict(count=1,
                             label='YTD',  # 今天以来
                             step='year',
                             stepmode='todate'),
                        dict(count=1,
                             label='1y',
                             step='year',
                             stepmode='backward'),
                        dict(step='all')
                    ])
                ),
                rangeslider=dict(),
                type='date'
            )
        )
        fig = dict(data=data, layout=layout)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def basic_plot(self):
        N = 100
        random_x = np.linspace(0, 1, N)
        random_y0 = np.random.randn(N) + 5
        random_y1 = np.random.randn(N)
        random_y2 = np.random.randn(N) - 5

        # Create traces
        trace0 = go.Scatter(
            x=random_x,
            y=random_y0,
            mode='markers',  # 纯散点的绘图
            name='markers'  # 曲线名称
        )
        trace1 = go.Scatter(
            x=random_x,
            y=random_y1,
            mode='lines+markers',  # 散点+线的绘图
            name='lines+markers'
        )
        trace2 = go.Scatter(
            x=random_x,
            y=random_y2,
            mode='lines',  # 线的绘图
            name='lines'
        )

        data = [trace0, trace1, trace2]
        fig = dict(data=data)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def line_full(self):
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        x_rev = x[::-1]

        # Line 1 002104恒宝股份20170518-20170602
        y1 = [8.86, 8.85, 8.69, 8.4, 8.62, 9, 8.99, 8.85, 8.59, 9.31]
        y1_upper = [9.05, 9.03, 9.08, 8.76, 8.63, 9.04, 9.09, 9.16, 8.9, 9.45]
        y1_lower = [8.86, 8.85, 8.64, 8.36, 8.33, 8.43, 8.93, 8.84, 8.53, 8.52]
        y1_lower = y1_lower[::-1]  # 逆序

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
            x=x + x_rev,
            y=y1_upper + y1_lower,
            fill='tozerox',
            fillcolor='rgba(0,0,205,0.2)',
            line=go.Line(color='transparent'),
            showlegend=False,
            name='恒宝股份',
        )
        trace2 = go.Scatter(
            x=x + x_rev,
            y=y2_upper + y2_lower,
            fill='tozerox',
            fillcolor='rgba(30,144,255,0.2)',
            line=go.Line(color='transparent'),
            name='湘潭电化',
            showlegend=False,
        )
        trace3 = go.Scatter(
            x=x + x_rev,
            y=y3_upper + y3_lower,
            fill='tozerox',
            fillcolor='rgba(112,128,144,0.2)',
            line=go.Line(color='transparent'),
            showlegend=False,
            name='大港股份',
        )
        trace4 = go.Scatter(
            x=x,
            y=y1,
            line=go.Line(color='rgb(0,0,205)'),
            mode='lines',
            name='恒宝股份',
        )
        trace5 = go.Scatter(
            x=x,
            y=y2,
            line=go.Line(color='rgb(30,144,255)'),
            mode='lines',
            name='湘潭电化',
        )
        trace6 = go.Scatter(
            x=x,
            y=y3,
            line=go.Line(color='rgb(112,128,144)'),
            mode='lines',
            name='大港股份',
        )

        data = go.Data([trace1, trace2, trace3, trace4, trace5, trace6])

        layout = go.Layout(
            paper_bgcolor='rgb(255,255,255)',
            plot_bgcolor='rgb(229,229,229)',
            xaxis=go.XAxis(
                gridcolor='rgb(255,255,255)',
                range=[1, 10],
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
            yaxis=go.YAxis(
                gridcolor='rgb(255,255,255)',
                showgrid=True,
                showline=False,
                showticklabels=True,
                tickcolor='rgb(127,127,127)',
                ticks='outside',
                zeroline=False
            ),
        )
        fig = go.Figure(data=data, layout=layout)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def bar_chart(self):
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
        fig = go.Figure(data=Data, layout=layout)

        # Plot
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def bonus_chart(self):
        labels = ['完成', '未完成']
        values = [0.7, 0.3]
        trace = [go.Pie(
            labels=labels,
            values=values,
            hole=0.7,
            hoverinfo="label + percent")]
        layout = go.Layout(
            title='工作进度图'
        )
        fig = go.Figure(data=trace, layout=layout)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def pie_chart(self):
        labels = ['上海国际集团有限公司', '中国移动通信集团', '富德生命人寿-传统', '富德生命人寿-资本金', '上海上国投资产管理有限公司']
        values = [4222533311, 4103763711, 2138028672, 1356332558, 1073516173]
        colors = ['#104E8B', '#1874CD', '#1C86EE', '#6495ED']

        trace = [go.Pie(labels=labels,
                        values=values,
                        rotation=30,
                        opacity=1,
                        showlegend=False,
                        pull=[0.1, 0, 0, 0, 0],
                        hoverinfo='label+percent',
                        textinfo='percent',  # textinfo = 'value',
                        textfont=dict(size=30, color='white'),
                        marker=dict(colors=colors,
                                    line=dict(color='#000000', width=2)))]
        fig = go.Figure(data=trace)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def stacked_bar(self):
        # Data
        data_1 = go.Bar(
            x=['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合', '华泰柏瑞'],
            y=[0.7252, 0.9912, 0.5347, 0.4436, 0.9911],
            name='股票投资'
        )

        data_2 = go.Bar(
            x=['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合', '华泰柏瑞'],
            y=[0.2072, 0, 0.4081, 0.4955, 0.02],
            name='其它投资'
        )

        data_3 = go.Bar(
            x=['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合', '华泰柏瑞'],
            y=[0, 0, 0.037, 0, 0],
            name='债券投资'
        )

        data_4 = go.Bar(
            x=['华夏新经济混合', '华夏上证50', '嘉实新机遇混合', '南方消费活力混合', '华泰柏瑞'],
            y=[0.0676, 0.0087, 0.0202, 0.0609, 0.0087],
            name='银行存款'
        )

        data = [data_1, data_2, data_3, data_4]

        # Layout
        layout = go.Layout(
            title='基金资产配置比例图',
            barmode='stack'
        )
        # Figure
        fig = go.Figure(data=data, layout=layout)
        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div

    def horizontal_chart(self):
        trace1 = go.Bar(
            y=['CU.SHF', 'AG.SHF', 'AU.SHF'],
            x=[21258, 30279, 8056],
            name='中信期货',
            orientation='h',
            marker=dict(
                color='#104E8B',
                line=dict(
                    color='#104E8B',
                    width=3)
            )
        )
        trace2 = go.Bar(
            y=['CU.SHF', 'AG.SHF', 'AU.SHF'],
            x=[19853, 9375, 4063],
            name='永安期货',
            orientation='h',
            marker=dict(
                color='#1874CD',
                line=dict(
                    color='#104E8B',
                    width=3)
            )
        )
        trace3 = go.Bar(
            y=['CU.SHF', 'AG.SHF', 'AU.SHF'],
            x=[4959, 13018, 8731],
            name='海通期货',
            orientation='h',
            marker=dict(
                color='#1C86EE',
                line=dict(
                    color='#104E8B',
                    width=3)
            )
        )

        data = [trace1, trace2, trace3]
        layout = go.Layout(
            title='贵金属期货持仓量对比图',
            barmode='stack'
        )

        fig = go.Figure(data=data, layout=layout)

        div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
        return div
