import unittest
import main
import json


class HelloTest(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()

    def tearDown(self):
        pass

    def test_home(self):
        uri = '/'
        message = 'Hello Flask'
        rv = self.app.get(uri)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_say(self):
        user = 'flask'
        uri = '/say/{}'.format(user)
        message = 'Hello {}'.format(user)
        rv = self.app.get(uri)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_ask(self):
        user = 'flask'
        uri = '/ask'
        param = {'user': user}
        message = 'Hello {}'.format(user)
        rv = self.app.get(uri, query_string=param)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_post_1(self):
        user = 'flask'
        uri = '/tell'
        data = {'user': user}
        header = {'Content-Type': 'application/x-www-form-urlencoded'}
        message = 'Hello {}'.format(user)
        rv = self.app.post(uri, data=data, headers=header)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_post_0(self):
        user = 'flask'
        uri = '/tell'
        data = {'user': user}
        message = 'Hello {}'.format(user)
        rv = self.app.post(uri, data=data)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_post_1(self):
        user = 'flask'
        uri = '/tell'
        data = {'user': user}
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        message = 'Hello {}'.format(user)
        rv = self.app.post(uri, data=data, headers=headers)
        self.assertEqual(message, rv.data.decode('utf-8'))

    def test_post_2(self):
        user = 'flask'
        uri = '/tell'
        data = json.dumps({'user': user})
        headers = {'content-type': 'application/json'}
        rv = self.app.post(uri, data=data, headers=headers)
        self.assertEqual(user, json.loads(rv.data.decode('utf-8'))['user'])
