"""
Module for testing the main application
"""

from application import application
import unittest


class ApplicationTest(unittest.TestCase):

    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home_status(self):
        self.assertEqual(self.app.get('/').status_code, 200)

    def test_home_data(self):
        f = open('templates/index.html')
        self.assertEqual(f.read(), self.app.get('/').data.decode('utf-8'))

    def tearDown(self):
        pass

if __name__=='__main__':
    unittest.main()
