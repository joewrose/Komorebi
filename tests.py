from django.test import TestCase

# Create your tests here.
from multiprocessing.connection import Client

from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from django.urls import reverse


class Test(TestCase):

    def test_all_views_for_not_logged_in_users(self):
        """
        Checks if pages and restricted images are displayed correctly for a user that is not logged in
        """
        response = self.client.get(reverse('manageUsers:home'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('manageUsers:login'))
        self.assertEqual(response.status_code, 200)
        # user gets redirected to login for these restricted pages that require logging in
        response = self.client.get(reverse('manageUsers:create'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('manageUsers:edit'))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('manageUsers:logout'))
        self.assertEqual(response.status_code, 302)

    def test_all_views_for_logged_in_users(self):
        # send login data
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        self.usertest = User.objects.create_user(**self.credentials)
        c = Client()
        self.credentials.update({'Login': 'Login'})
        response = c.post(reverse('manageUsers:login'), self.credentials, follow=True)
        # should be logged in now
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'].is_authenticated, True)
        self.assertEqual(response.status_code, 200)
        # when user is logged in he is able to acess the restricted pages that he wasnt able to acess when he
        # wasnt logged in
        response = c.get(reverse('manageImages:addimage'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('manageImages:like_picture'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('manageImages:dislike_picture'))
        self.assertEqual(response.status_code, 200)
        response = c.get(reverse('manageUsers:edit'))
        self.assertEqual(response.status_code, 302)
        response = c.get(reverse('manageUsers:logout'))
        self.assertEqual(response.status_code, 302)
