from django.db import models

# Create your models here.
class Feeling(models.Model):
    feeling_name = models.CharField(max_length=20)

class Food(models.Model):
    food_name = models.CharField(max_length=30)
    food_by_emotion = models.ForeignKey(Feeling, on_delete=models.CASCADE)