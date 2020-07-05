from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('<int:user_pk>/signup/update/', views.signup_update, name='signup_update'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]


