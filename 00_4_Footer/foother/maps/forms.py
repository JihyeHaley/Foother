from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    lat = forms.FloatField(
        widget=forms.HiddenInput()
    )
    lng = forms.FloatField(
        widget=forms.HiddenInput()
    )
    restaurant_address = forms.CharField(
        widget=forms.HiddenInput()
    )

    food_name = forms.CharField(
        label='음식 이름:',
        widget=forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : '음식 이름을 입력하세요',
            }
        )
    )
    
    class Meta:
        model = Review
        exclude = ('user',)