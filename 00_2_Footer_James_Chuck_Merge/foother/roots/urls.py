from django.urls import path
from . import views


app_name = 'roots'

urlpatterns = [
    path ('', views.root, name='root'),
]
