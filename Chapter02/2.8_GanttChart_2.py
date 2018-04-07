# 2.8-2 应用案例
import plotly as py
import pandas as pd
import plotly.figure_factory as ff
# Index by Numeric Variable
pyplt = py.offline.plot
df = [dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Complete = 0),
      dict(Task="Job B", Start='2008-12-05', Finish='2009-04-15', Complete = 50),
      dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Complete = 100)]

fig = ff.create_gantt(df, colors='Viridis', index_col='Complete', show_colorbar=True)
pyplt(fig, filename='tmp/gantt-numeric-variable.html')