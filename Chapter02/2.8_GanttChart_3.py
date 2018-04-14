# 2.8-3 应用案例
import plotly as py
import plotly.figure_factory as ff
pyplt = py.offline.plot

df = [dict(Task="Job-1", Start='2017-01-01', Finish='2017-02-02', Resource='Complete'),
      dict(Task="Job-2", Start='2017-02-15', Finish='2017-03-15', Resource='Incomplete'),
      dict(Task="Job-3", Start='2017-01-17', Finish='2017-02-17', Resource='Not Started'),
      dict(Task="Job-4", Start='2017-01-17', Finish='2017-02-17', Resource='Complete'),
      dict(Task="Job-5", Start='2017-03-10', Finish='2017-03-20', Resource='Not Started'),
      dict(Task="Job-6", Start='2017-04-01', Finish='2017-04-20', Resource='Not Started'),
      dict(Task="Job-7", Start='2017-05-18', Finish='2017-06-18', Resource='Not Started'),
      dict(Task="Job-8", Start='2017-01-14', Finish='2017-03-14', Resource='Complete')]

colors = {'Not Started': 'rgb(220, 0, 0)',
          'Incomplete': (1, 0.9, 0.16),
          'Complete': 'rgb(0, 255, 100)'}

fig = ff.create_gantt(df, colors=colors, index_col='Resource', group_tasks=True)
pyplt(fig, filename='tmp/gantt-group-tasks-together.html')
