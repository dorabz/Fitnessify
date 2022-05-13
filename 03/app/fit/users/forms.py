from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']


class ProfileUpdateForm(forms.ModelForm):

    name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    last_name = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    email = forms.EmailField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    age = forms.IntegerField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    calories_food = forms.IntegerField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    calories_exercise = forms.IntegerField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 1}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['name', 'last_name', 'email', 'age', 'calories_food', 'calories_exercise', 'bio']

