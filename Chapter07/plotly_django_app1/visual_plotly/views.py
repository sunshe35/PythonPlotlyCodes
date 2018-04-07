from django.shortcuts import render

import plotly as py
import plotly.graph_objs as go

def plotly_view(request):
    pyplt = py.offline.plot

    trace0 = go.Bar(
        x=['A类户型', 'B类户型', 'C类户型'],
        y=[20, 14, 23],
        text=['27%市场占有率', '24%市场占有率', '19%市场占有率'],
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
        title='2017年1月不同户型房屋单价情况',
    )

    fig = go.Figure(data=data, layout=layout)
    div = pyplt(fig, output_type='div', auto_open=False, show_link=False, include_plotlyjs=False)
    context = {}
    context['graph'] = div
    return render(request, 'index.html', context=context)



