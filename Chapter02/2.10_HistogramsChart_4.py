# # 2.10-4 Cumulative Histogram
import plotly as py
import plotly.graph_objs as go
import numpy as np
pyplt = py.offline.plot

s1 = np.random.RandomState(1)
x1 = s1.randn(1000)
trace1 = [go.Histogram(
    x=x1,
    cumulative=dict(enabled=True)
)]
pyplt(trace1, filename='tmp/cumulative_histogram.html')
