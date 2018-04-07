import plotly as py
import plotly.figure_factory as FF
import pandas as pd

# ----------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat\day01.csv', index_col=[0])
df_sample = df[100:150]

colorscale = [[0, '#4d004c'], [.5, '#f2e5ff'], [1, '#ffffff']]
fontcolor = ['#FF0000', '#00EE00', '#FF3030']
a = 'rgba(0,0,0,0)'
b = rgba(152, 0, 0, .8)
    titlefont = dict(
        color='rgb(0, 0, 255)'
        color='rgb(32, 253, 1)'
    ),
    a = 'gb(50, 35, 219)',
    b = '#00EE00',
        tickfont = dict(
            color='rgb(148, 103, 189)'
        ),
table = FF.create_table(df_sample, index=True,
                        colorscale=colorscale, font_colors=fontcolor)
table.layout.width = 1000

# 设置文本大小
for i in range(len(table.layout.annotations)):
    table.layout.annotations[i].font.size = 10 + (i % 50) * 0.2
pyplt(table, filename=r'tmp\style_table.html', show_link=False)
