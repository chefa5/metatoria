from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('auth/', views.auth, name='auth'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
]