from django.shortcuts import render
from main.models import News

def index(request):
    news = News.objects.order_by('-date')[:5]
    
    context = {
        'news': news
    }
    return render(request, 'main/index.html', context)