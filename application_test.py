"""
Module for testing the main application
"""
import unittest
from bs4 import BeautifulSoup
from application import application


class ApplicationTest(unittest.TestCase):
    """ Tests for application """

    def setUp(self):
        self.routes = [
            '/',
            '/states/texas',
            '/states/alaska',
            '/states/california',
            '/elections/general_election_2016',
            '/elections/texas_23_district_2016',
            '/elections/california_12_district_2016',
            '/candidates/gary_johnson',
            '/candidates/ted_cruz',
            '/candidates/nancy_pelosi',
            '/parties/libertarian',
            '/parties/democratic',
            '/parties/republican',
            '/states',
            '/elections',
            '/candidates',
            '/parties',
            '/about']

        self.html_docs = [
            'index.html',
            'states_texas.html',
            'states_alaska.html',
            'states_california.html',
            'elections_general_election_2016.html',
            'elections_texas_23_district_2016.html',
            'elections_california_12_district_2016.html',
            'candidates_gary_johnson.html',
            'candidates_ted_cruz.html',
            'candidates_nancy_pelosi.html',
            'parties_libertarian.html',
            'parties_democratic.html',
            'parties_republican.html',
            'states_model.html',
            'elections_model.html',
            'candidates_model.html',
            'parties_model.html',
            'about.html']

        self.app = application.test_client()
        self.app.testing = True

    def test_home_status(self):
        """ Test proper status code return """
        for route in self.routes:
            self.assertEqual(self.app.get(route).status_code, 200)

    def test_home_data(self):
        """ Test opening webpages """
        for index in range(len(self.routes)):
            fetched_page = self.app.get(self.routes[index])
            route = BeautifulSoup(fetched_page.data.decode(), 'html.parser')
            html_file = open('templates/' + self.html_docs[index])
            page = BeautifulSoup(html_file, 'html.parser')
        self.assertEqual(route.title.string, page.title.string)

    def test_empty_page(self):
        """ Ensure route does not return an empty page """
        for route in self.routes:
            page = self.app.get(route)
            self.assertNotEqual(page.data, '')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
