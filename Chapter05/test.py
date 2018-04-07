# -*- coding: utf-8 -*-
'''

'''
import pandas as pd
import plotly as py
import plotly.graph_objs as pygo
from plotly.graph_objs import *
from plotly.graph_objs import Scatter, Layout, Figure
from plotly.tools import FigureFactory as pyff
#
import my_talib as mta

# import zpd_talib as zta
# ------------------
pd.set_option('display.width', 450)
pyplt = py.offline.plot
# ------------------------
df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])
df = df.sort_index()
df['ma5'] = mta.MA(df, 5, 'close')
df = df.tail(300)
# df=df.head(50);print(df.head())
# start_day = '2016-06-01'
# end_day = '2017-01-01'
# df = df.loc[start_day:end_day, :]
max_vol = max(df['volume'])
# print('max', max_vol)
#

# Make increasing candlesticks and customize their color and name
fig_increasing = pyff.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index,
                                         direction='increasing', name='AAPL',
                                         marker=Marker(color='#FF0000'),
                                         line=Line(color='#FF0000'))

# Make decreasing candlesticks and customize their color and name
fig_decreasing = pyff.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index,
                                         direction='decreasing',
                                         marker=Marker(color='0026FF'),
                                         line=Line(color='0026FF'))

# Initialize the figure
fig = fig_increasing

# Add decreasing data with .extend()
fig['data'].extend(fig_decreasing['data'])

# fig = pyff.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index, increasing=dict(line=dict(color='#FF0000')), decreasing=dict(line=dict(color='#00EE00')))


fig['layout'].update(title='15分钟分时数据与ma5均线、成交量',
                     xaxis=pygo.XAxis(
                         # autorange=True,
                         gridcolor='rgb(180, 180, 180)',
                         mirror='all',
                         showgrid=True,
                         showline=True,
                         # ticks='inside',
                         tickangle=-20,
                         # title='tick data',
                         # tickformat='%m-%d %H:%M',
                         # dtick=3,
                         categoryorder="category descending",
                         type='category',
                         # type='linear',
                         # categoryarray=df.index,
                     ),
                     yaxis=pygo.YAxis(
                         autorange=True,
                         gridcolor='rgb(180, 180, 180)',
                     ),
                     # yaxis2=pygo.YAxis(
                     #     side='right',
                     #     overlaying='y',
                     #     range=[0, max_vol * 5],
                     # ),
                     )

# xtr_ma5 = pygo.Scatter(
#     x=df.index,
#     y=df['ma5'],
#     name='ma5',
#     line=pygo.Line(color='rgb(148, 103, 189)', width=1.5, )
# )
#
# xtr_vol = pygo.Bar(
#     x=df.index,
#     y=df['volume'],
#     name='volume',
#     yaxis='y2',
#     opacity=0.6,
#     marker=dict(
#         color='rgb(158,202,225)',
#         line=dict(
#             color='rgb(8,48,107)',
#             width=1.5,
#         ), ),
# )
#

# fig['data'].extend([xtr_ma5, xtr_vol])
#

pyplt(fig, filename='TF_OHLC_volume_test.html', show_link=False)
print('ok')
