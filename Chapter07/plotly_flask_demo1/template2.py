from flask import render_template
from flask import Flask

import plotly as py
import plotly.graph_objs as go

app = Flask(__name__)

@app.route('/')
def index():
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
    div = pyplt(fig, output_type='div', include_plotlyjs=False, auto_open=False, show_link=False)
    context = {}
    context['graph'] = div

    import sys
    print('参数div占用内存大小为 %d bytes'%sys.getsizeof(div))
    with open('div1.txt', 'w') as file:
        file.write(div)
        
    return render_template("index2.html",
        title = 'Home',
        context = context)   
    
if __name__ == '__main__':
      app.run()  
