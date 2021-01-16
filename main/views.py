# MAIN/views.py

from django.shortcuts import render
from .models import Main


# Create your views here.
def home(request):

	site = Main.objects.get(pk=2)
	return render(request, 'main/front/home.html', {'site':site})


def about(request):

	site = Main.objects.get(pk=2)
	return render(request, 'main/front/about.html', {'site':site})