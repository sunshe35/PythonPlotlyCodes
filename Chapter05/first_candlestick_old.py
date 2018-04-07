import plotly as py  # 导入plotly库并命名为py
import plotly.figure_factory   as ff  # 导入plotly工具箱库中的图像工厂方法并命名为FF


# -------------pre def
pyplt = py.offline.plot
import pandas as pd


df = pd.read_csv(r'dat/appl.csv', index_col=['date'], parse_dates=['date'])

fig = ff.create_candlestick(df.open, df.high, df.low, df.close, dates=df.index)

pyplt(fig, filename=r'tmp/first_candlestick_old.html')

