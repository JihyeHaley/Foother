from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('create/', views.create, name='create'),
    # path('comment_create/<int:pk>', views.comment_create, name='comment_create')
]