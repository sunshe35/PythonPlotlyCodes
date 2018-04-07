from plotly import tools
import plotly as py
import plotly.graph_objs as go


pyplt = py.offline.plot

trace1 = go.Scatter(
    x=[1, 2, 3],
    y=[4, 5, 6]
)
trace2 = go.Scatter(
    x=[20, 30, 40],
    y=[50, 60, 70],
)

fig = tools.make_subplots(rows=2, cols=1)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 2, 1)

fig['layout'].update(height=600, width=600, title='i <3 subplots')
pyplt(fig, filename='tmp/subplot_simple.html')