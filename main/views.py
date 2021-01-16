# MAIN/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News


# Create your views here.
def home(request):

	site = Main.objects.get(pk=2)
	news = News.objects.all()

	context = {
		'site':site,
		'news':news
	}
	
	return render(request, 'main/front/home.html', context)


def about(request):

	site = Main.objects.get(pk=2)
	return render(request, 'main/front/about.html', {'site':site})