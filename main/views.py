# MAIN/views.py

from django.shortcuts import render
from .models import Main


# Create your views here.
def home(request):

	# pagetitle = Main.objects.filter(pk=1)
	pagetitle = Main.objects.get(pk=1)

	return render(request, 'main/front/home.html', {'pagetitle':pagetitle})


def about(request):

	sitename = 'About page'
	
	return render(request, 'main/front/about.html', {'sitename':sitename})