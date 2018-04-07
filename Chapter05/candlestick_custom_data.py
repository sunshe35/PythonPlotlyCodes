import plotly as py
import plotly.graph_objs as go
from datetime import datetime


# -------------pre def
pyplt = py.offline.plot

# 添加数据
open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2016, month=10, day=10),
         datetime(year=2016, month=11, day=10),
         datetime(year=2016, month=12, day=10),
         datetime(year=2017, month=1, day=10),
         datetime(year=2017, month=2, day=10)]


# 创建ohlc
trace = go.Candlestick(x=dates,
                open=open_data,
                high=high_data,
                low=low_data,
                close=close_data)

data = [trace]

pyplt(data, filename=r'tmp/candlestick_custom_data.html')
