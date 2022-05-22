from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recipe, Ingredient
from django.forms.models import inlineformset_factory, modelformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *
from django.forms.models import BaseInlineFormSet


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


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name', 'recipe_description', 'calories', 'nutrients', 'prep_time']
    
    def isValid(self):
        return True


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'ingredient_calories', 'ingredient_nutrients', 'created_by']

IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, fields=('ingredient_name', 'ingredient_calories', 'ingredient_nutrients', 'created_by'), extra=0
)
