import plotly as py  # 导入plotly库并命名为py
import plotly.graph_objs as go
import pandas as pd

fig = go.Figure()

# -------------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])

trace = go.Ohlc(
    x=df.index,
    open=df.open,
    high=df.high,
    low=df.low,
    close=df.close,
)

fig['data'] = [trace]

fig['layout'].update(
    xaxis=go.XAxis(
        autorange=True,
        mirror='all',
        gridcolor='rgb(180, 180, 180)',
        showline=True,  # 画出 X 轴那条线
        showgrid=True,
        tickangle=-60,
        categoryorder="category ascending",
        type='category'),
    yaxis=go.YAxis(
        autorange=True,
        gridcolor='rgb(180, 180, 180)',
    ),
)

pyplt(fig, filename=r'tmp/ohlc_filter_time.html')
