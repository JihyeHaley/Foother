from django.shortcuts import render
from .models import FoodCategory, FoodChoice
import random


def result(request, food_ctg):
    foodCategory = FoodCategory.objects.get(food_ctg=food_ctg)
    foods = foodCategory.foodchoice_set.all()
    randomfood = random.choice(foods)
    # emotion에 pk가 emotion_id인 emotion을 가지고 온다.
    # 그 emotion에 음식 세트를 모두 가져온다.
    context = {
        'foods' : foods,
        'randomfood' : randomfood,
        'foodCategory' : foodCategory,
    }
    print(foodCategory.foodchoice_set)
    return render(request,'foods/food_result.html', context)
    # 예상 food.emotion_


def hangover(request):
    foods = FoodChoice.objects.filter(status='해장')
    randomfood = random.choice(foods) 
    context = {
        'foods' : foods,
        'randomfood' : randomfood,
    }
    return render(request,'foods/food_result.html', context)


def select(request, food_name):
    food = FoodChoice.objects.get(food_name=food_name)
    context = {
        'food' : food,
    }
    return render(request, 'foods/food_select.html', context)
   

# def example(request):
#     return render(request, 'foods/example.html')