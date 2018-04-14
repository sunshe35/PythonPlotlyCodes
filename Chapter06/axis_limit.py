# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:56:33 2017

@author: Administrator
"""
from pylab import *
import numpy as np#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py
# -------------pre def
pympl = py.offline.plot_mpl

# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

x = np.arange(-5.0, 5.0, 0.02)
# x = np.linspace(-5, 5, num=50, endpoint=True, retstep=False, dtype=None)
y1 = x**2+1
plt.figure(1)
plt.subplot(211)
xlabel('x 值')
ylabel('y1 值')
#设置x轴范围，x轴只显示（-5,3），总区间（-5,5)
xlim(-5, 3)
#设置y轴范围
ylim(-10, 50)
plt.plot(x,y1)
fig= plt.gcf()
plot_url = pympl(fig,filename=r'tmp/axis_limit.html', show_link=False,resize=True)