# 2.10-5 distplot
import plotly as py
import plotly.graph_objs as go
import numpy as np
import plotly.figure_factory as ff
pyplt = py.offline.plot

# Add histogram data
s1 = np.random.RandomState(12)
# 柯西分布
x1 = s1.standard_cauchy(200) - 4  
# 泊松分布
x2 = s1.uniform(1,10,200)  
# Gamma 分布
x3 = s1.standard_gamma(3,200) + 4  
# 指数分布
x4 = s1.exponential(3,200) + 8  

# Group data together
hist_data = [x1, x2, x3, x4]

group_labels = ['Group 1', 'Group 2', 'Group 3', 'Group 4']

# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data, group_labels, bin_size=.4)

# Plot!
pyplt(fig, filename='tmp/Distplot_with_Multiple_Datasets.html')
