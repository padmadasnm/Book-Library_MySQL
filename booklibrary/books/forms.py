from django.forms import ModelForm
from django import forms
from .models import MyUser, Books
from .admin import UserCreationForm


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=25, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = MyUser
        fields = ["email", "username", "date_of_birth", "password1", "password2"]
        widgets = {
            "email": forms.TextInput(attrs={'class': 'form-control'}),
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "date_of_birth": forms.DateInput(attrs={'class': 'form-control'}),
        }


class SigninForm(forms.Form):
    email = forms.CharField(max_length=40, widget=(forms.EmailInput(attrs={'class': 'form-control'})))
    password = forms.CharField(max_length=25, widget=(forms.PasswordInput(attrs={'class': 'form-control'})))


class BookForm(ModelForm):
    class Meta:
        model = Books
        fields = ["book_name", "author", "category", "review", "copies"]
        widgets = {
            "book_name": forms.TextInput(attrs={'class': 'form-control'}),
            "author": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.TextInput(attrs={'class': 'form-control'}),
            "review": forms.Textarea(attrs={'class': 'form-control'}),
            "copies": forms.NumberInput(attrs={'class': 'form-control'}),
        }
