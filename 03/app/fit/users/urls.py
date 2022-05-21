from django.urls import path
from .import views

from django.contrib.auth.decorators import login_required

import users.views as tracker_views

urlpatterns = [
    path('', views.home, name='homepage'),
    path("myprofile", views.myprofile, name="My Profile"),
    #path("physical", views.physical, name="physical"),
    path("diet", views.diet, name="Diet"),
    path("create/", login_required(views.ExerciseCreateView.as_view()), name="exercise_create"),
    path("physical", login_required(views.ExerciseListView.as_view()), name="exercise_list"),
    path("<int:pk>/", login_required(views.ExerciseDetailView.as_view()), name="exercise_detail"),
    path("<int:pk>/update/", login_required(views.ExerciseUpdateView.as_view()), name="exercise_update"),
    path("<int:pk>/delete/", login_required(views.ExerciseDeleteView.as_view()), name="exercise_delete"),
    path("recipe/", login_required(views.RecipeListView.as_view()), name="recipe_list"),
    path("recipe/create", login_required(views.RecipeCreateView.as_view()), name="recipe_create"),
]