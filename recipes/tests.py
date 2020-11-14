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
        self.user = User.objects.create_user(username="user1",first_name="user1",password="user1password",email="user1@tse.com",)
        #crete recipes
        self.recipe = Recipes.objects.create(reName='rice omlet',ingredient='rice egg',solution='sol')
        self.recipe.save()
        #create tag
        t = Tags.objects.create(tagName="home cook")
        
    def test_create_recipes(self):
        """Create recipes """
        self.assertEqual(self.recipe.reName, 'rice omlet')
        self.assertEqual(self.recipe.ingredient, 'rice egg')
        self.assertEqual(self.recipe.solution,'sol')

   
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
        
    def test_create_reName(self):
        r = Recipes.objects.create(reName="Tomyam")
        self.assertEqual(r.reName,"Tomyam")
        

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

    def test_str_recipes(self):
        """Test get object by reName"""
        r = Recipes.objects.create(reName='Tomyam',ingredient='lime',solution='Tom')
        self.assertEqual(r,Recipes.objects.get(reName="Tomyam"))
    
    def test_str_tags(self):
        """Test get object by tagName"""
        t = Tags.objects.create(tagName="Thai")
        self.assertEqual(t,Tags.objects.get(tagName="Thai"))

    def test_image(self):
        """Test image"""
        m1 = Recipes()
        m1.image = SimpleUploadedFile(name='test_image.jpg', content=open("static/menu/images/kapao.jpg", 'rb').read(), content_type='image/jpeg')
        user1=Recipes(reName='abc')
        user1.image.save('abc.png', File(open('static/menu/images/pancake.jpg', 'rb')))
        user1.save()
        self.assertEqual(Recipes.objects.count(), 2)