# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:59:48 2017

@author: Administrator
"""
import matplotlib.mlab as mlab#使用import导入模块matplotlib.mlab
import numpy as np#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py
# -------------pre def
pympl = py.offline.plot_mpl


# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

#正太分布函数等和其他函数都在matplotlib.mlab库里面
np.random.seed(19680801)
#产生随机种子
mu = 100
sigma = 15
x = mu + sigma * np.random.randn(437)
#生产数据
num_bins = 50
fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, normed=1)
#产生直方图

y = mlab.normpdf(bins, mu, sigma)
#normpdf：正态概率密度函数
#Y = normpdf(X,mu,sigma)
#mu：均值
#sigma：标准差
#Y：正态概率密度函数在x处的值
ax.plot(bins, y, '--')
#画图
ax.set_xlabel('X 轴')
#x轴标签
ax.set_ylabel('概率密度')
#y轴标签
ax.set_title(r'柱状图IQ: $\mu=100$, $\sigma=15$')
#设置标题
fig.tight_layout()
#产生紧凑的图片
plot_url = pympl(fig,filename=r'tmp/probability_density.html', show_link=False,resize=True)