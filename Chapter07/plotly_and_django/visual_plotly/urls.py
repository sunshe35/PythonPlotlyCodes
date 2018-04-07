from .views import plotly_view, plotly_view2
from django.conf.urls import url


urlpatterns = [
    url(r'^$', plotly_view),
    url(r'^demo2', plotly_view2),
]
