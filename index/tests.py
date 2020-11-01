from django.http import response
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError


# Create your tests here.
class indexTestCase(TestCase):
    def setUp(self):
        # create admin
        admin1 = User.objects.create_superuser(
            username="admin1", email="admin@tse.com", password="admin1password"
        )

        # create user
        u1 = User.objects.create_user(
            username="user1",
            first_name="user1",
            password="user1password",
            email="user1@tse.com",
        )

    # happy path login page
    def test_success_login(self):
        c = Client()
        response = c.post(
            "/login/", {"username": "user1", "password": "user1password"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response)
        # check authenticate
        user = authenticate(username="user1", password="user1password")
        self.assertTrue((user is not None) and user.is_authenticated)

    # sad path login page
    def test_fail_login(self):
        c = Client()
        response = c.post(
            "/login", {"username": "user1", "password": "admin1password"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        # TO DO List ^^^^^ check website login fail
        # check authenticate
        user = authenticate(username="user1", password="admin1password")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_error_message(self):
        """
        Test error_message for login page if authenticate() return False (User not in database) error_message will be sent to inform Client.
        """
        c = Client()
        response = c.post('/login/', {"username":"wronguser","password":"withworngpassword"}, follow=True)
        self.assertTrue(response.context['error_message'] == 'Invalid Credentials')

    def test_register_unique_email(self):
        c = Client()
        response = c.post('/register/',{'username': 'user2',
        'password': 'user2password',
        'email': 'user1@tse.com' # Same email as user1
        })

        self.assertRaisesMessage(IntegrityError, 'Email was taken.')

    def test_register_unique_username(self):
        c = Client()
        response = c.post('/register/',{'username': 'user1', # Same username as user1
        'password': 'user2password',
        'email': 'user2@tse.com'
        })

        self.assertRaisesMessage(IntegrityError, 'Username was taken.')
