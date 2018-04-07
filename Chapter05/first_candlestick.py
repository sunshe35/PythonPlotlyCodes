import plotly as py  # 导入plotly库并命名为py
import plotly.graph_objs as go

# -------------pre def
pyplt = py.offline.plot
import pandas as pd


df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])


trace = go.Candlestick(
    x=df.index,
    open=df.open,
    high=df.high,
    low=df.low,
    close=df.close,
)


data = [trace]

pyplt(data, filename=r'tmp/first_candlestick.html')

