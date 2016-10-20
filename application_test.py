""" Phase 1 Test Bed """
# pylint: disable=unused-import
# pylint: disable=duplicate-code
import os
import unittest
import tempfile
from application import application


class ApplicationTest(unittest.TestCase):
    """ Tests for application """

    def setUp(self):
        self.app = application.test_client()
        self.app.testing = True

    def test_home_status(self):
        """ Test proper status code return """
        self.assertEqual(self.app.get('/').status_code, 200)

    def test_home_data(self):
        """ Test opening webpages """
        page = open('templates/index.html')
        self.assertEqual(page.read(), self.app.get('/').data.decode('utf-8'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
