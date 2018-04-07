import plotly as py
import plotly.graph_objs as go
import pandas as pd

# ----------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat/day01.csv', index_col=['date'], parse_dates=['date']) # 读取数据。
df.sort_index(inplace=True) # 设置索引列从大到小排序
df = df.iloc[-300:-100] # 选取其中的200行数据

trace0 = go.Scatter(x=df.index, y=df['close'], mode='line', name='temperature')

data = [trace0]
layout = {
    # 我们通过创建矩形的方式来高亮某一个时间区间
    'shapes': [
        # 首先，我们高亮显示2月4日--->3月6日.
        {
            'type': 'rect',
            # x参考系使用绝对坐标系（相对于轴）
            'xref': 'x',
            # y参考系使用相对坐标系（相对于plot）
            'yref': 'paper',
            'x0': '2015-02-04',
            'y0': 0,
            'x1': '2015-03-06',
            'y1': 1,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        },
        # 其次，我们高亮显示区间5月20日--->6月22日.
        {
            'type': 'rect',
            'xref': 'x',
            'yref': 'paper',
            'x0': '2015-05-20',
            'y0': 0,
            'x1': '2015-06-22',
            'y1': 1,
            'fillcolor': '#d3d3d3',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        }
    ]
}

fig = {'data': data, 'layout': layout}
pyplt(fig, filename='tmp/timestamp_highlight.html')
