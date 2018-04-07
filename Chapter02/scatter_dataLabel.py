import plotly as py
import plotly.graph_objs as go
import random
import numpy as np
import pandas as pd

# ----------pre def
pyplt = py.offline.plot

# ----------code
l = []
y = []
data = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv")
# Setting colors for plot.
N = 53
c = ['hsl(' + str(h) + ',50%' + ',50%)' for h in np.linspace(0, 360, N)]

for i in range(int(N)):
    y.append((2000 + i))
    trace0 = go.Scatter(
        x=data['rank'],
        y=data['pop'] + (i * 1000000),
        mode='markers',
        marker=dict(size=14,
                    line=dict(width=1),
                    color=c[i], # 颜色映射表
                    opacity=0.3 # 透明度0.3
                    ),
        name=y[i], # 名字为200+i
        text=data['state'])  # The hover text goes here...
    l.append(trace0)

layout = go.Layout(
    title='Stats of USA States',
    hovermode='closest',
    xaxis=dict(
        title='Pop',
        ticklen=5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title='Rank',
        ticklen=5,
        gridwidth=2,
    ),
    showlegend=False
)
fig = go.Figure(data=l, layout=layout)
pyplt(fig, filename=r'tmp\scatter_dataLabel.html')
