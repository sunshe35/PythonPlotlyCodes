# 3.2 SVR
import plotly as py
import plotly.graph_objs as go
import numpy as np
from sklearn.svm import SVR

pyplt = py.offline.plot

X = np.sort(5 * np.random.rand(40, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - np.random.rand(8))

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
svr_lin = SVR(kernel='linear', C=1e3)
svr_poly = SVR(kernel='poly', C=1e3, degree=2)

y_rbf = svr_rbf.fit(X, y).predict(X)
y_lin = svr_lin.fit(X, y).predict(X)
y_poly = svr_poly.fit(X, y).predict(X)


def data_to_plotly(x):
    k = []
    
    for i in range(0, len(x)):
        k.append(x[i][0])
        
    return k

lw = 2
p1 = go.Scatter(x=data_to_plotly(X), y=y,
                mode='markers',
                marker=dict(color='darkorange'),
                name='data')

p2 = go.Scatter(x=data_to_plotly(X), y=y_rbf, 
                mode='lines',
                line=dict(color='navy', width=lw),
                name='RBF model')

p3 = go.Scatter(x=data_to_plotly(X), y=y_lin, 
                mode='lines',
                line=dict(color='cyan', width=lw),
                name='Linear model')

p4 = go.Scatter(x=data_to_plotly(X), y=y_poly, 
                mode='lines', 
                line=dict(color='cornflowerblue', width=lw),
                name='Polynomial model')

layout = go.Layout(title='Support Vector Regression',
                   hovermode='closest',
                   xaxis=dict(title='data'),
                   yaxis=dict(title='target'))

fig = go.Figure(data=[p1, p2, p3, p4], layout=layout)
pyplt(fig, filename = r'tmp\SVR.html')