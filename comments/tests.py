from django.http import response
from django.apps import apps
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from comments.apps import CommentsConfig

# Create your tests here.
class CommentsTestCase(TestCase):
    """#test apps comments"""
    def test_apps(self):
        self.assertEqual(CommentsConfig.name, 'comments')
        self.assertEqual(apps.get_app_config('comments').name, 'comments')