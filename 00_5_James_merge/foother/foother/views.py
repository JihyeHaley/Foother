from django.shortcuts import render
from maps.models import Review
from maps.forms import ReviewForm
from django.core.paginator import Paginator


def foother_index(request):
    reviews = Review.objects.all()
    paginator = Paginator(reviews, 12)
    
    page_number = request.GET.get('page')
    reviews = paginator.get_page(page_number)

    context = {
        'reviews' : reviews,
    }
    return render(request, 'base.html', context)