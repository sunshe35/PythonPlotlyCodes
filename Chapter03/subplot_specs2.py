from plotly import tools
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace1 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,1)')
trace2 = go.Scatter(x=[1, 2], y=[1, 2], name='(1,2)')
trace3 = go.Scatter(x=[1, 2], y=[1, 2], name='(2,1)')
trace4 = go.Scatter(x=[1, 2], y=[1, 2], name='(3,1)')
trace5 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,1)')
trace6 = go.Scatter(x=[1, 2], y=[1, 2], name='(5,2)')

fig = tools.make_subplots(rows=5, cols=2,
                          specs=[[{}, {'rowspan': 2}],
                                 [{}, None],
                                 [{'rowspan': 2, 'colspan': 2}, None],
                                 [None, None],
                                 [{}, {}]],
                          print_grid=True)

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 5, 1)
fig.append_trace(trace6, 5, 2)

fig['layout'].update(height=600, width=1000, title='specs examples')
pyplt(fig, filename='tmp/subplot_specs2.html')