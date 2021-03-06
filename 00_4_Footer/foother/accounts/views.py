from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required


def signup(request):
    if request.user.is_authenticated :
        return redirect('foother-index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('foother-index')

    else:
        form = CustomUserCreationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)

@login_required
def signup_update(request, username):
    user = get_object_or_404(User, username=username)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save()
            return redirect ('accounts:detail', user.username)
    else:
        form = CustomUserCreationForm(instance=user)
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup_update.html', context)



def login(request):
    if request.user.is_authenticated :
        return redirect('foother-index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # user = form.save()
            user = form.get_user()
            auth_login(request, user)
            return redirect('foother-index')

    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }

    return render(request, 'accounts/form.html', context)


def logout(request):
    auth_logout(request)
    return redirect('foother-index')
