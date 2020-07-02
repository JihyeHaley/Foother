from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def create(request):
    # user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('accounts:profile', review.user.username)

    else:
        form = ReviewForm()
        # key = config('API_KEY')

    context = {
        'form' : form,
        # 'key' : key,
    }
    return render(request, 'maps/review_create.html', context)


@login_required
def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    user = request.user

    if review in user.like_reviews.all():
        review.like_reviews.remove(review)
        liked = False

    else:
        review.like_reviews.add(review)
        liked= True

    context = {
        'msg' : 'like works',
        'liked' : liked,
    }

    return JsonResponse(context)