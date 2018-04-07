# 3.1 SVM
import plotly as py
import plotly.graph_objs as go
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets

pyplt = py.offline.plot
iris = datasets.load_iris()
X = iris.data[:, :2] # 只去前两个特征
Y = iris.target      # 分类标签
h = .02  # 设定网格大小
clf = svm.SVC(kernel='linear')
clf.fit(X, Y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
x_ = np.arange(x_min, x_max, h)
y_ =  np.arange(y_min, y_max, h)
xx, yy = np.meshgrid(x_, y_)
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()]) # xx.ravel() 返回连续扁平的数组

# Put the result into a color plot
Z = Z.reshape(xx.shape)

cmap = [['RGB(10,64,159)'],['RGB(5,159,126)'],['RGB(159,26,64)']]
# 画布
trace1 = go.Heatmap(x=x_, y=y_, z=Z,
                    colorscale=cmap,
                    showscale=False)

# 画点
trace2 = go.Scatter(x=X[:, 0], y=X[:, 1], 
                    mode='markers',
                    marker=dict(color=Y, 
                                colorscale=cmap, 
                                showscale=False,
                                line=dict(color='black', width=1)))

layout = go.Layout(title="3-Class classification using Support Vector Machine with linear kernel")
fig = go.Figure(data= [trace1, trace2], layout=layout)
pyplt(fig, filename = r'tmp\SVM_clustering.html')
