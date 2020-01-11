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
        response = self.client.get('/music-info/techniques')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_both(self):
        response = self.client.get('/music-info/techniques/both')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_electric(self):
        response = self.client.get('/music-info/techniques/electric')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_acoustic(self):
        response = self.client.get('/music-info/techniques/acoustic')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_simple(self):
        response = self.client.get('/music-info/times/simple')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_compound(self):
        response = self.client.get('/music-info/times/compound')
        self.assertEqual(response.status_code, 200)

    def test_get_tech_complex(self):
        response = self.client.get('/music-info/times/complex')
        self.assertEqual(response.status_code, 200)

    def test_get_chord_random(self):
        response = self.client.get('/music-info/chords/random')
        self.assertEqual(response.status_code, 200)

    def test_get_scale_random(self):
        response = self.client.get('/music-info/scales/random')
        self.assertEqual(response.status_code, 200)

    def test_get_technique_random(self):
        response = self.client.get('/music-info/techniques/random')
        self.assertEqual(response.status_code, 200)

    def test_get_time_random(self):
        response = self.client.get('/music-info/times/random')
        self.assertEqual(response.status_code, 200)
