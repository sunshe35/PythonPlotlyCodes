import os

from django.shortcuts import redirect
from django.shortcuts import render

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
# Create your views here.
from plotly_django_app2.chart_plot import ChartPlot
chart = ChartPlot()
context = {}

def index(request):
    context['graph_range_slide'] = chart.range_slide()
    return render(request, 'index.html', context=context)

def start(request):
    return redirect(r'/index.html')

def charts(request):
    context['graph_basic_plot']= chart.basic_plot()
    context['graph_line_full'] = chart.line_full()
    context['graph_bar_chart'] = chart.bar_chart()
    context['graph_bonus_chart'] = chart.bonus_chart()
    context['graph_pie_chart'] = chart.pie_chart()
    context['graph_stacked_bar'] = chart.stacked_bar()
    context['graph_horizontal_chart'] = chart.horizontal_chart()
    return render(request, 'charts.html', context=context)


def finances(request):
    return render(request, 'finances.html')


def ui(request):
    return render(request, 'ui.html')


def tables(request):
    return render(request, 'tables.html')


def form_demo(request):
    return render(request, 'form_demo.html')


def form_elements(request):
    return render(request, 'form_elements.html')


def bookings(request):
    return render(request, 'bookings.html')


def calendar(request):
    return render(request, 'calendar.html')


def documentation(request):
    return render(request, 'documentation.html')


def file_managers(request):
    return render(request, 'file_managers.html')


def form_elements(request):
    return render(request, 'form_elements.html')


def form_validator(request):
    return render(request, 'form_validator.html')


def gallery(request):
    return render(request, 'gallery.html')


def login(request):
    return render(request, 'login.html')

def pages(request):
    return render(request, 'pages.html')

def product_edit(request):
    return render(request, 'product_edit.html')
