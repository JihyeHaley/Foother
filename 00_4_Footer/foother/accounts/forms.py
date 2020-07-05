from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User
from django import forms


class CustomUserCreationForm(UserCreationForm):
    user_birth = forms.DateField(
                widget=forms.DateInput(
                    format='%Y-%m-%d',
                    attrs={
                        "class": "form-control text-input",
                    }
                ),
    )
    # 원래라면  forms.ModelForm
    # 내가 어떤 유저 모델을 가르키고 있는지를 알고 있어야 한다.
    # AUTH_USER_MODEL
    class Meta:
        model = get_user_model()
        fields = ('username',  'password1',  'password2', 'user_phone', 'user_birth', 'user_profile_image')

# '%Y-%m-%d'