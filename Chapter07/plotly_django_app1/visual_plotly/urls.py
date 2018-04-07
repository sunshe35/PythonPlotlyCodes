from .views import plotly_view
from django.conf.urls import url


urlpatterns = [
    url(r'^$', plotly_view),
]
