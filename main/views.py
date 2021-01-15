# MAIN/views.py

from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'main/front/home.html')


def about(request):
	return render(request, 'main/front/about.html')