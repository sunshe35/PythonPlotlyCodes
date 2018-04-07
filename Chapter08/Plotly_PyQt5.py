# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 16:29:55 2017

@author: Administrator
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import Series
from pandas import DataFrame

import os
import plotly.offline as pyof
import plotly.graph_objs as go
from plotly import figure_factory as ff


class Plotly_PyQt5():
    def __init__(self):
        plotly_dir = 'plotly_html'
        if not os.path.isdir(plotly_dir):
            os.mkdir(plotly_dir)

        self.path_dir_plotly_html = os.getcwd() + os.sep + plotly_dir

        # path_plotly_four_line = os.getcwd() + os.sep + plotly_dir + os.sep + 'mpl_two_line.html'
        # pyof.plot_mpl(a, resize=True, auto_open=False, filename=path_plotly_four_line)

    def get_plotly_path_if_hs300_bais(self, file_name='if_hs300_bais.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        df = pd.read_excel(r'if_index_bais.xlsx')

        '''绘制散点图'''
        line_main_price = go.Scatter(
            x=df.index,
            y=df['main_price'],
            name='main_price',
            connectgaps=True,  # 这个参数表示允许连接数据缺口
        )

        line_hs300_close = go.Scatter(
            x=df.index,
            y=df['hs300_close'],
            name='hs300_close',
            connectgaps=True,
        )
        data = [line_hs300_close, line_main_price]

        layout = dict(title='if_hs300_bais',
                      xaxis=dict(title='Date'),
                      yaxis=dict(title='Price'),
                      )

        fig = go.Figure(data=data, layout=layout)
        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plot_path_matplotlib_plotly(self, file_name='matplotlib_plotly.html'):
        path_plotly = self.path_dir_plotly_html + os.sep + file_name

        N = 50
        x = np.random.rand(N)
        y = np.random.rand(N)
        colors = np.random.rand(N)
        area = np.pi * (15 * np.random.rand(N)) ** 2  # 0 to 15 point radii
        scatter_mpl_fig = plt.figure()
        plt.scatter(x, y, s=area, c=colors, alpha=0.5)

        pyof.plot_mpl(scatter_mpl_fig, filename=path_plotly, resize=True, auto_open=False)
        return path_plotly


    def get_plotly_path_monte_markovitz(self, file_name='monte_markovitz.html', monte_count=400, risk_free=0.03):
        """
        """
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        df = pd.read_excel(r'data\组合.xlsx', index_col=[0])
        returns = df.pct_change()
        returns.dropna(inplace=True)
        noa = 3

        # 蒙特卡洛随机模拟结果
        port_returns = []
        port_variance = []

        for p in range(monte_count):
            weights = np.random.random(noa)
            weights /= np.sum(weights)
            port_returns.append(np.sum(returns.mean() * 50 * weights))  # 加入模拟的均值
            port_variance.append(np.sqrt(np.dot(weights.T, np.dot(returns.cov() * 50, weights))))  # 加入模拟的标准差

        port_returns = np.array(port_returns)
        port_variance = np.array(port_variance)
        color_array = (port_returns - risk_free) / port_variance  # 夏普比，不同的夏普比对应的颜色是不同的。

        trace1 = go.Scatter(
            x=port_variance,
            y=port_returns,
            mode='markers',
            marker=dict(
                size='6',
                color=color_array,  # 通过一个可变的变量表示颜色，结果是绘图颜色可变。
                colorscale='Viridis',
                # 设置colorbar
                colorbar=dict(
                    tickmode='linear',
                    tick0=color_array.min(),
                    dtick=(color_array.max() - color_array.min()) / 5,
                ),
                showscale=True,
            )
        )
        data = [trace1]

        pyof.plot(data, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_table(self, file_name='产品组合信息表.html', df=None, w=None):
        '''画产品组合信息表
        df为dataframe，末尾一列为组合。
        w为权重
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name
        risk_free = 0.03
        std_year = df.std() * 50
        mean_year = df.pct_change().mean() * 50 - risk_free
        sharp_year = mean_year / std_year
        max_drawback = (df / df.cummax()).min()

        _temp = {i[0]: i[1] for i in zip(['风险', '均值', '夏普比', '最大回撤'], [std_year, mean_year, sharp_year, max_drawback])}
        df_info = pd.concat(_temp, axis=1).T
        df_info.index.name = '指标'
        df_info = df_info.round(decimals=3)
        table = ff.create_table(df_info, index=True, index_title='指标')

        pyof.plot(table, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_pie(self, file_name='产品组合成分饼图.html', df=None, w=None):
        '''
        画产品组合成分饼图
        df为dataframe，末尾一列为组合。
        w为权重
        :return:
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name

        labels = df.columns[:-1]
        values = w
        trace = go.Pie(labels=labels, values=values, text='哈哈')
        layout = dict(title='产品组合成分图')
        fig = dict(data=[trace], layout=layout)

        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly

    def get_plotly_path_combination_versus(self, file_name='产品组合VS沪深300.html', df=None, df_base=None, w=None):
        '''
        画产品组合VS沪深300
        df为dataframe，末尾一列为组合。
        w为权重
        :return:
        '''
        path_plotly = self.path_dir_plotly_html + os.sep + file_name

        df_contra = pd.concat([df_base.close, df['组合']], axis=1, join='inner')
        df_contra = df_contra / df_contra.iloc[0, :]
        df_contra.rename(columns={'close': '沪深300'}, inplace=True)

        trace1 = go.Scatter(x=df_contra.index, y=df_contra.iloc[:, 0], mode='lines+markers',
                            name='沪深300', marker=dict(color='blue'))
        trace2 = go.Scatter(x=df_contra.index, y=df_contra.iloc[:, 1], mode='lines+markers',
                            name='产品组合', marker=dict(color='red'))
        data = [trace1, trace2]
        layout = {'title': '产品组合VS沪深300'}
        fig = dict(data=data, layout=layout)

        pyof.plot(fig, filename=path_plotly, auto_open=False)
        return path_plotly
