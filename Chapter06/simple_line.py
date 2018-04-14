# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 11:39:15 2017

@author: Administrator
"""

import matplotlib.pyplot as plt
#使用import导入模块matplotlib.pyplot，并简写成plt
import numpy as np
#使用import导入模块numpy，并简写成np
import plotly as py  # 导入plotly库并命名为py

# -------------pre def
pympl = py.offline.plot_mpl

# 配置中文显示
plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

fig, ax = plt.subplots()
x = np.linspace(1,10)
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 参数解释：start,stop是开始，结束的数字，num是生成多少个数字，默认50个；endpoint是最后一个stop数字是否包含进去，默认包含；retstep,是两个数字间的间距，默认不显示；dtype默认。
y = x*3 + 5
#线性方程y= x*3 + 5
plt.title("线性函数")
#设置标题
plt.xlabel("x 值")
#设置x轴标签
plt.ylabel("y 值")
#设置y轴标签
ax.plot(x, y)
#画图




plot_url = pympl(fig,filename=r'tmp/simple_line.html', show_link=False,resize=True)