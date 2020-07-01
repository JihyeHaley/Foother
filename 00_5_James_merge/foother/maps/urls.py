from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('create/', views.review, name='review'),
    path('profile/<str:username>/', views.profile, name='profile'),
]