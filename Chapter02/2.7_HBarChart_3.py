# 2.7-3 应用案例
import plotly as py
import plotly.graph_objs as go
from plotly import tools

# Bar Chart with Line Plot
pyplt = py.offline.plot
y_saving = [1.3586, 2.2623000000000002, 4.9821999999999997, 6.5096999999999996,
            7.4812000000000003, 7.5133000000000001, 15.2148, 17.520499999999998
            ] # 对应柱形的长度
y_net_worth = [93453.919999999998, 81666.570000000007, 69889.619999999995,
               78381.529999999999, 141395.29999999999, 92969.020000000004,
               66090.179999999993, 122379.3] # 对应折线的值，分别对应从下至上
x_saving = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
            'United States', 'Belgium', 'Sweden', 'Switzerland']
x_net_worth = ['Japan', 'United Kingdom', 'Canada', 'Netherlands',
               'United States', 'Belgium', 'Sweden', 'Switzerland'
               ]
trace0 = go.Bar(
    x = y_saving,
    y = x_saving,
    marker = dict(
        color = 'rgba(50, 171, 96, 0.6)', # 柱形颜色
        line = dict(
            color = 'rgba(50, 171, 96, 1.0)', # 柱形边框颜色
            width = 1),
    ),
    name = 'Household savings, percentage of household disposable income',
    orientation = 'h',
)
trace1 = go.Scatter(
    x = y_net_worth,
    y = x_net_worth,
    mode = 'lines + markers',
    line = dict(
        color = 'rgb(128, 0, 128)'), # 折线颜色
    name = 'Household net worth, Million USD/capita',
)
layout = dict(
    title = 'Household savings & net worth for eight OECD countries',
    # 左边的图 y 轴
    yaxis1 = dict(
        showgrid = False,          # 是否显示横向网格
        showline = False,          # 是否显示左侧轴线
        showticklabels = True,     # 是否显示坐标轴上的标注
        domain = [0, 0.85],
    ),
    # 右边的图 y 轴
    yaxis2 = dict(
        showgrid = False,
        showline = True,
        showticklabels = False,
        linecolor = 'rgba(102, 102, 102, 0.8)', # 左侧轴线颜色
        linewidth = 2,
        domain = [0, 0.85],
    ),
    # 左边的图 x 轴
    xaxis1 = dict(
        zeroline = False,     # 是否显示左侧轴线
        showline = False,     # 是否显示下方轴线
        showticklabels = True,
        showgrid = True,      # 是否显示纵向网格
        domain = [0, 0.42],
    ),
    # 右边的图 x 轴
    xaxis2 = dict( 
        zeroline = False, 
        showline = False, 
        showticklabels = True, 
        showgrid = True, 
        domain = [0.47, 1],
        side = 'top', # 轴上标注在上方，默认下方
        dtick = 25000, # 调整轴上标注数值间隔，25000表示相邻标注间隔数值为25000
    ),
    legend = dict(
        x = 0.029,   # 图例x位置
        y = 1.038,   # 图例y位置
        font = dict(
            size = 10, # 图例字号大小
        ),
    ),
    margin = dict(
        l = 100, # 左侧空白大小
        r = 20,  # 右侧空白大小
        t = 70,  # 上方空白大小
        b = 70,  # 下方空白大小
    ),
    paper_bgcolor = 'rgb(248, 248, 255)', # 整张图片背景颜色
    plot_bgcolor = 'rgb(248, 248, 255)',  # 绘图部分背景颜色
)

annotations = []

y_s = np.round(y_saving, decimals = 2) # 四舍五入至两位小数
y_nw = np.rint(y_net_worth)            # 四舍五入至整数

for ydn, yd, xd in zip(y_nw, y_s, x_saving): # 把数据对应起来
    # 右侧折线图设置标签
    annotations.append(dict(xref = 'x2', yref = 'y2',
                            y = xd, x = ydn - 20000,
                            text='{:,}'.format(ydn) + 'M', # 从右向左，每隔三位','
                            font = dict(family = 'Arial', size = 12, 
                                      color = 'rgb(128, 0, 128)'), # 设置标签字体，颜色与大小
                            showarrow = False)) # 是否添加从标签到数据点的箭头
    # 左侧水平柱形图设置标签
    annotations.append(dict(xref = 'x1', yref = 'y1',
                            y = xd, x = yd + 3,
                            text = str(yd) + '%',
                            font = dict(family = 'Arial', size = 12,
                                      color = 'rgb(50, 171, 96)'),
                            showarrow = False))
# 下侧标签设置
annotations.append(dict(xref = 'paper', yref = 'paper', # 设置文字样式
                        x = 0.3, y = -0.05, # 设置文字位置
                        text = 'OECD "' +
                             '(2015), Household savings (indicator), ' +
                             'Household net worth (indicator). doi: ' +
                             '10.1787/cfc6f499-en (Accessed on 05 June 2015)', # 设置图下方文字
                        font = dict(family = 'Arial', size = 10, # 设置图下方文字格式
                                  color = 'rgb(150,150,150)'),
                        showarrow = False))

layout['annotations'] = annotations

# Creating two subplots
# shared_yaxes 不共享y轴，shared_xaxes 共享x轴，rows = 1, cols = 2 表示划分为两个子图
fig = tools.make_subplots(rows = 1, cols = 2, 
                          shared_xaxes = True,
                          shared_yaxes = False)

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)

fig['layout'].update(layout)
pyplt(fig, filename='tmp/oecd-networth-saving-bar-line.html')