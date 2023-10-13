from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input", 
            'placeholder': 'Создайте никнейм'}
            ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "input", 
            'placeholder': 'Укажите пароль'}
            ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "input", 
            'placeholder': 'Повторите пароль'}
            ))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    

    
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "input", 
            'placeholder': 'Укажите имя'}
            ))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "input", 
            'placeholder': 'Укажите пароль'}
            ))
    
    class Meta:
        model = User
        fields = ['username', 'password1']

    


