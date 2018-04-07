import plotly as py
import plotly.graph_objs as go
import pandas as pd

# ----------pre def
pyplt = py.offline.plot

# ----------code
df = pd.read_csv(r'dat/day01.csv',index_col=[0])

trace = go.Scatter(x=df.index,
                   y=df.close)

data = [trace]
layout = dict(
    title='时间序列的滑块与选择器',
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label='1m',
                     step='month',
                     stepmode='backward'),
                dict(count=6,
                     label='6m',
                     step='month',
                     stepmode='backward'),
                dict(count=1,
                    label='YTD',#今天以来
                    step='year',
                    stepmode='todate'),
                dict(count=1,
                    label='1y',
                    step='year',
                    stepmode='backward'),
                dict(step='all')
            ])
        ),
        rangeslider=dict(),
        type='date'
    )
)
fig = dict(data=data, layout=layout)
pyplt(fig,filename='tmp/RangeSlide.html')