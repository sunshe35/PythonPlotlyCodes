from plotly import tools
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace0 = go.Scatter(
    x=[1, 2, 3],
    y=[2, 3, 4]
)
trace1 = go.Scatter(
    x=[20, 30, 40],
    y=[5, 5, 5],
)
trace2 = go.Scatter(
    x=[2, 3, 4],
    y=[600, 700, 800],
)
trace3 = go.Scatter(
    x=[4000, 5000, 6000],
    y=[7000, 8000, 9000],
)

fig = tools.make_subplots(rows=2, cols=2, shared_yaxes=True)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)

fig['layout'].update(height=600, width=600,
                     title='Multiple Subplots with Shared Y-Axes')
pyplt(fig, filename='tmp/subplot_share_yaxes.html')