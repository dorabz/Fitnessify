from django.contrib import admin
from .models import Profile, Exercise, Recipe, Ingredient
# Register your models here.


admin.site.register(Profile)
admin.site.register(Exercise)
admin.site.register(Recipe)
admin.site.register(Ingredient)