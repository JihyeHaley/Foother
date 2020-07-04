from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, CommentForm
from .models import Review, Comment
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
@require_http_methods(['GET', 'POST'])
def review_create(request):
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
@require_http_methods(['GET', 'POST'])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    # if request.method == 'POST':
    #     form = ReviewForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         review = form.save(commit=False)
    #         review.user = request.user
    #         review.save()
    #         return redirect('maps:review-detail', review.pk)
    # else:
    #     form = ReviewForm(instance=review)
       
    context = {
        'review' : review,
    }
    return render(request, 'maps/review_detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def review_update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save
            # (commit=False)
            # review.user = request.user
            # review.save()
            return redirect('maps:review-detail', review.pk)
    else:
        form = ReviewForm(instance=review)
       
    context = {
        'form' : form,
    }
    return render(request, 'maps/review_update.html', context)



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


@login_required
def comment_create(request, review_pk):
    if request.method == 'POST':
        print("comment post 들어옴")
        review = Review.objects.get(pk=review_pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            print("comment post_valid 들어옴")
            comment = form.save(commit=False)
            print(comment)
            comment.review = review
            comment.save()
            return redirect('maps:comment-complete')
    
    else:
        print("comment get 들어옴")
        form = CommentForm()
        context = {
            'form' : form,
            'review_pk' : review_pk,
        }
        print(form)
    
    return render(request, 'maps/comment_create.html',context)

def comment_complete(request):
    return render(request, 'maps/comment_complete.html')


def review_all(request):
    reviews = Review.objects.all()
    # paginator = Paginator(reviews, 12)
    
    # page_number = request.GET.get('page')
    # reviews = paginator.get_page(page_number)
    # for star in len(reviews.food_star):
    

    context = {
        'reviews' : reviews,
    }
    return render(request, 'maps/review_all.html', context)