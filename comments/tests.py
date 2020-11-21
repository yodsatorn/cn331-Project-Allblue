from django.http import response
from django.apps import apps
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from comments.apps import CommentsConfig
from .models import  Comments
from recipes.models import Tags , Recipes

# Create your tests here.
class CommentsTestCase(TestCase):

    def setUp(self):
        # create user
        user1 = User.objects.create_user(
            username="user1", first_name="user1", password="user1password", email="user1@tse.com")
        user2 = User.objects.create_user(
            username="user2", first_name="user2", password="user2password", email="user2@tse.com")
        # crete recipes
        recipe1 = Recipes.objects.create(
            reName='rice omlet', ingredient='rice egg', solution='sol')
        recipe2 = Recipes.objects.create(
            reName='steak', ingredient='pork', solution='grill')
        recipe3 = Recipes.objects.create(
            reName='Cheese cake', ingredient='cheese,milk', solution='baked')
        # create tag
        tag1 = Tags.objects.create(tagName="home cook")
        tag2 = Tags.objects.create(tagName="Thai food")
        tag3 = Tags.objects.create(tagName="Chinese food")

        # create comment
        comment1 = Comments.objects.create(body = 'Great!!',username = 'user1')
        comment2 =Comments.objects.create(body = "Oh it's look delicious", username = 'user2')

    
    def test_apps(self):
        """test apps comments"""
        self.assertEqual(CommentsConfig.name, 'comments')
        self.assertEqual(apps.get_app_config('comments').name, 'comments')

    def test_comments_str(self):
        """Test comment str"""
        comment = Comments.objects.get(pk=1)
        self.assertTrue('User: 1 | Body: Great!!',comment.__str__())

    