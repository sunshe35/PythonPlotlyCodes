import plotly as py
import plotly.graph_objs as go

# ----------pre def
pyplt = py.offline.plot

# ----------code
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    text=['A</br>size: 40</br>default', 'B</br>size: 60</br>default', 'C</br>size: 80</br>default', 'D</br>size: 100</br>default'],
    mode='markers',
    name='default',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizemode='area',
    )
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[14, 15, 16, 17],
    text=['A</br>size: 40</br>sizeref: 0.2', 'B</br>size: 60</br>sizeref: 0.2', 'C</br>size: 80</br>sizeref: 0.2', 'D</br>size: 100</br>sizeref: 0.2'],
    mode='markers',
    name = 'ref0.2',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizeref=0.2,
        sizemode='area',
    )
)
trace2 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[20, 21, 22, 23],
    text=['A</br>size: 40</br>sizeref: 2', 'B</br>size: 60</br>sizeref: 2', 'C</br>size: 80</br>sizeref: 2', 'D</br>size: 100</br>sizeref: 2'],
    mode='markers',
    name='ref2',
    marker=dict(
        size=[400, 600, 800, 1000],
        sizeref=2,
        sizemode='area',
    )
)

data = [trace0, trace1, trace2]
pyplt(data, filename='tmp/bubble_scale.html')