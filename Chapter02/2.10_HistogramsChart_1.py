# 2.10-1 基本示例
import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot
s1 = np.random.RandomState(1)
x = s1.randn(1000)
data = [go.Histogram(x=x,
                       histnorm = 'probability')] 
# y = x 水平直方图，histnorm='probability' y轴显示概率，没有则显示数目
pyplt(data, filename='tmp/basic_histogram.html')
