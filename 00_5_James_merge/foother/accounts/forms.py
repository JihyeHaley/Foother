from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms
from django.forms.widgets import SelectDateWidget


class CustomUserCreationForm(UserCreationForm):
    user_phone = forms.CharField(
        label = '핸드폰 번호:',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-user-phone form-control',
                'placeholder' : '핸드폰번호를 입력해주세요', 
            }
        )
    )
    user_birth = forms.DateField(
        label = '생일: ',
        widget = SelectDateWidget(
            empty_label = ('년', '월', '일'),
        ),
    )
    
    # 원래라면  forms.ModelForm
    # 내가 어떤 유저 모델을 가르키고 있는지를 알고 있어야 한다.
    # AUTH_USER_MODEL
    class Meta:
        model = get_user_model()
        fields = ('username',  'password1',  'password2', 'user_phone', 'user_birth', 'user_profile_image')

# '%Y-%m-%d'