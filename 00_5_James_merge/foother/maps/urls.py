from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('create/', views.create, name='create'),
    path('profile/<str:username>/', views.profile, name='profile'),
]