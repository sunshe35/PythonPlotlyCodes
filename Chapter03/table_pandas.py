import plotly as py
from plotly.tools import FigureFactory as FF

import pandas as pd

# ----------pre def
pyplt = py.offline.plot

df = pd.read_csv(r'dat\day01.csv',index_col=[0])
df_sample = df[100:120]


table = FF.create_table(df_sample, index=True, index_title='Date')
pyplt(table, filename=r'tmp\table_pandas.html', show_link=False)

