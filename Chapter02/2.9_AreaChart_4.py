# 2.9-4 应用案例
# Stacked Area Chart with Original Values
import plotly as py
import plotly.graph_objs as go
import numpy as np

pyplt = py.offline.plot
# Add original data
x=['Winter', 'Spring', 'Summer', 'Fall']

y0_org=[40, 60, 40, 10]
y1_org=[20, 10, 10, 60]
y2_org=[40, 30, 50, 30]

# Add data to create cumulative stacked values
y0_stck=y0_org
y1_stck=[y0+y1 for y0, y1 in zip(y0_org, y1_org)]
y2_stck=[y0+y1+y2 for y0, y1, y2 in zip(y0_org, y1_org, y2_org)]

# Make original values strings and add % for hover text
y0_txt=[str(y0)+'%' for y0 in y0_org]
y1_txt=[str(y1)+'%' for y1 in y1_org]
y2_txt=[str(y2)+'%' for y2 in y2_org]

trace0 = go.Scatter(
    x=x,
    y=y0_stck,
    text=y0_txt,
    hoverinfo='x+text',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(131, 90, 241)'),
    fill='tonexty'
)
trace1 = go.Scatter(
    x=x,
    y=y1_stck,
    text=y1_txt,
    hoverinfo='x+text',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(111, 231, 219)'),
    fill='tonexty'
)
trace2 = go.Scatter(
    x=x,
    y=y2_stck,
    text=y2_txt,
    hoverinfo='x+text',
    mode='lines',
    line=dict(width=0.5,
              color='rgb(184, 247, 212)'),
    fill='tonexty'
)
data = [trace0, trace1, trace2]

fig = go.Figure(data=data)
pyplt(fig, filename='tmp/stacked-area-plot-hover.html')