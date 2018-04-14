# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:57:32 2017

@author: Administrator
"""

from numpy.random import rand#使用import导入模块numpy
import matplotlib.pyplot as plt#使用import导入模块matplotlib.pyplot
import plotly as py  # 导入plotly库并命名为py
# -------------pre def
pympl = py.offline.plot_mpl
# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig, ax = plt.subplots()
for color in ['red', 'green', 'blue']:
    n = 500
    x, y = rand(2, n)#产生2*n的矩阵
    ax.scatter(x, y, c=color, label=color,
               alpha=0.3, edgecolors='none')
#设置每个点的颜色，x,y分别代表的横纵坐标，通过横纵坐标确定点的位置，c表示点的颜色color，s表示点的大小size，alpha表示点的透明度，1是不透明，0是透明。
ax.legend()
ax.grid(True)
#设置网格
plot_url = pympl(fig,filename=r'tmp/scatter_2.html', show_link=False,resize=True)