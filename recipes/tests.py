from django.http import response
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import Recipes

# Create your tests here.
class RecipesTestCase(TestCase):
    
    def setUp(self):
        # create user
        u1 = User.objects.create_user(username="user1",first_name="user1",password="user1password",email="user1@tse.com",)
        #crete recipes
        r = Recipes.objects.create(reName='rice omlet',ingredient='rice egg',solution='sol')
         
    def test_valid_recipes(self):
        """Check that Recipes is valid"""
        c = Recipes.objects.filter(pk = 1).exists()
        self.assertTrue(c)

    def test_invalid_recipes(self):
        """Check that Recipes is invalid"""
        c = Recipes.objects.filter(pk = 4).exists()
        self.assertFalse(c)
