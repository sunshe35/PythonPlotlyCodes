import plotly as py  # 导入plotly库并命名为py
import pandas as pd

# -------------pre def
pyplt = py.offline.plot

df_50 = pd.read_csv(r'dat/000016.csv', index_col=['date']) # 读取数据
df_50.sort_index(inplace=True) # 排序
df_50 = df_50.loc['2017-01-03':,:]
df_300 = pd.read_csv(r'dat/000300.csv', index_col=['date'])
df_300.sort_index(inplace=True) # 排序
df_300 = df_300.loc['2017-01-01':]

fig = {
    'data': [
        {
            'x': df_50.index,
            'y': df_50.volume,
            'mode': 'markers',
            'name': '上证50'},
        {
            'x': df_300.index,
            'y': df_300.volume,
            'mode': 'markers',
            'name': '沪深300'}
    ],
    'layout': {
        'xaxis': {'title': '时间',
                  # 'type': 'log',
                  },
        'yaxis': {'title': "成交量"}
    }
}

url = pyplt(fig, filename='tmp/basic_scatter.html')
