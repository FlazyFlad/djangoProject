from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .models import News
from captcha.fields import CaptchaField
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

class RegisterUserForm(UserCreationForm):

    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder':"Email"}))
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'required form-control', 'placeholder':"UserName"}))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder':"Password"}))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder':"Repeat Password"}))
    class Meta:
        model = User
        fields = ('email','username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':"Email"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': 'required form-control', 'placeholder':"Password"}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows':10}))
    captcha = CaptchaField()