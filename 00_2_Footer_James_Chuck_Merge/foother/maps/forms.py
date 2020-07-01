from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    lat = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    lng = forms.IntegerField(
        widget=forms.HiddenInput()
    )
    
    class Meta:
        model = Review
        exclude = ('user',)