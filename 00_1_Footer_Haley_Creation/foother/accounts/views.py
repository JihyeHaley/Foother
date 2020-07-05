from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


def index(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.user.is_authenticated :
        return redirect('accounts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = CustomUserCreationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)
    

def detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/detail.html', context)


def signup_update(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect ('accounts:detail', user.pk)
    else:
        form = CustomUserCreationForm(instance=user)
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup_update.html', context)

def login(request):
    if request.user.is_authenticated :
        return redirect('accounts:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # user = form.save()
            user = form.get_user()
            auth_login(request, user)
            return redirect('accounts:index')

    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')
