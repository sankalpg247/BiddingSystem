from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm



User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


CHOICES = [('Citizen', 'Citizen'),
           ('Farmer', 'Farmer')]


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    userType = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'password1', 'password2', 'userType',
        )
