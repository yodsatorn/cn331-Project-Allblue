from django.http import response, HttpResponse, HttpResponseRedirect
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.apps import apps
from index.apps import IndexConfig
from recipes.urls import urlpatterns


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
        """
        Test login Success
        """
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
        """
        Test Login fail
        """
        c = Client()
        response = c.post(
            "/login", {"username": "user1", "password": "admin1password"}, follow=True
        )
        self.assertEqual(response.status_code, 200)
        # check authenticate
        user = authenticate(username="user1", password="admin1password")
        self.assertFalse(user is not None and user.is_authenticated)

    def test_login_error_message(self):
        """
        Test error_message for login page if authenticate() return False (User not in database) error_message will be sent to inform Client.
        """
        c = Client()
        response = c.post(
            "/login/",
            {"username": "wronguser", "password": "withworngpassword"},
            follow=True,
        )
        self.assertTrue(
            response.context["error_message"] == "Invalid Credentials")

    def test_register_success(self):
        """
        Test user can register success
        """
        c = Client()
        response = c.post(
            "/register/",
            {
                "username": "user2",
                "password": "user2password",
                "email": "user2@tse.com",
            }, follow=True
        )
        response1 = c.get('/register/')
        self.assertEqual(response1.status_code, 200)
        self.assertTemplateUsed(response1, 'register.html')

    def test_register_unique_email(self):
        """
        Test Unique email when email was taken IntegrityError will raise with message 'Email was taken.'
        """
        c = Client()
        response = c.post(
            "/register/",
            {
                "username": "user2",
                "password": "user2password",
                "email": "user1@tse.com",  # Same email as user1
            },
        )

        self.assertRaisesMessage(IntegrityError, "Email was taken.")

    def test_register_unique_username(self):
        """
        Test Unique Username when Username was taken IntegrityError will raise with message 'Username was taken.'
        """
        c = Client()
        response = c.post(
            "/register/",
            {
                "username": "user1",  # Same username as user1
                "password": "user2password",
                "email": "user2@tse.com",
            },
        )

        self.assertRaisesMessage(IntegrityError, "Username was taken.")

    # test log out
    def test_Logout(self):
        """
        Test log out
        """
        # log in
        c = Client()
        response = c.post(
            "/login/",
            {"username": "user1",
             "password": "user1password"
             },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        # Log out
        self.client.logout()
        self.client.get('/logout/')
        # Check response code
        response = self.client.get("")
        self.assertEquals(response.status_code, 200)

    # Test profile page
    def test_access_profile_page(self):
        """
        Test access to profile's page
        """
        # log in
        c = Client()
        response = c.post(
            "/login/", {"username": "user1", "password": "user1password"}, follow=True
        )
        response = c.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_fail_profile_page(self):
        """
        Test failure access to profile's page.
        """
        c = Client()
        response = c.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    # test apps index

    def test_apps(self):
        """
        Test app index
        """
        self.assertEqual(IndexConfig.name, 'index')
        self.assertEqual(apps.get_app_config('index').name, 'index')

    # Test about's page
    def test_about_page(self):
        """
        Test about page
        """
        c = Client()
        response = c.get('/about/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('about.html')

    # Test edit profile
    def test_edit_profile(self):
        """
        Test edit profile
        """
        c = Client()
        response = c.post(
            "/login/", {"username": "user1", "password": "user1password"}, follow=True
        )
        response = c.post('/profile/edit/',
                          {
                              'password': 'user1password2',
                              'first_name': 'Jack',
                              'last_name': 'Sparelow',
                              'username': 'user1',
                              'email': 'user1@tse.com'},
                          )
        response = c.post(
            "/login/", {"username": "user1", "password": "user1password2"}, follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_fail_edit_profile(self):
        """
        Test fail edit profile
        """
        c = Client()
        self.client.login(username='user1', password='user1password')
        response = c.get('/profile/edit/')
        self.assertEqual(response.status_code, 200)
