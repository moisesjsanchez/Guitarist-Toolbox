import unittest
from Guitarist_Toolbox import create_app
from Guitarist_Toolbox.config import TestConfig


class APITestCase(unittest.TestCase):
    '''
    Testing API views
    '''
    # setup

    def setUp(self):
        self.app = create_app(config_class=TestConfig)
        self.client = self.app.test_client()

    # testing API status codes
    def test_get_all(self):
        response = self.client.get('/music-info/all')
        self.assertEqual(response.status_code, 200)

    def test_get_chords(self):
        response = self.client.get('/music-info/chords')
        self.assertEqual(response.status_code, 200)

    def test_get_scales(self):
        response = self.client.get('/music-info/scales')
        self.assertEqual(response.status_code, 200)

    def test_get_technique(self):
        response = self.client.get('/music-info/technique')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_both(self):
        response = self.client.get('/music-info/technique/tech_type/both')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_electric(self):
        response = self.client.get('/music-info/tech_type/electric')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_acoustic(self):
        response = self.client.get('/music-info/tech_type/acoustic')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_simple(self):
        response = self.client.get('/music-info/time/time_type/simple')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_compound(self):
        response = self.client.get('/music-info/time/time_type/compound')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_complex(self):
        response = self.client.get('/music-info/time/time_type/complex')
        self.assertEqual(response.status_code, 200)
