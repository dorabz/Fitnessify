from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Recipe, Ingredient
from django.forms.models import inlineformset_factory


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
    
    def is_valid(self):
        calories = 0
        count_name = ''
        try:
            for value in self.data:
                if value.endswith('TOTAL_FORMS'):
                    count_name = value
            # print(count_name)
            for i in range(int(self.data[count_name])):
                calories += int(self.data[f'ingredient-{i}-ingredient_calories'])
            return calories <= int(self.data['calories'])
        except:
            return False


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['ingredient_name', 'ingredient_calories', 'ingredient_nutrients']


IngredientFormSet = inlineformset_factory(
    Recipe, Ingredient, fields=('ingredient_name', 'ingredient_calories', 'ingredient_nutrients'), extra=0
)
