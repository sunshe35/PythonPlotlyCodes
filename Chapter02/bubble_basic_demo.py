import plotly as py
import plotly.graph_objs as go

# ----------pre def
pyplt = py.offline.plot

# ----------code
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 11, 12, 13],
    mode='markers',
    marker=dict(
        size=[40, 60, 80, 100],
    )
)

data = [trace0]
pyplt(data, filename='tmp/bubble_baisc_demo.html')