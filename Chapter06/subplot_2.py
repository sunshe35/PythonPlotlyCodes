# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:20:04 2017

@author: Administrator
"""

import numpy as np#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py
# -------------pre def
pympl = py.offline.plot_mpl
# 配置中文显示
fig, ax = plt.subplots()
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def f(t):
    return np.cos(2*np.pi*t)
#产生f(t)函数
t1 = np.arange(0.0, 5.0, 0.5)
t2 = np.arange(0.0, 5.0, 0.01)
#产生t1，t2数据
plt.figure(1)
plt.subplot(211)
#添加子图
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#画图
plt.subplot(212)
#添加子图
plt.plot(np.cos(2*np.pi*t2), 'r--')

plot_url = pympl(fig,filename=r'tmp/subplot_2.html', show_link=False,resize=True)