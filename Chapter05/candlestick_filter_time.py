import plotly as py  # 导入plotly库并命名为py
import plotly.graph_objs as go

fig = go.Figure()

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

fig['data'] = [trace]

fig['layout'] = dict(
    xaxis=dict(
        showline=True, # 画出 X 轴那条线
        tickangle=-60,

        categoryorder="category ascending",
        type='category')
)


pyplt(fig, filename=r'tmp/candlestick_filter_time.html')
