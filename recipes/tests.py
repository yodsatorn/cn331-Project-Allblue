from django.http import response
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import Recipes, Tags
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

# Create your tests here.
class RecipesTestCase(TestCase):

    def setUp(self):
        # create user
        u = User.objects.create_user(username="user1",first_name="user1",password="user1password",email="user1@tse.com",)
        #crete recipes
        r= Recipes.objects.create(reName='rice omlet',ingredient='rice egg',solution='sol')
        #create tag
        t = Tags.objects.create(tagName="home cook")
    
    
        
   #Test that it's valid recipe
    def test_valid_recipes(self):
        """Check that Recipes is valid"""
        try:
            c = Recipes.objects.get(pk=1)
        except Recipes.DoesNotExist:
            c = None
        if c == None:
            self.assertFalse(c==None)

        else:
            self.assertTrue(c.is_valid_Recipes())
        
    #Test that it's invalid recipe
    def test_invalid_recipes(self):
        """Check that Recipes is invalid"""
        try:
            c = Recipes.objects.get(pk=4)
        except Recipes.DoesNotExist:
            c = None
        if c == None:
            self.assertTrue(c==None)
        else:
            self.assertFalse(c.is_valid_Recipes())

    #Test that it's valid tag
    def test_valid_tag(self):
        """Check that Tags is valid"""
        try:
            c = Tags.objects.get(pk=1)
        except Tags.DoesNotExist:
            c = None
        if c == None:
            self.assertFalse(c==None)
        else:    
            self.assertTrue(c.is_valid_Tags())

    #Test that it's invalid tag   
    def test_invalid_tag(self):
        """Check that Tags is invalid"""
        try:
            c = Tags.objects.get(pk=4)
        except Tags.DoesNotExist:
            c = None
        if c == None:
            self.assertTrue(c==None)
        else:
            self.assertFalse(c.is_valid_Tags())


    def test_valid_str_recipes(self):
        """Test valid string of recipe's name"""
        r = Recipes.objects.create(reName='Tomyam',ingredient='lime',solution='Tom')
        self.assertEqual(r,Recipes.objects.get(reName="Tomyam"))
    
    def test_invalid_str_recipes(self):
        """Test invalid string of recipe's name"""
        r = Recipes.objects.create(reName='Tomyam',ingredient='lime',solution='Tom')
        self.assertNotEqual(r,Recipes.objects.get(reName="rice omlet"))
    
    def test_valid_str_tags(self):
        """Test valid string of tag's name"""
        t = Tags.objects.create(tagName="Thai")
        self.assertEqual(t,Tags.objects.get(tagName="Thai"))

    def test_invalid_str_tags(self):
        """Test invalid string of tag's name"""
        t = Tags.objects.create(tagName="Thai")
        self.assertNotEqual(t,Tags.objects.get(tagName="home cook"))


    def test_image(self):
        """Test image"""
        m1 = Recipes()
        m1.image = SimpleUploadedFile(name='test_image.jpg', content=open("static/menu/images/kapao.jpg", 'rb').read(), content_type='image/jpeg')
        user1=Recipes(reName='abc')
        user1.image.save('abc.png', File(open('static/menu/images/pancake.jpg', 'rb')))
        user1.save()
        self.assertEqual(Recipes.objects.count(), 2)