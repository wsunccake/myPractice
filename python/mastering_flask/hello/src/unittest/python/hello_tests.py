import unittest
import hello


class HelloTest(unittest.TestCase):
    def setUp(self):
        self.app = hello.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        uri = '/'
        message = 'Hello Flask'
        rv = self.app.get(uri)
        self.assertEqual(message, rv.data.decode("utf-8"))

