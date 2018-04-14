# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 15:55:37 2017

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
fig, ax = plt.subplots()
#产生测试数据
x = np.arange(1,30)
y =np.sin(x)
ax1 = fig.add_subplot(111)
#设置标题
ax1.set_title('散点图')
#设置X轴标签
plt.xlabel('X')
#设置Y轴标签
plt.ylabel('Y')
#画散点图
lValue = x
ax1.scatter(x,y,c='r',s= 100,linewidths=lValue,marker='o')
#设置图标
plt.legend('x1')
plot_url = pympl(fig,filename=r'tmp/scatter_1.html', show_link=False,resize=True)