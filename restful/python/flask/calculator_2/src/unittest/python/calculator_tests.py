import unittest
from calculator import create_app

import json


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        app = create_app()
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_main(self):
        uri = '/'
        message = 'Hello Flask'

        rv = self.app.get(uri)

        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_base_sqrt(self):
        uri = '/sqrt' + '/1'
        data = {'function': 'sqrt',
                'input': ['1'],
                'output': ['1.0']}
        json_data = json.dumps(data, sort_keys=True)

        rv = self.app.get(uri)

        self.assertEqual(json_data, rv.data.decode('utf-8'))

    def test_base_power(self):
        uri = '/power?base={}&exponent={}'.format(1, 2)
        data = {'function': 'power',
                'input': ['1', '2'],
                'output': ['1.0']}
        json_data = json.dumps(data, sort_keys=True)

        rv = self.app.get(uri)

        self.assertEqual(json_data, rv.data.decode('utf-8'))
