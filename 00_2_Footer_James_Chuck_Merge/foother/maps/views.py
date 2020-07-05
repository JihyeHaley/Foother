from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from .forms import ReviewForm
from .models import Review
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def review_create(request):
    # key = config('API_KEY')
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('maps:review-profile', review.username)


    else:
        form = ReviewForm()

    context = {
        'map_form' : form,
        # 'key' : key,
    }

    return render(request, 'maps/_chuck_main_input.html', context)

@login_required
def review_profile(request, username):
    reviews = get_object_or_404(get_user_model(), username=username)
    context = {
        'reviews' : reviews,
    }
    return render(request, 'maps/_chuck_main_profile.html', context)