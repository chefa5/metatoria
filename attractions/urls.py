from django.urls import path

from attractions import views

urlpatterns = [
    path('', views.attractions, name='attractions'),
]