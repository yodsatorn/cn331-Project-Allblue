from django.http import response
from django.apps import apps
from django.test import Client, TestCase ,RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError
from .models import Recipes, Tags
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db.models import ImageField
from recipes.apps import RecipesConfig
from django.shortcuts import redirect
from comments.models import Comments



# Create your tests here.


class RecipesTestCase(TestCase):

    def setUp(self):
       
        # create user
        user1 = User.objects.create_user(
            username="user1", first_name="user1", password="user1password", email="user1@tse.com")
        user2 = User.objects.create_user(
            username="user2", first_name="user2", password="user2password", email="user2@tse.com")
        
        # crete recipes
        recipe1 = Recipes.objects.create(reName='rice omlet', ingredient='rice egg', solution='sol')
        recipe2 = Recipes.objects.create(reName='steak', ingredient='pork', solution='grill')
        recipe3 = Recipes.objects.create(reName='Cheese cake', ingredient='cheese,milk', solution = 'baked')
        
        # create tag
        tag1 = Tags.objects.create(tagName="home cook")
        tag2 = Tags.objects.create(tagName="Thai food")
        tag3 = Tags.objects.create(tagName="Chinese food")
        
        # recipe3 was create by user2
        recipe3.user.add(user2)
        
        # tag3 was tag by recipe3
        recipe3.tag.add(tag3)

    # Test string
    def test_valid_str_recipes(self):
        """
        Test valid string of recipe's name
        """
        r = Recipes.objects.create(
            reName='Tomyam', ingredient='lime', solution='Tom')
        self.assertEqual(r.__str__(), Recipes.objects.get(
            reName="Tomyam").__str__())

    # Test string
    def test_invalid_str_recipes(self):
        """
        Test invalid string of recipe's name
        """
        r = Recipes.objects.create(
            reName='Tomyam', ingredient='lime', solution='Tom')
        self.assertNotEqual(r.__str__(), Recipes.objects.get(
            reName="rice omlet".__str__()))

    # Test string
    def test_valid_str_tags(self):
        """
        Test valid string of tag's name
        """
        t = Tags.objects.create(tagName="Thai")
        self.assertEqual(t.__str__(), Tags.objects.get(
            tagName="Thai").__str__())

    # Test string
    def test_invalid_str_tags(self):
        """
        Test invalid string of tag's name
        """
        t = Tags.objects.create(tagName="Thai")
        self.assertNotEqual(t.__str__(), Tags.objects.get(
            tagName="home cook").__str__())

    # Test that this field is a image type.
    def test_image_field_type(self):
        """
        Test image field type
        """
        image = Recipes._meta.get_field('image')
        self.assertTrue(isinstance(image, ImageField))

    def test_str_type_field(self):
        """
        Test that it's string type field
        """
        recipe1 = Recipes.objects.get(pk=1)
        self.assertIsInstance(recipe1.reName, str)
        self.assertIsInstance(recipe1.ingredient, str)
        self.assertIsInstance(recipe1.solution, str)

    # Test valid recipe.
    def test_valid_recipe(self):
        """
        Test valid recipe.
        """
        r = Recipes.objects.get(pk=1)
        self.assertTrue(r.is_valid_Recipes())

    # Test valid tags.
    def test_valid_tag(self):
        """
        Test valid tag.
        """
        t = Tags.objects.get(pk=1)
        self.assertTrue(t.is_valid_Tags())

    # Test access to menu's page without login
    def test_access_menu_page_withOut_login(self):
        """
        Test access to menu's page without login
        """
        c = Client()
        response = c.get('/recipes/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, 'layout-topnavRe.html')
        self.assertEqual(response.context['menu'].count(), 3)

    # Test access to menu's page with login
    def test_access_menu_with_login(self):
        """
        Test access to menu's page with login
        """
        c = Client()
        # user login
        response = c.post(
            '/login/', {'username': 'user1', 'password': 'user1password'}, follow=True
        )
        response = c.get('/recipes/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')
        self.assertTemplateUsed(response, 'layout-topnavRe.html')
        self.assertEqual(response.context['menu'].count(), 3)

    # Test access to menu's page by search bar
    def test_access_menu_by_search(self):
        """
        Test access to menu's page by search bar
        """
        c = Client()
        reponse = c.post(
            '/menu/', {'q': 'steak', 'search_option': 'by_name'}, follow=True
        )
        response1 = c.get('/recipes/menu/')
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'menu.html')
        self.assertTemplateUsed(response1, 'layout-topnavRe.html')

    def test_search(self):
        """
        Test search
        """
        c = Client()
        response = c.post(reverse('index'), data={
                          'q': 'steak', 'search_option': 'by_name'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # Test that user can access recipe's page
    def test_access_recipes_page(self):
        """
        Test that users can access recipes page
        """
        # user1 login
        self.client.login(username='user1', password='user1password')
        # user1 want to checkout content in Recipe that has id = 3
        recipe = Recipes.objects.get(pk=3)
        response = self.client.get(f'/recipes/view/recipe/{recipe.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewrecipe.html')
        self.assertTemplateUsed(response, 'layout-topnavRe.html')

    # Test apps recipes
    def test_apps(self):
        """
        Test app recipes
        """
        self.assertEqual(RecipesConfig.name, 'recipes')
        self.assertEqual(apps.get_app_config('recipes').name, 'recipes')

    # Test recipe user
    def test_recipe_user_view(self):
        """
        Test that users can access their recipe
        """
        # user1 login
        self.client.login(username='user1', password='user1password')
        # user1 want to checkout content in Recipe that has id = 3
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=2)
        c = Client()
        response = self.client.get(f'/recipes/view/myrecipe/{u.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')
        self.assertTemplateUsed(response, 'layout-topnavRe.html')

    # Test delete recipe
    def test_delete_recipe(self):
        """
        Test delete recipe
        """
        # user1 login
        c = Client()
        response = c.post(
            "/login/", {"username": "user1", "password": "user1password"}, follow=True
        )
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=2)
        response = c.get(f'/recipes/view/myrecipe/{u.id}')
        response = c.get(f'/recipes/delete/{recipe.id}', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_recipes.html')
        self.assertTemplateUsed(response, 'layout-topnavRe.html')

    #Test tag view recipes
    def test_tag_view_reciep(self):
        """
        Test view menu by tag
        """
        c = Client()
        t = Tags.objects.get(pk=3)
        response = c.get(f'/recipes/menu/tag/{t.id}' , follow = True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu.html')


    def test_voteUp_1(self):
        """
        Test vote up which user never vote any voteUp or voteDown
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        response = c.get(f'/recipes/view/recipe/voteup/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')

    def test_voteUp_2(self):
        """
        Test vote up which user has already voted down
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=1)
        recipe.voteDown.add(u) # user1 has voted down before user1 voted up.
        response = c.get(f'/recipes/view/recipe/voteup/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')

    def test_voteUp_3(self):
        """
        Test vote up which user has already voted up
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=1)
        recipe.voteUp.add(u) # user1 has voted up before user1 voted up again.
        response = c.get(f'/recipes/view/recipe/voteup/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')

    def test_voteDown_1(self):
        """
        Test vote down which user never vote any voteUp or voteDown
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        response = c.get(f'/recipes/view/recipe/votedown/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')
        
    def test_voteDown_2(self):
        """
        Test vote up which user has already voted up
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=1)
        recipe.voteUp.add(u) # user1 has voted up before user1 voted down.
        response = c.get(f'/recipes/view/recipe/votedown/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')
    
    def test_voteDown_3(self):
        """
        Test vote up which user has already voted down
        """
        c = Client()
        # user1 login
        c.login(username='user1', password='user1password')
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)
        recipe = Recipes.objects.get(pk=3)
        u = User.objects.get(pk=1)
        recipe.voteDown.add(u) # user1 has voted down before user1 voted down again.
        response = c.get(f'/recipes/view/recipe/votedown/{recipe.id}' , follow =True)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, 'viewrecipe.html')


