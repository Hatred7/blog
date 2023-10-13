from django import forms
from .models import *


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Название поста'}), label='Название поста')
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea', 'size': 40, 'placeholder': 'Напишите текст поста'}), label='Текст поста')
    image = forms.ImageField(label='Картинка для поста', required=False)
    comments_allowed = forms.BooleanField(label='Комменты разрешены', widget=forms.CheckboxInput(), required=False)

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'comments_allowed']


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input', 'placeholder': "Оставьте ваш комментарий"
    }))

    class Meta:
        model = Comment
        fields = ['text', ]
