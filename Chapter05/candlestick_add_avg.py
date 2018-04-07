import plotly as py  # 导入plotly库并命名为py
import plotly.graph_objs as go
import pandas as pd

fig = go.Figure()

# -------------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])
df['avg_5'] = df['close'].rolling(5).mean()

# K线图
trace = go.Candlestick(
    x=df.index,
    open=df.open,
    high=df.high,
    low=df.low,
    close=df.close,
)


# 5日均线拟合直线
add_line = go.Scatter(
         x=df.index,
         y=df.avg_5,
         name= '5日均线',
         line=dict(color='black')
    )

fig['data'] = [trace]
fig['data'].extend([add_line])

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

pyplt(fig, filename=r'tmp/candlestick_add_svg.html')
