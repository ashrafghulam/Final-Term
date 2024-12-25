import unittest
from app import app

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up the Flask test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_page(self):
        # Test the home route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Find Your Perfect Apartment', response.data)

    def test_login_page(self):
        # Test the login route
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_signup_page(self):
        # Test the signup route
        response = self.app.get('/signup')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Signup', response.data)

if __name__ == '__main__':
    unittest.main()
