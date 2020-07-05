from django.shortcuts import render
from .models import FoodCategory, FoodChoice

# Create your views here.
def main(request):
    foodsCategories = FoodCategory.objects.all()
    # emotion = Emotion.objects.get(name=Food.food_name).emotion
    # foods = emotion.food_set.all()

    context = {
        'foodsCategories' : foodsCategories,
        # 'foods' : foods
    }
    return render(request,'foods/food_main.html', context)


def result(request, food_ctg):
    foodCategory = FoodsCategory.objects.get(food_ctg=food_ctg)
    foods = foodCategory.foodChoice_set.all()
    # emotion에 pk가 emotion_id인 emotion을 가지고 온다.
    # 그 emotion에 음식 세트를 모두 가져온다.
    context = {
        'foods' : foods,
    }
    return render(request,'foods/food_result.html', context)
    # 예상 food.emotion_

def select(request, food_name):
    food = FoodChoice.objects.get(food_name=food_name)
    context = {
        'food' : food,
    }
    return render(request, 'foods/food_select.html', context)
   

# def example(request):
#     return render(request, 'foods/example.html')