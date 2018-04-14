# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:52:42 2017

@author: Administrator
"""

import numpy as np#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py
# -------------pre def
pympl = py.offline.plot_mpl
# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

np.random.seed(19680801)
#产生随机种子
n_bins = 10
x = np.random.randn(1000, 3)
#产生1000*3的矩阵
fig, axes = plt.subplots(nrows=2, ncols=2)
ax0, ax1, ax2, ax3 = axes.flatten()

colors = ['red', 'tan', 'lime']
#设置颜色
ax0.hist(x, n_bins, normed=1, histtype='bar', color=colors, label=colors)
#设置柱状图的信息
ax0.legend(prop={'size': 10})
ax0.set_title('图例bar')
#添加标题
ax1.hist(x, n_bins, normed=1, histtype='bar', stacked=True)
#设置柱状图的信息

ax1.set_title('堆积bar')
#添加标题
ax2.hist(x, n_bins, normed=1, histtype='bar', stacked=True, fill=False)
#设置柱状图信息
ax2.set_title('堆积bar（非填充）')
#添加标题
x_multi = [np.random.randn(n) for n in [10000, 5000, 2000]]
ax3.hist(x_multi, n_bins, histtype='bar')
#设置柱状图信息
ax3.set_title('不同样本容量')
#添加标题
fig.tight_layout()
#使图形紧凑
fig1= plt.gcf()
plot_url = pympl(fig1,filename=r'tmp/bar_2.html', show_link=False,resize=True)