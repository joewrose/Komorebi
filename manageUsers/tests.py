from django.test import TestCase
from manageUsers.forms import PostForm, EditForm


class PostFormTests(TestCase):
    def test_title_starting_lowercase(self):
        form = PostForm(data={"title": "a lowercase title"})

        self.assertEqual(
            form.errors["title"], ["Should start with an uppercase letter"]
        )
