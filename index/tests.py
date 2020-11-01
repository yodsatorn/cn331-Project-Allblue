from django.test import Client,TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class indexTestCase(TestCase):
    
    def setUp(self):
       
        #create user and admin 
        admin_1 = User.objects.create_superuser(username = 'admin',email = 'admin@tse.com',password = '12345')
        u1 = User.objects.create_user(username="starter",first_name="Yodsatorn",password="12345",email="yod@tse.com")
    #happy path login page
    def test_login_page(self):
        c = Client()
        response_1 =  c.login(username="starter",password="12345")
        response = c.get('/login')
        self.assertEqual(response.status_code,200)
        self.assertTrue(response_1)
    def test_not_login_page(self):
        c = Client()
        response_1 = c.login(username = "starter",password="54321")
        response = c.get('/login')
        self.assertNotEqual(response.status_code,200)
        self.assertFalse(response_1)