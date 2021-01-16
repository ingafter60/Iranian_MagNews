# MAIN/urls.py

from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('', home, name='home'),
    url(r'^$', views.home, name='home'),
    # path('about/', about, name='about'),
    url(r'^about/$', views.about, name='about'),
]
