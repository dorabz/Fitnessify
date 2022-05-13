from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    name = models.TextField(max_length=100, null=True, blank=True)
    last_name = models.TextField(max_length=100)
    email = models.EmailField(max_length=200, default="email@domain.com")
    age = models.IntegerField(null=True, blank=True)
    calories_food = models.IntegerField(null=True, blank=True)
    calories_exercise = models.IntegerField(null=True, blank=True)
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.user.username


class Exercise(models.Model):
    exercise_name = models.CharField(max_length=100)
    calories_burned = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    performed = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.exercise_name  