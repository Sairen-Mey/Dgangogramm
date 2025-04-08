from .models import User, Post
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login
from django.shortcuts import render
class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Input password')
    confirm_password = forms.CharField(max_length=65, widget=forms.PasswordInput, label='Repeat password')
    class Meta():
        model = User
        fields = ['email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", min_length=8)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        # Спроба автентифікації користувача
        user = authenticate(email=email, password=password)

        if user is None:
            raise ValidationError("Невірний email або пароль.")

        # Зберігаємо користувача у формі
        self.user = user

        return cleaned_data


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = [single_file_clean(data, initial)]
        return result


class PostForm(forms.ModelForm):
    images = MultipleFileField(required=False)

    class Meta:
        model = Post
        fields = ['content', 'images']
