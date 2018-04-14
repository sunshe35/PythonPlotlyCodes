# -*- coding: utf-8 -*-

import pandas as pd
import pandas as pd
import plotly as py
import plotly.graph_objs as pygo

# ----------pre def
pd.set_option('display.width', 450)
pyplt = py.offline.plot
# ----------code
df = pd.read_csv('dat/tk01_m15.csv')
df9 = df[:10];
print(df9)
#
idx = df9['xtim']
xd0 = (df9['close'] - 27) * 50
df2 = df9
df2['xd1'] = xd0 - 10
df2['xd2'] = xd0
df2['xd3'] = xd0 + 10

print('xd2\n', df2);
# --------
xtr1 = pygo.Scatter(
    x=idx,
    y=df2['xd1'],
    mode='markers',  # xtr1,散点图
    name='xtr1-markers',
)
xtr2 = pygo.Scatter(
    x=idx,
    y=df2['xd2'],
    mode='lines',  # xtr2,曲线图
    name='xtr2-lines',
)
xtr3 = pygo.Scatter(
    x=idx,
    y=df2['xd3'],
    mode='markers+lines',  # xtr3,曲线+散点组合
    name='xtr3-markers+lines',
)
xdat = pygo.Data([xtr1, xtr2, xtr3])
layout = pygo.Layout(
    title='收盘价--15分钟分时数据',
    xaxis=pygo.XAxis(tickangle=-15),

)
fig = pygo.Figure(data=xdat, layout=layout)
pyplt(fig,filename=r'tmp\scatter_apply.html')
#
print('ok')

