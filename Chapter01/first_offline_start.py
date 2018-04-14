import plotly as py
from plotly.graph_objs import Scatter, Layout, Data

trace0 = Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = Data([trace0, trace1])

py.offline.plot(data, filename = 'first_offline_start.html')

