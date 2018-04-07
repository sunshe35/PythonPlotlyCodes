
import plotly as py
import plotly.graph_objs as go
import pandas as pd

fig = go.Figure()

# -------------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])

trace = go.Candlestick(x=df.index,
                open=df.open,
                high=df.high,
                low=df.low,
                close=df.close,
                increasing=dict(line=dict(color='#FF0000')),
                decreasing=dict(line=dict(color='#0C05F9'))
                )
data = [trace]

fig['data'] = [trace]

fig['layout'] = {
    'xaxis': {
        'showline': True,  # 画出 X 轴那条线
        'tickangle': -60,
        'categoryorder': "category ascending",
        'type': 'category'},
    'title': '苹果公司K线图',
    'yaxis': {'title': '股票价格'},
    'shapes': [{
        'x0': '2016-08-22', 'x1': '2016-10-05',
        'y0': 0, 'y1': 1, 'xref': 'x', 'yref': 'paper',
        'line': {'color': 'rgb(30,30,30)', 'width': 2}
    }],
    'annotations': [{
        'x': '2016-09-12', 'y': 0.05, 'xref': 'x', 'yref': 'paper',
        'showarrow': True, 'xanchor': 'left',
        'text': '区间最低价'
    }]
}

pyplt(fig, filename=r'tmp/candlestick_style.html')
