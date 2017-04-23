from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask.views import MethodView
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

import json
from config import DevConfig


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


class RegistrationForm(FlaskForm):
    username = StringField(
            'Name',
            validators=[DataRequired(), Length(min=2, max=255)]
    )
    password = PasswordField(
            'New Password',
            validators=[DataRequired(), EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField("Send")


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return 'Hi Flask'
    else:
        return 'Hello Flask'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if form.validate_on_submit():
        url = url_for('user_api')
        payload = json.dumps({'username': form.username.data, 'password': form.password.data})
        headers = {'content-type': 'application/json'}

        rv = app.test_client().post(url, data=payload, headers=headers)
        if rv.status_code == 200:
            flash('Success to register')
            return redirect(url_for('user_api'))
        else:
            flash('Fail to register')

    # if request.method == 'POST' and form.validate():
    #     print('username: {}'.format(form.username.data))
    #     print('password: {}'.format(form.password.data))
    #     return redirect(url_for('home'))

    return render_template('register.html', form=form)


class UserAPI(MethodView):
    def get(self, user_id):
        if user_id is None:
            users = db.session.query(User).limit(10).all()

            if not users:
                return 'No data'
            else:
                text = ['user: {}'.format(u.username) for u in users]
                return '<br>'.join(text)

        else:
            user = User.query.get(user_id)
            return 'Hello {}'.format(user.username)

    def post(self):
        if request.headers['Content-Type'] == 'application/json':
            username = request.json['username']
            password = request.json['password']

            db.session.add(User(username, password))
            db.session.commit()
            return 'Done', 200

    def delete(self, user_id):
        db.session.delete(User.query.get(user_id))
        db.session.commit()
        return 'Done', 200

    def put(self, user_id):
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


user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
app.add_url_rule('/users/', view_func=user_view, methods=['POST'])
app.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':
    app.run(port=8080)
