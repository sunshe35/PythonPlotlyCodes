# 2.8-3 应用案例
import plotly as py
import pandas as pd
import plotly.figure_factory as ff
# Index by String Variable
pyplt = py.offline.plot

df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-01', Resource='Apple'),
      dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource='Grape'),
      dict(Task="Job C", Start='2009-04-20', Finish='2009-09-30', Resource='Banana')]

# colors = ['#7a0504', (0.2, 0.7, 0.3), 'rgb(210, 60, 180)']
colors = dict(Apple = '#7a0504',
              Grape = (0.2, 0.7, 0.3),
              Banana = 'rgb(210, 60, 180)')
fig = ff.create_gantt(df, colors=colors, index_col='Resource', show_colorbar = True,\
                     bar_width=0.3, showgrid_x=True, showgrid_y=True) # reverse_colors = True(按逆序配置颜色)，列表可以，字典不可以
pyplt(fig, filename='tmp/gantt-string-variable.html')