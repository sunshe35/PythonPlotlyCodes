import plotly as py
import plotly.graph_objs as go

import datetime


# ----------pre def
pyplt = py.offline.plot

# ----------code
def to_unix_time(dt):
    '''
    :param dt:datetime类型的时间戳 
    :return: dt相对于utc起始时间差别的毫秒数
    '''
    epoch =  datetime.datetime.utcfromtimestamp(0) # 获取0时刻对应的utc（世界标准时间）
    return (dt - epoch).total_seconds() * 1000 # 计算传入的时间相对于utc的起始时间差别多少毫秒

x = [datetime.datetime(year=2013, month=10, day=4),
    datetime.datetime(year=2013, month=11, day=5),
    datetime.datetime(year=2013, month=12, day=6)]

data = [go.Scatter(
            x=x,
            y=[1, 3, 6])]

layout = go.Layout(xaxis = dict(
                   range = [to_unix_time(datetime.datetime(2013, 10, 17)),
                            to_unix_time(datetime.datetime(2013, 11, 20))]
    ))

fig = go.Figure(data = data, layout = layout)
pyplt(fig, filename='tmp/timeRange.html')
