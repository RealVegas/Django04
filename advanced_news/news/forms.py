from .models import NewsPost
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class NewsPostForm(ModelForm):
    class Meta:
        model = NewsPost
        fields = ['n_title', 'n_desc', 'n_text', 'n_date', 'n_author']
        widgets = {
            "n_title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок новости'
            }),
            "n_desc": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание новости'
            }),
            "n_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Новость'
            }),
            "n_author": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор'
            }),
            "n_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),

        }