from django.shortcuts import render
from foods.models import FoodCategory
# from django.core.paginator import Paginator


def foother_index(request):
    foodsCategories = FoodCategory.objects.all()

    # emotion = Emotion.objects.get(name=Food.food_name).emotion
    # foods = emotion.food_set.all()

    context = {
        'foodsCategories' : foodsCategories,
        # 'foods' : foods
    }

    return render(request,'foods/food_main.html', context)
    