# MAIN/urls.py

from django.urls import path
from main.views import home, about

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
]
