from django.contrib import admin
from django.urls import path
from . import views

app_name = 'foods'

urlpatterns = [
    path('', views.main, name='main'),
    path('<str:food_ctg>/', views.result, name='result'),
    path('<str:food_name>/select', views.select, name='select'),
    # path("example/", views.example, name='example'),
]