import plotly as py
import plotly.graph_objs as go

from datetime import datetime

# ----------pre def
pyplt = py.offline.plot

# ----------code
x_datetime = [datetime(year=2013, month=10, day=4),
              datetime(year=2013, month=11, day=5),
              datetime(year=2013, month=12, day=6)]
x_string = ['2013-10-04', '2013-11-05', '2013-12-06']

trace_datetime = go.Scatter(x=x_datetime, y=[1, 3, 6],name='trace_datetime')
trace_string = go.Scatter(x=x_string, y=[2, 4, 7],name='trace_string')
data = [trace_datetime, trace_string]
pyplt(data, filename='tmp/timeSeries.html')
