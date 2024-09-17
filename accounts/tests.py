from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class CelebrantRegistrationTest(TestCase):
    def test_celebrant_registration_success(self):
        data = {
            'username': 'celebrant_test',
            'email': 'celebrant@test.com',
            'password1': 'SecurePassword123',
            'password2': 'SecurePassword123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)
        user_exists = User.objects.filter(username='celebrant_test').exists()
        self.assertTrue(user_exists)

    def test_celebrant_registration_failure_missing_field(self):
        data = {
            'username': 'celebrant_test',
            'email': '',  # Missing email
            'password1': 'SecurePassword123',
            'password2': 'SecurePassword123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Form should re-render on failure
        user_exists = User.objects.filter(username='celebrant_test').exists()
        self.assertFalse(user_exists)

    def test_celebrant_registration_failure_duplicate_email(self):
        User.objects.create_user(username='existing_celebrant', email='existing@test.com', password='password123')
        data = {
            'username': 'new_celebrant',
            'email': 'existing@test.com',  # Duplicate email
            'password1': 'SecurePassword123',
            'password2': 'SecurePassword123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 200)  # Form should re-render on failure
        user_exists = User.objects.filter(username='new_celebrant').exists()
        self.assertFalse(user_exists)
