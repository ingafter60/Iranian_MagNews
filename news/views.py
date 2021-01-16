# NEWS/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import News


# Create your views here.
# def news_detail(request,pk):
def news_detail(request):

	# news = News.objects.filter(pk=pk)
	news = News.objects.all()

	context = {
		'news':news
	}
	
	return render(request, 'main/front/news_detail.html', context)
