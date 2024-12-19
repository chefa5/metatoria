from django.shortcuts import render
from attractions.models import Card
# Create your views here.

def attractions(request):
    Cards = Card.objects.all()
    context = {
        'cards': Cards
    }
    return render(request, 'attractions/attractions.html', context)