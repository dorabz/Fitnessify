from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recipe, Ingredient
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


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
        fields = ['recipe_name', 'recipe_description']
    
    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('recipe_name'),
                Field('recipe_description'),
                Fieldset('Add ingredients',
                    Formset('ingredients')),
                Field('ingredient_name'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'save')),
                )
            )

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'ingredient_calories']

IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, form=IngredientForm,
    fields=['ingredient_name', 'ingredient_calories'], extra=1, can_delete=True
)