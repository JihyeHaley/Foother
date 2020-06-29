from django.shortcuts import render, redirect
from decouple import config
from .forms import ReviewForm

# Create your views here.
def index(request):
    pass

def review(request):
    # user = request.user
    form = ReviewForm()
    key = config('API_KEY')

    context = {
        'form' : form,
        'key' : key,
    }
    return render(request, 'maps/_chuck_main_input.html', context)
    