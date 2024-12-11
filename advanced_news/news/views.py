from django.shortcuts import render
from .models import NewsPost


# Create your views here.
def home(request):
    news: NewsPost = NewsPost.objects.all()
    return render(request, 'news/news.html', {'option': 'active', 'news': news})