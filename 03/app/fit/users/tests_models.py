from django.test import TestCase
from django.urls import reverse


# unit and integration test

# unit test -- test MODEL - Exercise

from .models import Exercise
from django.contrib.auth.models import User 


class ExerciseModelTest(TestCase):
    @classmethod
    def setUpTestData(self):
        # Set up non-modified objects used by all test methods
        self.u1 = User.objects.create(username='user1')
        self.ex1=Exercise.objects.create(exercise_name='sklekovi', calories_burned=500, sets=2, reps=10, weight=2, created_by =self.u1)

    def tearDown(self):
        self.ex1.delete()
        self.u1.delete()

    def test_exercise_name_label(self):
        exercise = Exercise.objects.get(id=1)
        field_label = exercise._meta.get_field('exercise_name').verbose_name
        self.assertEqual(field_label, 'exercise name')

    def test_calories_burned_label(self):
        exercise = Exercise.objects.get(id=1)
        field_label = exercise._meta.get_field('calories_burned').verbose_name
        self.assertEqual(field_label, 'calories burned')

    def test_exercise_name_max_length(self):
        exercise = Exercise.objects.get(id=1)
        max_length = exercise._meta.get_field('exercise_name').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_exercise_name(self):
        exercise = Exercise.objects.get(id=1)
        expected_object_name = f'{exercise.exercise_name}'
        self.assertEqual(str(exercise), expected_object_name)

