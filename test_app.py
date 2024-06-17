import unittest
from flask_testing import TestCase
from app import app

class TestAPI(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_get_users(self):
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(len(data), 5)
        for user in data:
            self.assertIn('username', user)
            self.assertIn('email', user)
            self.assertIn('is_active', user)

if __name__ == '__main__':
    unittest.main()
