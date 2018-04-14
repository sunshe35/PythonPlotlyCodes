# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:49:20 2017

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

plt.figure(figsize=(7,5))

X = np.arange(1,6)
#X是1,2,3,4,5,6,7,8,柱的个数
# numpy.random.uniform(low=0.0, high=1.0, size=None), normal
#uniform均匀分布的随机数，normal是正态分布的随机数，0.5-1均匀分布的数，一共有n个
Y1 = np.random.uniform(0.5,1.0,5)
Y2 = np.random.uniform(0.5,1.0,5)
plt.bar(X,Y1,width = 0.35,facecolor = 'lightskyblue',edgecolor = 'white')
#width:柱的宽度
plt.bar(X+0.35,Y2,width = 0.20,facecolor = 'yellowgreen',edgecolor = 'white')
#水平柱状图plt.barh，属性中宽度width变成了高度height
#打两组数据时用+
#facecolor柱状图里填充的颜色
#edgecolor是边框的颜色
#想把一组数据打到下边，在数据前使用负号
fig = plt.gcf()
plot_url = pympl(fig,filename=r'tmp/bar_1.html', show_link=False,resize=True)