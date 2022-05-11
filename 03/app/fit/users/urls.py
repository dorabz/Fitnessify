from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path("myprofile", views.myprofile, name="My Profile"),
    path("physical", views.physical, name="Physical Activites"),
    path("diet", views.diet, name="Diet"),
]