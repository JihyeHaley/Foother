from django import forms
from .models import Review
from django.forms.widgets import SelectDateWidget

class ReviewForm(forms.ModelForm):
    # hidden tag
    lat = forms.FloatField(
        widget=forms.HiddenInput()
    )
    lng = forms.FloatField(
        widget=forms.HiddenInput()
    )
    restaurant_address = forms.CharField(
        widget=forms.HiddenInput()
    )
    restaurant_name = forms.CharField(
        label = "﹅먹은 장소: ",
        widget=forms.TextInput(
            attrs = {
                'class' : 'my-restaurant-name form-control',
                'placeholder' : '먹은 장소를 입력해주세요',
                'readonly' : '',
            }
        )
    )


    # TextInput
    food_name = forms.CharField(
        label = "﹅먹은 것: ",
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-food-name form-control',
                'placeholder' : '먹은 것을 입력해주세요',
            }
        )
    )

    # Textarea
    food_review = forms.CharField(
        label = '﹅후기: ',
        widget = forms.Textarea(
            attrs = {
                'class' : 'my-food-review form-control',
                'placeholder' : '후기를 입력해주세요',
                'rows' : 5,
                'cols' : 20,
            }
        )
    )


    food_star = forms.FloatField(
        label = '﹅별점: ',
        widget = forms.NumberInput(
            attrs = {
                'class' : 'my-food-review form-control',
                'placeholder' : '평점을 주세요.',
            }
        )
    )

        
    visit_date = forms.DateField(
        label = '﹅방문 날짜: ',
        widget = SelectDateWidget(
            empty_label = ('년', '월', '일',)
        ),
    )


    
    class Meta:
        model = Review
        exclude = ('user',)