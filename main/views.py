# MAIN/views.py

from django.shortcuts import render

# Create your views here.
def home(request):

	sitename = 'Home page'

	return render(request, 'main/front/home.html', {'sitename':sitename})


def about(request):

	sitename = 'About page'
	
	return render(request, 'main/front/about.html', {'sitename':sitename})