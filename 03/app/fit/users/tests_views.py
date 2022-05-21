from django.test import TestCase
from django.urls import reverse


from django.contrib.auth.models import User 
from .models import Exercise
from .views import ExerciseListView


# unit test -- test  VIEWS - Exercise

class ExerciseListViewTest(TestCase):
    @classmethod
    def setUpTestData(self):

        test_user1 = User.objects.create_user(username='testuser1', password='1X<ISRUkw+tuK')

        test_user1.save()

        # Create 15 exercises for pagination tests
        number_of_exercises = 15
        self.u2 = User.objects.create(username='hrvoje')

        for exercise_id in range(number_of_exercises):
            Exercise.objects.create(
                exercise_name=f'Sklekovi {exercise_id}',
                calories_burned=500, sets=2, reps=10, weight=2, created_by =test_user1
            )

    def test_logged_in_uses_correct_template(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('exercise_list'))

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'testuser1')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Check we used correct template
        self.assertTemplateUsed(response, 'users/exercise_list.html')

        self.assertTrue(response.context['is_paginated'] == True)
     

    def test_pagination_is_ten(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('exercise_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        #self.assertEqual(len(response.context['exercise_list']), 10)

    def test_lists_all_exercises(self):
        login = self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        # Get second page and confirm it has (exactly) remaining 5 items
        response = self.client.get(reverse('exercise_list')+'?page=2')
        self.assertEqual(response.status_code, 200)
        self.assertTrue('is_paginated' in response.context)
        self.assertTrue(response.context['is_paginated'] == True)
        #self.assertEqual(len(response.context['exercise_list']), 5)