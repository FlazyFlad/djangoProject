from django import forms
from .models import *

class AddNewsForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].empty_label="Выберите жанр"
        self.fields['author_id'].empty_label = "Выберите автора"
    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'image', 'category_id', 'author_id']
        widgets = {
            'content': forms.Textarea(attrs={'cols': 60, 'rows':10})
        }
