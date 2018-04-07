from flask import Flask
from flask import render_template

app = Flask(__name__)
from chart_plot import Chart_Plot

chart = Chart_Plot()

context = {}

@app.route('/')
def index():
    context['bar_graph'] = chart.bar_graph()
    context['line_graph'] = chart.line_graph()
    context['pie_graph'] = chart.pie_graph()
    context['twoline_graph'] = chart.twoline_graph()
    
    return render_template("chars.html", title='Home', context=context)

@app.route('/bar')
def index2():
    context['graph'] = chart.bar_graph()

    return render_template("bar.html", title='Home', context=context)

@app.route('/faq')
def faq():
    context = {}

    return render_template("faq.html",title='Home',context=context)

@app.route('/plans')
def plans():
    context = {}

    return render_template("plans.html",title='Home',context=context)

@app.route('/grid')
def grid():
    context = {}

    return render_template("grid.html",title='Home',context=context)

@app.route('/charts')
def charts():
    context = {}

    return render_template("charts.html",title='Home',context=context)

@app.route('/account')
def account():
    context = {}

    return render_template("account.html",title='Home',context=context)

@app.route('/login')
def login():
    context = {}

    return render_template("login.html",title='Home',context=context)

if __name__ == '__main__':
    app.run( port=5000 )
