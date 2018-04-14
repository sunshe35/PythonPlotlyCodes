# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:10:23 2017

@author: Administrator
"""

import numpy as np#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py

# -------------pre def
pympl = py.offline.plot_mpl

fig, ax = plt.subplots()

# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


x1 = np.arange(0.0, 3.0, 0.01)
x2 = np.arange(0.0, 4.0, 0.01)
#产生x1，x2数据
y1 = np.cos(2 * np.pi * x1) * np.exp(-x1)
y2 = np.cos(2 * np.pi * x2)
#产生数据y1，y2
plt.subplot(2, 1, 1)
# pyplot通过调用subplot或者add_subplot来增加子图，如p1 = plt.subplot(211) 或者 p1 = plt.subplot(2,1,1)， 表示创建一个2行，1列的图，p1为第一个子图，然后在p1上画曲线，设置标注标题图例等，就可以使用p1来调用相关的函数，可以直接使用pyplot画图，添加label，等。
plt.plot(x1, y1)
plt.title('子图1')
#添加标题
plt.ylabel('y1 值')
#添加y轴名称
plt.subplot(2, 1, 2)
#添加子图
plt.plot(x2, y2)
plt.xlabel('数量')
#添加标签
plt.ylabel('y2 值')
#添加y轴名称
plot_url = pympl(fig,filename=r'tmp/subplot_1.html', show_link=False,resize=True)