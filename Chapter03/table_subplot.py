import plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF


# ----------pre def
pyplt = py.offline.plot


# 添加表格数据
table_data = [['团队', '赢', '输', '平'],
              ['清华大学', 18, 4, 0],
              ['北京大学', 18, 5, 0],
              ['中国<br>人民大学', 16, 5, 0],
              ['复旦大学', 13, 8, 0],
              ['上海<br>交通大学', 13, 8, 0],
              ['同济大学', 13, 8, 0]]
# 通过 FF.create_table(table_data)来初始化一个figure
figure = FF.create_table(table_data, height_constant=60)

# 添加绘图数据
teams = ['清华大学', '北京大学', '中国<br>人民大学',
         '复旦大学', '上海<br>交通大学', '同济大学']
scoreA = [3.54, 3.48, 3.0, 3.27, 2.83, 2.45]
scoreB = [2.17, 2.57, 2.0, 2.91, 2.57, 2.14]
# 对绘图添加 traces
trace1 = go.Scatter(x=teams, y=scoreA,
                    marker=dict(color='#0099ff'),
                    name='分值A',
                    xaxis='x2', yaxis='y2')
trace2 = go.Scatter(x=teams, y=scoreB,
                    marker=dict(color='#404040'),
                    name='分值B',
                    xaxis='x2', yaxis='y2')

# 把 trace 添加到 figure 中
figure['data'].extend(go.Data([trace1, trace2]))

# 设置 figure 的 layout
figure.layout.xaxis.update({'domain': [0, .5]})
figure.layout.xaxis2.update({'domain': [0.6, 1.]})
# 图的 yaxis 要与图的 xaxis 对应
figure.layout.yaxis2.update({'anchor': 'x2'})
figure.layout.yaxis2.update({'title': '分值'})
# 设置figure的边界 .
figure.layout.margin.update({'t':50, 'b':100})
figure.layout.update({'title': '20xx年部分高校xx游戏比赛'})

# 画图!
pyplt(figure, filename='tmp/subplot_table', show_link=False)