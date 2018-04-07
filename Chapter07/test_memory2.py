import plotly as py
import plotly.graph_objs as go

pyplt = py.offline.plot

# test memory1

trace0 = go.Bar(
    x=['Product A', 'Product B', 'Product C'],
    y=[20, 14, 23],
    text=['27% market share', '24% market share', '19% market share'],
    marker=dict(
        color='rgb(158,202,225)',
        line=dict(
            color='rgb(8,48,107)',
            width=1.5,
        )
    ),
    opacity=0.6
)

data = [trace0]
layout = go.Layout(
    title='January 2013 Sales Report',
)

fig = go.Figure(data=data, layout=layout)
div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)

if __name__ == '__main__':
    import sys
    print('参数div占用内存大小为 %d bytes'%sys.getsizeof(div))
    with open('div2.txt', 'w') as file:
        file.write(div)