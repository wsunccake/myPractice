from flask import Flask, request
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)

db = SQLAlchemy(app)


class User(db.Model):
    # __tablename__ = 'user'

    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return "<User '{}'>".format(self.username)


@app.route('/')
def home():
    return 'Hello Flask'


@app.route('/users', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        users = db.session.query(User).limit(10).all()
        print(users)

        if not users:
            return 'No data'
        else:
            text = ['user: {}'.format(u.username) for u in users]
            return '<br>'.join(text)

    elif request.method == 'POST':
        if request.headers['Content-Type'] == 'application/json':
            username = request.json['username']
            password = request.json['password']

            db.session.add(User(username, password))
            db.session.commit()

            return 'Done', 200


@app.route('/user/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def user_id_op(user_id):
    if request.method == 'GET':
        user = User.query.get(user_id)
        return 'Hello {}'.format(user.username)

    elif request.method == 'PUT':
        if request.headers['Content-Type'] == 'application/json':
            username = request.json['username']
            password = request.json['password']

            User.query.filter_by(id=user_id).update({
                'username': username,
                'password': password
            })
            db.session.commit()
            return 'Done', 200

        return 'Fail', 501

    elif request.method == 'DELETE':
        db.session.delete(User.query.get(user_id))
        db.session.commit()
        return 'Done', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
