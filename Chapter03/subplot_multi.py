from plotly import tools
import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

trace1 = go.Scatter(x=[1, 2, 3],
                    y=[4, 5, 6],
                    mode='markers+text+lines',
                    text=['A', 'B', 'C'],
                    textposition='bottom'
                    )
trace2 = go.Scatter(x=[20, 30, 40],y=[50, 60, 70])
trace3 = go.Scatter(x=[300, 400, 500],
                    y=[600, 700, 800],
                    mode='markers+text+lines',
                    text=['D', 'E', 'F'],
                    textposition='bottom'
                    )
trace4 = go.Scatter(x=[4000, 5000, 6000], y=[7000, 8000, 9000])

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Plot 1', 'Plot 2',
                                                          'Plot 3', 'Plot 4'))

fig.append_trace(trace1, 1, 1)
fig.append_trace(trace2, 1, 2)
fig.append_trace(trace3, 2, 1)
fig.append_trace(trace4, 2, 2)

fig['layout'].update(height=600, width=1000, title='Multiple Subplots2')

pyplt(fig, filename='tmp/subplot_multi.html')
