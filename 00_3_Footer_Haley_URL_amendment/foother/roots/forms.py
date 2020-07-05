from django import forms
from .models import Food, Feeling

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'

        
class FeelingForm(forms.ModelForm):
    class Meta:
        model = Feeling
        fields = '__all__'

