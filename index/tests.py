from django.test import Client,TestCase
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
class indexTestCase(TestCase):
    
    def setUp(self):
        # create admin 
        admin1 = User.objects.create_superuser(username = 'admin1',email = 'admin@tse.com',password = 'admin1password')

        # create user
        u1 = User.objects.create_user(username="user1",first_name="user1",password="user1password",email="user1@tse.com")
    
    # happy path login page
    def test_login_page(self):
        c = Client()
        #response_1 =  c.login(username="user1",password="admin1password")
        response = c.post('/login',username="user1",password="user1password")
        self.assertEqual(response.status_code,200)
        self.assertTrue(response)

    # sad path login page
    def test_fail_login_page(self):
        c = Client()
        #response_1 = c.login(username = "user1",password="user1password")
        response = c.post('/login',username = "user1", password="admin1password")
        self.assertNotEqual(response.status_code,200)
        self.assertFalse(response)