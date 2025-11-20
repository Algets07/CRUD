from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class registerform(UserCreationForm):
    class Meta:
        model = User
        fields =['username','email','password1','password2']
    
    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter username',
                'class':'form-control'
            }
        )
    )
    email= forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'placeholder':'enter email',
                'class':'form-control'
            }
        )
    )
    password1=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )
    password2=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'confirm password',
                'class':'form-control'
            }
        )
    )

class loginform(AuthenticationForm):
    class Meta:
        model = User
        fields =['username','password']

    username= forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'enter username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'
            }
        )
    )