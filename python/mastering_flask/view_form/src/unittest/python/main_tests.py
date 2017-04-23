import json
import unittest
from main import app, db, User
from sqlalchemy import or_, not_


class MainTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_home(self):
        uri = '/'
        message = 'Hello Flask'
        rv = self.app.get(uri)
        self.assertEqual(message, rv.data.decode("utf-8"))

    def test_create_user(self):
        user = User('Ramesh')
        self.db.session.add(user)
        self.db.session.commit()

        # users = User.query.all()
        users = self.db.session.query(User).all()
        self.assertIn(user, users)

        self.db.session.delete(user)
        self.db.session.commit()

    def test_delete_user(self):
        user = User('Ramesh')
        self.db.session.add(user)
        self.db.session.commit()

        users = self.db.session.query(User).all()
        self.assertIn(user, users)

        self.db.session.delete(user)
        self.db.session.commit()

        users = User.query.all()
        self.assertNotIn(user, users)

    def test_read_user(self):
        demo_users = ['Ramesh', 'Khilan', 'Kaushik', 'Chaitali', 'Hardik', 'Komal', 'Paul', 'James', 'James']
        for u in demo_users:
            self.db.session.add(User(u))
        self.db.session.commit()

        users = self.db.session.query(User).limit(3).all()
        self.assertLessEqual(len(users), 3)

        users = self.db.session.query(User).order_by(User.username.desc()).all()
        demo_users.sort()
        demo_users.reverse()
        for i in range(len(demo_users)):
            self.assertEqual(users[i].username, demo_users[i])

        user = User.query.get(1)
        self.assertEqual(user.username, 'Ramesh')

        user = User.query.order_by(User.username.desc()).first()
        self.assertEqual(user.username, 'Ramesh')

        page = User.query.paginate(2, 3)
        self.assertLessEqual(len(page.items), 3)
        self.assertLessEqual(page.page, 2)
        self.assertTrue(page.has_next)
        self.assertTrue(page.has_prev)

        users = User.query.filter_by(username='James').all()
        self.assertNotEqual(len(users), 0)

        users = User.query.filter_by(username='Jame').all()
        self.assertEqual(len(users), 0)

        users = User.query.filter(
            User.id % 2 == 1,
            User.username.like('%k')
        ).all()
        for u in users:
            self.assertEqual(u.username[-1], 'k')

        users = User.query.filter(
            or_(User.id % 2 == 1,
                not_(User.username.like('%a%'))
                )
        )
        for u in users:
            print('id: {}, name: {}'.format(u.id, u.username))

        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_update_user(self):
        user = User('Ramesh')
        self.db.session.add(user)
        self.db.session.commit()

        User.query.filter_by(username='Ramesh').update({
            'password': 'test'
        })
        self.db.session.commit()

        user = User.query.filter_by(username='Ramesh').first()
        self.assertEqual(user.password, 'test')

        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_userapi_get(self):
        uri = '/users'
        rv = self.app.get(uri, follow_redirects=True)
        self.assertEqual(rv.data.decode("utf-8"), 'No data')
        self.assertEqual(rv.status_code, 200)

    def test_userapi_get_id(self):
        username = 'Ramesh'
        password = '1234'
        user = User(username, password)
        self.db.session.add(user)
        self.db.session.commit()

        uri = '/users/{}'.format(1)
        rv = self.app.get(uri, follow_redirects=True)
        message = 'Hello {}'.format(username)
        self.assertEqual(rv.data.decode('utf-8'), message)
        self.assertEqual(rv.status_code, 200)

        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_userapi_post(self):
        username = 'Ramesh'
        password = '1234'
        uri = '/users/'
        data = {'username': username, 'password': password}
        json_data = json.dumps(data)
        headers = {'content-type': 'application/json'}
        rv = self.app.post(uri, data=json_data, headers=headers)
        self.assertEqual(rv.status_code, 200)

        user = User.query.get(1)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_userapi_put(self):
        username = 'Ramesh'
        password = '1234'
        user = User(username, password)
        self.db.session.add(user)
        self.db.session.commit()

        new_username = 'James'
        new_password = 'abcde'
        uri = '/users/{}'.format(1)
        data = {'username': new_username, 'password': new_password}
        json_data = json.dumps(data)
        headers = {'content-type': 'application/json'}
        rv = self.app.put(uri, data=json_data, headers=headers)
        self.assertEqual(rv.status_code, 200)

        user = User.query.get(1)
        self.assertEqual(user.username, new_username)
        self.assertEqual(user.password, new_password)

        self.db.session.query(User).delete()
        self.db.session.commit()

    def test_userapi_delete(self):
        username = 'Ramesh'
        password = '1234'
        user = User(username, password)
        self.db.session.add(user)
        self.db.session.commit()

        user = User.query.get(1)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)

        uri = '/users/{}'.format(1)
        headers = {'content-type': 'application/json'}
        rv = self.app.delete(uri, headers=headers)
        self.assertEqual(rv.status_code, 200)

        user = User.query.get(1)
        self.assertIsNone(user)

        self.db.session.query(User).delete()
        self.db.session.commit()
