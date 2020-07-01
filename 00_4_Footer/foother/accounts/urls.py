from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('<str:username>/signup/update/', views.signup_update, name='signup_update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


