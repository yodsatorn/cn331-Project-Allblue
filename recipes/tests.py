from django.http import response
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import Recipes, Tags
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import ImageField

# Create your tests here.
class RecipesTestCase(TestCase):

    def setUp(self):
        # create user
        user1 = User.objects.create_user(username="user1",first_name="user1",password="user1password",email="user1@tse.com")
        user2 = User.objects.create_user(username="user2",first_name="user2",password="user2password",email="user2@tse.com")
        #crete recipes
        recipe1 = Recipes.objects.create(reName='rice omlet',ingredient='rice egg',solution='sol')
        recipe2 = Recipes.objects.create(reName = 'steak',ingredient = 'pork',solution = 'grill')
        recipe3 =  Recipes.objects.create(reName  = 'cheese cake',ingredient = 'cheese,milk',solution = 'baked')
        #create tag
        tag1 = Tags.objects.create(tagName= "home cook")
        tag2 = Tags.objects.create(tagName = "Thai food")
        tag3 = Tags.objects.create(tagName  = "Chinese food")


    def test_valid_str_recipes(self):
        """Test valid string of recipe's name"""
        r = Recipes.objects.create(reName='Tomyam',ingredient='lime',solution='Tom')
        self.assertEqual(r.__str__(),Recipes.objects.get(reName="Tomyam").__str__())
    
    def test_invalid_str_recipes(self):
        """Test invalid string of recipe's name"""
        r = Recipes.objects.create(reName='Tomyam',ingredient='lime',solution='Tom')
        self.assertNotEqual(r.__str__(),Recipes.objects.get(reName="rice omlet".__str__()))
    
    def test_valid_str_tags(self):
        """Test valid string of tag's name"""
        t = Tags.objects.create(tagName="Thai")
        self.assertEqual(t.__str__(),Tags.objects.get(tagName="Thai").__str__())

    def test_invalid_str_tags(self):
        """Test invalid string of tag's name"""
        t = Tags.objects.create(tagName="Thai")
        self.assertNotEqual(t.__str__(),Tags.objects.get(tagName="home cook").__str__())


    def test_image_field_type(self):
        """Test image field type"""
        image = Recipes._meta.get_field('image')
        self.assertTrue(isinstance(image,ImageField))


    def test_str_type_field(self):
        """Test that it's string type field"""
        recipe1 = Recipes.objects.get(pk=1)
        self.assertIsInstance(recipe1.reName,str)
        self.assertIsInstance(recipe1.ingredient,str)
        self.assertIsInstance(recipe1.solution,str)