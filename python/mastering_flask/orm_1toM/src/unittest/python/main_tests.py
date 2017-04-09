import unittest
from main import app, db, User, Post
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

    def test_post(self):
        user = User('Ramesh')
        user.id = 1
        self.db.session.add(user)

        post = Post('Post Title')
        post.user_id = user.id
        self.db.session.add(post)

        self.db.session.commit()

        posts = self.db.session.query(Post).filter(
            post.user_id == user.id
        ).all()
        self.assertEqual(posts[0].user_id, user.id)

        for p in user.posts:
            print(p)

        self.db.session.query(User).delete()
        self.db.session.query(Post).delete()
        self.db.session.commit()
