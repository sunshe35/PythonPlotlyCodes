import plotly as py  # 导入plotly库并命名为py
import plotly.graph_objs as go

import pandas as pd
import numpy as np

# -------------pre def
pyplt = py.offline.plot

N = 40
x = np.linspace(0, 1, N)
y = np.random.randn(N)
df = pd.DataFrame({'x': x, 'y': y})
df.head()

data = [
    go.Bar(
        x=df['x'], # x可以是 DataFrame 的某一列
        y=df['y']
    )
]

url = pyplt(data, filename=r'tmp/basic_bar.html')