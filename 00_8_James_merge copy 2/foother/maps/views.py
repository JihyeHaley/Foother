from django.shortcuts import render, redirect, get_object_or_404
from decouple import config
from .forms import ReviewForm
from .models import Review
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
@require_http_methods(['GET', 'POST'])
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
    print(request)
    review = get_object_or_404(Review, pk=review_pk)
    
    print(review)
    user = request.user
    # review.like_users.filter(pk=user.pk).exist():

    if review in user.like_reviews.all():
        user.like_reviews.remove(review)
        liked = False

    else:
        user.like_reviews.add(review)
        liked= True

    context = {
        'msg' : 'like works',
        'liked' : liked,
    }

    return JsonResponse(context)