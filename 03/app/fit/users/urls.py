from django.urls import path
from .import views

from django.contrib.auth.decorators import login_required

import users.views as tracker_views

urlpatterns = [
    path('', views.home, name='homepage'),
    path("myprofile", views.myprofile, name="My Profile"),
    #path("physical", views.physical, name="physical"),
    path("create/", login_required(views.ExerciseCreateView.as_view()), name="exercise_create"),
    path("physical", login_required(views.ExerciseListView.as_view()), name="exercise_list"),
    path("<int:pk>/", login_required(views.ExerciseDetailView.as_view()), name="exercise_detail"),
    path("<int:pk>/update/", login_required(views.ExerciseUpdateView.as_view()), name="exercise_update"),
    path("<int:pk>/delete/", login_required(views.ExerciseDeleteView.as_view()), name="exercise_delete"),

    path("recipes/", login_required(views.RecipeListView.as_view()), name="recipe_list"),
    path("recipes/create", login_required(views.create), name="recipe_create"),
    path("recipes/<int:pk>/update/", login_required(views.update), name="recipe_update"),
    path("recipes/<int:pk>/delete/", login_required(views.recipe_delete), name="recipe_delete"),
    
    path("ingredient/create", login_required(views.IngredientCreateView.as_view()), name="ingredient_create"),
]