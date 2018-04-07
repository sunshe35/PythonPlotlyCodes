import plotly as py
import plotly.figure_factory  as FF


# ----------pre def
pyplt = py.offline.plot


data_matrix = [['用户', '编程语言', '绘图类型', '浏览数量'],
               ['<a href="https://plot.ly/~empet/folder/home">empet</a>',
                '<a href="https://plot.ly/python/">Python</a>',
                '<a href="https://plot.ly/~empet/8614/">Network Graph</a>',
                298],
               ['<a href="https://plot.ly/~Grondo/folder/home">Grondo</a>',
                '<a href="https://plot.ly/matlab/">Matlab</a>',
                '<a href="https://plot.ly/~Grondo/42/">Subplots</a>',
                356],
               ['<a href="https://plot.ly/~Dreamshot/folder/home">Dreamshot</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plot.ly/~Dreamshot/6575/_2014-us-city-populations/">Bubble Map</a>',
                262],
               ['<a href="https://plot.ly/~FiveThirtyEight/folder/home">FiveThirtyEight</a>',
                '<a href="https://help.plot.ly/tutorials/">Web App</a>',
                '<a href="https://plot.ly/~FiveThirtyEight/30/">Scatter</a>',
                692],
               ['<a href="https://plot.ly/~cpsievert/folder/home">cpsievert</a>',
                '<a href="https://plot.ly/r/">R</a>',
                '<a href="https://plot.ly/~cpsievert/1130/">Surface</a>',
                302]]

table = FF.create_table(data_matrix)
pyplt(table, filename='tmp\linked_table', show_link=False)