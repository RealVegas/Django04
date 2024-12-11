from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm


# Create your views here.
def home(request):
    news: NewsPost = NewsPost.objects.all()
    return render(request, 'news/news.html', {'option': 'active', 'news': news})


def create_news(request):

    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')

    form: NewsPostForm = NewsPostForm()
    return render(request, 'news/add_entry.html', {'option': 'active', 'form': form})