from importlib import import_module
import unittest


class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        flask_app = import_module('main')
        flask_app.app.testing = True
        self.app = flask_app.app.test_client()

    def test_http_post(self):
        name = 'QualityStart,Inc'
        actual = self.app.post('/output', data=dict(name=name))
        # print(actual.status_code)
        assert actual.status_code == 302
        assert 'Redirecting' in actual.get_data(as_text=True)

    def test_prg_pattern(self):
        name = 'QualityStart,Inc'
        actual = self.app.post('/output', data=dict(name=name), follow_redirects=True)
        assert actual.status_code == 200
        assert name in actual.get_data(as_text=True)
