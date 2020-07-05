  
from django.urls import path
from . import views

app_name = 'maps'
urlpatterns = [
    path('review/create/', views.review_create, name='review-create'),
    path('<str:username>/review/profile/', views.review_profile, name='review-profile'),
]