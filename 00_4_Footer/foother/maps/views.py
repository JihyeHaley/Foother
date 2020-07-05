from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from .forms import ReviewForm
from .models import Review
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required



def index(request):
    pass



@login_required
def review(request):
    # user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('maps:profile', review.username)

    else:
        form = ReviewForm()
        # key = config('API_KEY')

    context = {
        'form' : form,
        # 'key' : key,
    }
    return render(request, 'maps/review_create.html', context)


@login_required
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    context = {
        'review_user' : user,
    }
    return render(request, 'maps/review_profile.html', context)