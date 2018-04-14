# 2.8-1 基本示例
import plotly as py
import plotly.figure_factory as ff

# Simple Gantt Chart
pyplt = py.offline.plot

df = [dict(Task = "Job A", Start = '2009-01-01', Finish = '2009-02-28'),
      dict(Task = "Job B", Start = '2009-03-05', Finish = '2009-04-15'),
      dict(Task = "Job C", Start = '2009-02-20', Finish = '2009-05-30')]

fig = ff.create_gantt(df)
pyplt(fig, filename='tmp/gantt-simple-gantt-chart.html')