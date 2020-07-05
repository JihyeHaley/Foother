from django.db import models

# Create your models here.
class FoodCategory(models.Model):
    food_ctg = models.CharField(max_length=100) 
    # selectbox로 설정
    # img = models.ImageField()
    # food_set 자동생김    


class FoodChoice(models.Model):
    food_name = models.CharField(max_length=100)
    food_ctgs = models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    # food_by_emotion