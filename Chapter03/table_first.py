import plotly as py
import plotly.figure_factory as FF

# ----------pre def
pyplt = py.offline.plot


data_matrix = [['国家', '年份', '人口'],
               ['中国',2000, 1267430000],
               ['美国', 2000, 282200000],
               ['加拿大', 2000, 27790000],
               ['中国', 2005, 1307560000],
               ['美国', 2005, 295500000],
               ['加拿大', 2005, 32310000],
               ['中国', 2010, 1340910000],
               ['美国', 2010, 309000000],
               ['加拿大', 2010, 34000000]]

table = FF.create_table(data_matrix)
pyplt(table, filename='tmp\simple_table', show_link=False)