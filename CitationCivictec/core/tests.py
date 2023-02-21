from django.test import TestCase
from .models import Officer
from django.contrib.auth.models import User

# Create your tests here.
class OfficerTestCase(TestCase):
    """Proof that the official profile has been created and linked to the user correctly."""
    
    def setUp(self):
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exist(self):
        existsOfficer = Officer.objects.filter(user__username='test').exists()
        self.assertEqual(existsOfficer, True)